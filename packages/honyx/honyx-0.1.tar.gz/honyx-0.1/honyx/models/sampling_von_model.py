"""
Module giving access to the SamplingVONModel.
"""

import numpy as np
from scipy.special import comb, rel_entr, rel_entr, loggamma
from math import exp, log, log2

from honyx.models.hon_model import HONModel

######################################################################################
def _kl_divergence_vect(c_p, c_q, n_p, n_q):
    """Compute the kullback divergence  between numpy vectors c_q and c_p

    Parameters
    ----------
    c_p: 1D np-array
    c_q: 1D np-array
    n_p: sum of c_p
    n_q: sum of c_q
    """
    res = 0.
    for i in range(len(c_p)):
        if c_p[i] > 0:
            res += (c_p[i]/n_p)/(c_q[i]/n_q)*log2((c_p[i]/n_p)/(c_q[i]/n_q))
    return res
    # return sum(rel_entr(c_p/n_p, c_q/n_q))

######################################################################################
def _fast_binom_pmf(s_n, k, prob):
    """Compute the probability to have k sucess with probability prob among s_n trials 
    using the loggamma function
    
    Parameters
    ----------
    s_n: int
        number of trials
    k: int
        number of sucess
    prob: float [0,1]
        probability of sucess

    Notes
    -----
    see
    `scipy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.loggamma.html#scipy.special.loggamma>`_.
    """
    return exp(loggamma(s_n+1)-loggamma(k+1)-loggamma(s_n-k+1)+k*log(prob)+(s_n-k)*log(1.-prob))

######################################################################################
class SamplingVONModel(HONModel):
    """
    A context is considered valid if the p-value of its divergence from the last 
    valid context is less than the confidence threshold ('ct' attribute).
    The p-value is computed using controlled a Monte-carlo sampling.
    The maximum number of samples is chosen in order to control a given resampling risk ('risk' attribute). 

    Notes
    -----
    Inherit :class:`hon_model.HONModel`

    Attributes
    ----------
    ct : float
        Defines a significance threshold used to verify validity.
    risk: float
        in [0,1]. The resampling risk
    r: float 
        > 1. Asymmetric risk parameter
    method: str ['marginals', 'count']
        method used for multivariate_hypergeometric draws
    """
    def __init__(self, max_order, min_support, ct, risk = 0.1, r = 3., method='marginals'):
        HONModel.__init__(self, max_order, min_support)
        self.ct = ct
        self.risk = risk
        self.r = r
        self.method = method
        self.lim_nb_draws = self.max_nb_draws()
        self.rng_gen =  np.random.default_rng()

    ######################################################################################
    def get_name(self):
        """Overrides to give the name of this model."""
        return "samp"

    ######################################################################################
    def get_params_str(self, short=False):
        """Extends to show the extra information in the model (which is pval)."""
        base_params = super().get_params_str(short)
        return (base_params+ f"ct:{self.ct};risk:{self.risk};r:{self.r}")
    
    ######################################################################################
    def max_nb_draws(self):
        if self.r <= 1. :
            return 999999
        ## find p such that B(n, α, np) = B(n, r*α, np)
        p_crit = log((1.-self.r*self.ct)/(1.-self.ct))/(log((1.-self.r*self.ct)/(1.-self.ct)) - log(self.r))
        ## find n such that (n+1) * B(n, α, np) <=  ϵ
        inc = 100000
        max_n = 0
        while inc >= 1:
            for k in range(1,11):
                i = max_n + k*inc
                if (i+1.)*_fast_binom_pmf(i, i*p_crit, self.r*self.ct) <= self.risk:
                    break
            max_n = i - inc
            inc = int(inc/10)
        return max_n

    ######################################################################################
    def is_valid_csm(self, c_val, n_e, kld, n_max=50000, risk = 0.25):
        """TODO"""
        n_v = np.sum(c_val)
        Sn = 0
        i=1
        for draw in self.rng_gen.multivariate_hypergeometric(c_val, n_e, size=self.lim_nb_draws, method=self.method):
            kld_t = _kl_divergence_vect(draw, c_val, n_e, n_v)
            if kld_t >= kld:
                Sn += 1
            if i >= 10 :            
                Bn = (i+1.)*min(_fast_binom_pmf(i, Sn, self.r*self.ct), _fast_binom_pmf(i, Sn, self.ct))
                if Bn <= self.risk:
                    break
            i += 1
        return (Sn+1.) / (i+1.) <= (self.r+1.)*self.ct/2. 

    ######################################################################################
    def is_context_valid(self, valid, ext):
        """Overrides to determinate if the given context is valid or not for this model."""

        dict_val = self.count[valid]
        dict_ext = self.count[ext]

        c_val, c_ext = np.zeros(len(dict_val), dtype=int), np.zeros(len(dict_val), dtype=int)
        index = 0
        for key, val in dict_val.items():
            c_val[index] = val            
            if key in dict_ext:
                c_ext[index] = dict_ext[key]
            index += 1

        k = len(c_val)
        n_v = int(np.sum(c_val))
        n_e = int(np.sum(c_ext))

        assert n_e > 0, 'Error: no obs. of extended context.'

        ## Test trivial cases
        if n_v <= 1 or k == 1 or n_e == n_v or np.max(c_val)==1:
            return False

        ext_kld = _kl_divergence_vect(c_ext, c_val, n_e, n_v)
        
        return self.is_valid_csm(c_val, n_e, ext_kld)

    ######################################################################################

    def is_ever_valid(self, valid, curr):
        """Overrides to determinate if the given context can have a valid extension
        for this model."""

        return True

    ######################################################################################
