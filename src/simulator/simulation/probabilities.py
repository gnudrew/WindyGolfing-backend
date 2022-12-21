"""Probability function generators used by SimTrialRunner"""

class ProbGen:
    """Base class for probability function generators"""
    pass

class UniformProbGen(ProbGen):
    """Generate Uniform probability functions"""
    def __init__(self, x_min=None, x_max=None, **kwargs):
        self.x_min = x_min
        self.x_max = x_max

    def generate_fn(self):
        """Generate a normalized probability density function (pdf)"""
        def pdf(x):
            if x < self.x_min:
                return 0
            elif x > self.x_max:
                return 0
            else:
                return 1/(self.x_max-self.x_min)
        return pdf

    def generate_inv_fn(self):
        """Generate the inversion of the pdf"""
        pass

class NormalProbGen(ProbGen):
    """Generate Normal probabilibty functions"""
    pass

class LogNormalProbGen(ProbGen):
    """Generate Log-normal probability functions"""
    pass
