import numpy as np
from math import sqrt

import boxplots
import outlier


def normal_distribution(n):
    return np.random.normal(0, 1, n)


def cauchy_distribution(n):
    return np.random.standard_cauchy(n)


def poisson_distribution(n):
    return np.random.poisson(10, n)


def uniform_distribution(n):
    return np.random.uniform(-sqrt(3), sqrt(3), n)


distributions = [
        ('Normal', normal_distribution),
        ('Cauchy', cauchy_distribution),
        ('Poisson', poisson_distribution),
        ('Uniform', uniform_distribution),
]

# 1
sample_size = [20, 100, 1000]
boxplots.build_boxplots(sample_size, distributions)

# 2
outlier.print_outliers_table(sample_size, distributions)
