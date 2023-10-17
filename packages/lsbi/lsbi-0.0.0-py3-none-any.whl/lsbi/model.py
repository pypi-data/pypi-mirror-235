import numpy as np
from functools import cached_property
from scipy.stats import multivariate_normal, multivariate_t

class LinearModel(object):
    """
    A linear model:

    - Parameters: theta (n,)
    - Data: D (d,)
    - Prior mean: mu (n,) 
    - Prior covariance: Sigma (n, n)
    - Data mean: m (d,)
    - Data covariance: C (d, d)
    - Model M: D = m + M theta +/- sqrt(C)

    Parameters
    ----------
    M : array_like, optional
        Model matrix, defaults to identity matrix
    m : array_like, optional
        Data mean, defaults to zero vector
    C : array_like, optional
        Data covariance, defaults to identity matrix
    mu : array_like, optional
        Prior mean, defaults to zero vector
    Sigma : array_like, optional
        Prior covariance, defaults to identity matrix

    the overall shape is attempted to be inferred from the input parameters
    """
    def __init__(self, *args, **kwargs):

        self.M = self.kwargs.pop('M', None) 
        self.m = self.kwargs.pop('m', None) 
        self.C = self.kwargs.pop('C', None) 
        self.mu = self.kwargs.pop('mu', None) 
        self.Sigma = self.kwargs.pop('Sigma', None) 

        if self.m is not None:
            self.m = np.atleast_1d(self.m) 
            d, = self.m.shape
        if self.C is not None:
            self.C = np.atleast_2d(self.C)
            d, d = self.C.shape
        if Sigma is not None:
            Sigma = np.atleast_2d(Sigma)
            n, n = Sigma.shape
        if self.mu is not None:
            self.mu = np.atleast_1d(self.mu)
            n, = self.mu.shape
        if self.M is not None:
            self.M = np.atleast_2d(self.M) 
            d, n = self.M.shape

        if n is None:
            raise ValueError('Unable to determine parameters dimensions n')
        if d is None:
            raise ValueError('Unable to determine data dimensions d')

        if self.M is None:
            self.M = np.eye(d, n)
        if self.m is None:
            self.m = np.zeros(d)
        if self.C is None:
            self.C = np.eye(d)
        if self.mu is None:
            self.mu = np.zeros(n)
        if Sigma is None:
            self.Sigma = np.eye(n)


    @cached_property
    def invSigma(self):
        return np.linalg.inv(self.Sigma)

    @cached_property
    def invC(self):
        return np.linalg.inv(self.C)

    def likelihood(self, theta):
        return multivariate_normal(self.D(theta), self.C)

    def prior(self):
        return multivariate_normal(self.mu, self.Sigma)

    def posterior(self, D):
        Sigma = np.linalg.inv(self.invSigma + self.M.T @ self.invC @ self.M)
        mu = Sigma @ (self.invSigma @ self.mu
                      + self.M.T @ self.invC @ (D-self.m))
        return multivariate_normal(mu, Sigma)

    def evidence(self):
        return multivariate_normal(self.D(self.mu),
                                   self.C + self.M @ self.Sigma @ self.M.T)

    def joint(self):
        mu = np.concatenate([self.m+self.M @ self.mu, self.mu])
        Sigma = np.block([[self.C+self.M @ self.Sigma @ self.M.T,
                           self.M @ self.Sigma],
                          [self.Sigma @ self.M.T, self.Sigma]])
        return multivariate_normal(mu, Sigma)

    def D(self, theta):
        return self.m + self.M @ theta

    def DKL(self, D):
        cov_p = self.posterior(D).cov
        cov_q = self.prior().cov
        mu_p = self.posterior(D).mean
        mu_q = self.prior().mean
        return 0.5 * (np.linalg.slogdet(cov_p)[1] - np.linalg.slogdet(cov_q)[1]
                      + np.trace(np.linalg.inv(cov_q) @ cov_p)
                      + (mu_q - mu_p) @ np.linalg.inv(cov_q) @ (mu_q - mu_p)
                      - len(mu_p))
