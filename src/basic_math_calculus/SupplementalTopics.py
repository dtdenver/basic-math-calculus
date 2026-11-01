# CDF and Inverse CDF from Scratch
# Example A-7 Generating random golder retriever weights

import random
from matplotlib.pylab import mean
from scipy.special import erf, erfinv

def inv_normal_cdf(p: float, mean: float, std_dev: float) -> float:
    return mean + (std_dev * (2.0 ** 0.5) * erfinv(2.0 * p - 1.0))

mean = 64.43
std_dev = 2.99

for i in range(1000):
    random_p = random.uniform(0.0, 1.0)
    print(inv_normal_cdf(random_p, mean, std_dev))





# # Example A-6 Using the inverse CDF (called ppf()) in Python

# import math

# def normal_cdf(x:float, mean:float, std_dev:float) -> float:
#    """Calculates the cumulative distribution function of a normal distribution."""
#    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))

# mean = 64.43
# std_dev = 2.99

# x = normal_cdf(66, mean, std_dev) - normal_cdf(62, mean, std_dev)

# print(x) # prints 0.49204501470628936













# Example A-5 The normal distribution function in Python

# import math

# def normal_pdf(x:float, mean:float, std_dev:float) -> float:
#     """Calculates the probability density function of a normal distribution."""
#     # exponent = -0.5 * ((x - mean) / std_dev) ** 2
#     # coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
#     # return coefficient * math.exp(exponent)
#     return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * math.exp(-1 * ((x - mean) ** 2) / (2.0 * std_dev ** 2))

# def approximat_integral(a:float, b:float, n:int, f) -> float:
#     """Approximates the integral of a function f from a to b using the midpoint rule."""
#     delta_x = (b - a) / n
#     total_sum = 0.0

#     for i in range(1, n + 1):
#         midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
#         total_sum += f(midpoint)
#     return total_sum * delta_x

# p_between_61_and_62 = approximat_integral(a=61, b=62, n=7, f=lambda x: normal_pdf(x, 64.43, 2.99))

# print(p_between_61_and_62) # prints 0.0825344984983386


# def normal_cdf(x:float, mean:float, std_dev:float) -> float:
#     """Calculates the cumulative distribution function of a normal distribution."""
#     return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))

# def inverse_normal_cdf(p:float, mean:float, std_dev:float) -> float:
#     """Calculates the inverse cumulative distribution function of a normal distribution."""
#     if p < 0 or p > 1:
#         raise ValueError("p must be between 0 and 1")
#     return mean + std_dev * math.sqrt(2) * math.erfinv(2 * p - 1)





# Deriving Bayes Theorem



# # Beta Distribution from Scratch

# # Example A-4 Beta distribution from scratch
# # EXAMPLE: 5! = 5*4*3*2*1 = 120
# def factorial(n:int):
#     f = 1
#     for i in range(n):
#         f *= (i + 1)
#     return f

# def approximate_integral(a:float, b:float, n:int, f):
#     delta_x = (b - a) / n
#     total_sum = 0.0

#     for i in range(1, n + 1):
#         midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
#         total_sum += f(midpoint)
#     return total_sum * delta_x

# def beta_distribution(x:float, alpha:int, beta:int) -> float:
#     if x < 0.0 or x > 1.0:
#         raise ValueError("x must be between 0 and 1")

#     numerator = x**(alpha - 1.0) * (1.0 - x)**(beta - 1.0)
#     denominator = (1.0 *  factorial(alpha - 1) * factorial(beta - 1)) / (1.0 * factorial(alpha + beta - 1))

#     return numerator / denominator

# greater_than_90 = approximate_integral(a=.90, b=1.0, n=1_000, f=lambda x: beta_distribution(x, 8, 2))
# less_than_90 = 1.0 - greater_than_90

# print ("GREATER THAN 90%: {}, LESS THAN 90%: {}".format(greater_than_90, less_than_90))










# # Binominial Distribution from Scratch

# # Example A-3 Building a binomial distribution from scratch

# # Factorials multiply consecutive descending integers down to 1
# # EXAMPLE: 5! = 5*4*3*2*1 = 120
# def factorial(n:int):
#     f = 1
#     for i in range(n):
#         f *= (i + 1)
#     return f
    
# # Generates the coefficent needed for the binomial distribution
# def binomial_coefficient(n:int, k:int):
#     return factorial(n) / (factorial(k) * factorial(n - k))

# # Binomial distribution calculates the probability of k events out n trials
# # given the probability of K occurring
# def binomial_distribution(n:int, k:int, p:float):
#     return binomial_coefficient(n, k) * (p ** k) * (1.0 - p) ** (n - k)

# # 10 trials where each has 90% success probability
# n = 10
# p = 0.9

# for k in range(n + 1):
#     probability = binomial_distribution(n, k, p)
#     print("{0} - {1}".format(k, probability))










# Using LaTeX Rendering with SymPy

# Example A-2 Open a mathlatex rendering using CodeCogs

# import webbrowser
# from sympy import sqrt, symbols, latex

# x,y = symbols('x y')

# z = x**2 / sqrt(2*y**3 - 1)

# webbrowser.open("https://latex.codecogs.com/png.latex?\\pi{200}" + latex(z))





# Example A-1 Using SymPy to convert an expression into LaTeX
# from sympy import sqrt, symbols, latex

# x,y = symbols('x y')

# z = x**2 / sqrt(2*y**3 - 1)

# print(latex(z)) # \frac{x^{2}}{\sqrt{2 y^{3} - 1}}

# prints
# \frac{x^{2}}{\sqrt{2 y^{3} - 1}}