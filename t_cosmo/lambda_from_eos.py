import pkg_resources

import numpy as np
from scipy.interpolate import interp1d

class LambdaFunc:

    def __init__(self, eos_code):
        path = pkg_resources.resource_filename(__name__,  f'/data/{eos_code}.dat')
        m, lam = np.loadtxt(path)[:,(2,4)].T
        self.func = interp1d(m, lam, fill_value='extrapolate')
    
    def __call__(self, m):
        lam = self.func(m)
        if not np.shape(lam):
            lam = float(lam)
        return lam

get_lambda_from_mass_MPA1 = LambdaFunc('MPA1')
