# from scipy.stats import binom

from scipy.stats import binomtest
from math import comb
# # chapter 2 Understanding Probability
# # Excercise 5


result = binomtest(k=15, n=19, p=0.5, alternative='two-sided')
print(f"p-value: {result.pvalue:.4f}")

alpha = 0.05
if result.pvalue < alpha:
    print("Reject the null hypothesis: the coin is likely NOT fair.")
else:
    print("Fail to reject the null hypothesis: no strong evidence the coin is unfair.")



m = sum(comb(19, k) for k in range(15, 20)) / 2**19 * 2
print(f"Manual p-value: {m:.4f}")


# # # Excercise 4

# n = 137
# p = .40

# p_50_or_more_no_shows = 0.0

# for x in range(50, n + 1):
#     p_50_or_more_no_shows += binom.pmf(x, n, p)

# print(p_50_or_more_no_shows)





# # Excercise 3 Conditional p 47
# p_rain_today = 0.3
# p_umbrella_arrives = 0.2
# p_conditional = p_rain_today * p_umbrella_arrives
# print(p_conditional) # prints 0.06








# # Excercise 2 OR p 45
# p_rain_today = 0.3
# p_umbrella_arrives = 0.4
# p_OR = ((1 -p_rain_today) + p_umbrella_arrives) - (p_rain_today * p_umbrella_arrives)
# print(p_OR) # prints 0.7






# # Exercise 1 AND p 44

# p_rain_today = 0.3
# p_umbrella_arrives = 0.4
# p_AND = p_rain_today * p_umbrella_arrives
# print(p_AND) # prints 0.12





















# # example 2-6 Beta distribution middle area using SciPy

# a = 8
# b = 2

# p = beta.cdf(0.90, a, b) - beta.cdf(0.80, a, b)

# # 0.33863336200000016
# # 0.33863336199999994

# print(p)







# # example 2.5 A beta distribution with more trials

# a = 30
# b = 6

# p = 1.0 - beta.cdf(0.90, a, b)

# # 0.13163577484183708
# # 0.13163577484183697

# print(p)




# # example 2.4 Subtracting to get a right area in a beta distribution

# a = 8
# b = 2

# p = 1.0 - beta.cdf(0.90, a, b)

# # 0.22515902199999993
# # 0.22515902199999982

# print(p)





# # example 2.3 Beta distribution using SciPy

# a = 8
# b = 2

# p = beta.cdf(0.90, a, b)

# # 0.7748409780000001
# # 0.7748409780000002
# print(p)


# # example 2.2 Using SciPy for the binomial distribution

# n = 10
# p = 0.9

# for k in range (n + 1):
#     probability = binom.pmf(k, n, p)
#     print("{0} - {1}".format(k, probability))

# OUTPUT

# 0 - 9.999999999999998e-11
# 1 - 8.999999999999998e-09
# 2 - 3.645000000000001e-07
# 3 - 8.748000000000001e-06
# 4 - 0.00013122000000000002
# 5 - 0.0014880349999999998
# 6 - 0.010077696000000001
# 7 - 0.05739562800000001
# 8 - 0.19371024499999998
# 9 - 0.3874204890000001
# 10 - 0.3486784401000001
          

# 0 - 9.999999999999977e-11
# 1 - 8.999999999999978e-09
# 2 - 3.6449999999999943e-07
# 3 - 8.747999999999991e-06
# 4 - 0.00013778099999999974
# 5 - 0.0014880347999999982
# 6 - 0.011160260999999996
# 7 - 0.05739562799999997
# 8 - 0.1937102444999998
# 9 - 0.38742048899999976
# 10 - 0.3486784401000001




# # example 2.1 Using Bayes' theorem in Python

# p_coffee_drinker = 0.65
# p_cancer = 0.005
# p_coffee_drinker_given_cancer = 0.85

# p_cancer_given_coffee_drinker = (p_coffee_drinker_given_cancer * p_cancer) / p_coffee_drinker
# # prints 0.006538461538461539
# #        0.006538461538461539    

# print(p_cancer_given_coffee_drinker)






# # # chapter 1 question 8

# # Declare 'x' to SymPy
# x = symbols('x')

# # Now just use Python syntax to declare function
# f = 3*x**2 + 1

# # Calculate the integral of the function with respect to x
# # for the area between x = 0 and 2
# area = integrate(f, (x, 0, 2))










# # # chapter 1 question 7

# # Declare 'x' to SymPy
# x = symbols('x')

# # Now just use Python syntax to declare function
# f = 3*x**2 + 1

# # Calculate the derivative of the function
# dx_f = diff(f)
# print(dx_f) # prints 6*x
# print(dx_f.subs(x,3)) # 18





# from math import exp

# # # chapter 1 question 6

# p = 1000 # principal, starting amount
# r = .05 # interest rate, by year
# t = 3.0 # time, number of years

# a = p * exp(r*t)

# print(a) # prints 1161.834242728283










# from math import exp

# # chapter 1 question 5

# p = 1000
# r = .05
# t = 3
# n = 12

# a = p * (1 + (r/n)) **(n*t)

# print(a) # prints 1161.4722313334678


# # Example 1-30 Using limits to calculate integrals

# # Declare variables to SymPy
# x, i, n = symbols('x i n')

# # Declare function and range
# f = x**2 + 1
# lower, upper = 0, 1

# # Calculate width and each rectangle height at index 'i'
# delta_x = ((upper - lower) / n)
# x_i = (lower + delta_x * i)
# fx_i = f.subs(x, x_i)

# # Iterate all 'n' rectangles and sum their area
# n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# # Calculate the area by approaching the number
# # of rectangles 'n' to infinity
# area = limit(n_rectangles, n, oo)

# print(area) # prints 4/3












# # 1-29 Using SymPy to perform integration

# # Declare 'x' to SymPy
# x = symbols('x')

# # Now just use Python syntax to declare function
# f = x**2 + 1

# # Calculate the integral of the function with respect to x
# # for the area between x = 0 and 1
# area = integrate(f, (x, 0 ,1))

# print(area) # prints 4/3


# example 1-28 Yet another integral approximation in Python

# example 1-27 Another integral approximation in Python

# # example 1-26 An integral approximation in Python

# def approximate_integral(a, b, n, f):
#     delta_x = (b - a) / n
#     total_sum = 0

#     for i in range(1, n + 1):
#         midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
#         total_sum += f(midpoint)

#     return total_sum * delta_x

# def my_function(x):
#     return x**2 + 1

# area = approximate_integral(a=0, b=1, n=1_000_000, f=my_function)

# print(area) # prints 1.3



# # example 1-25 Calculating the derivative dz/dx with and without the chain rule, but still getting the same answer

# x, y = symbols('x y')

# # derivative for first function
# # need to underscore y to prevent variable clash
# _y = x**2 + 1
# dy_dx = diff(_y)

# # derivative for second function
# # chain rule, substitute y function
# z = y**3 - 2
# dz_dy = diff(z)

# # Calculate the derivative with and without
# # chain rule, substitute y function
# dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
# dz_dx_no_chain = diff(z.subs(y, _y))

# # Prove change rule by showing both are equal
# print(dz_dx_chain) # 6*x*(x**2 + 1)**2
# print(dz_dx_no_chain) # 6*x*(x**2 + 1)**2







# # example 1-24 Finding the derivative of z with respect to x

# x = symbols('x')

# z = (x**2 + 1)**3 - 2

# dz_dx = diff(z,x)

# print(dz_dx) # 6*x*(x**2 + 1)**2















# # example 1.23 Using limits to calculate a derivative
# # 'x' and step_size 's'
# x, s = symbols('x s')

# # declare function
# f = x**2

# # slope between two points with gap "s"
# # substitute into rise-over-run formula
# slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# # calculate derivative function
# # infinitely approach step size +s+ to 0
# result = limit(slope_f, s, 0)

# print(result) # 2x















# # example 1.22
# # 'x' and step_size 's'
# x, s = symbols('x s')

# # declare function
# f = x**2

# # slope between two points with gap 's'
# # substitute into rise-over-run formula
# slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# # substitute 2 for x
# slope_2 = slope_f.subs(x, 2)

# # calculate slope at x = 2
# # infinitely approach step size _s_ to 0
# result = limit(slope_2, s, 0)

# print(result) # 4












# from sympy.plotting import plot3d

# # Declare x and y to SymPy
# x,y = symbols('x y')

# # Now just use python syntax to declare function
# f = 2*x**3 + 3*y**3

# # Calculate the partial derivatives for x and y
# dx_f = diff(f,x)
# dy_f = diff(f,y)

# print(dx_f) # prints 6*x**2
# print(dy_f) # prints 9*y**2

# # plot the function
# plot3d(f)

















# # from basic_math_calculus.calculus import derivative

# # declare 'x' to sympy
# x = symbols('x')

# def f(x):
#     return x**2

# def dx_f(x):
#     return 2*x

# slope_at_2 = dx_f(2.0)

# print(slope_at_2) # prints 4.0
# print(dx_f(x).subs(x,2)) # prints 4
















# # declare 'x' to sympy
# x = symbols('x')

# # declare function
# f = x**2

# # calculate the derivative of the function
# dx_f = diff(f)
# print(dx_f) # prints 2*x

# def derivative_x(f,x,step_size):
#     m = (f(x+step_size) - f(x))/((x + step_size)-x)
#     return m

# def my_function(x):
#     return x**2

# slope_at_2 = derivative_x(my_function,2,.00001)

# print(slope_at_2)

# def test_derivative():
#     x = symbols("x")
#     assert derivative(x**2 + 1, x) == 2 * x