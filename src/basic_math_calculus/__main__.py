"""Command-line entry point: `python -m myproject` or `myproject`."""

# from math import log

import argparse

from basic_math_calculus import __version__, greet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="basic-math-calculus", description=__doc__)
    parser.add_argument("name", nargs="?", default="world", help="who to greet")
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0

from sympy import *
# from sympy.plotting import plot3d

# def main():
#     n = symbols('n')
#     f = (1 + (1/n))**n
#     result = limit(f,n,oo)
#     print(result) # E
#     print(result.evalf()) # 2.71828182845905 
    # x = symbols('x')
    # f = 1/x
    # result = limit(f,x,oo)
    # print(result) # 0
    # e raised to what power gives us 10
    # x = log(10)
    # print(x) # prints 
    # p = 100 # principal, starting amount
    # r = .20 # interest rate, by year
    # t = 2.0 # time, number of years
    # # n = 12

    # # a = p * (1 + (r/n))**(n * t)
    # a = p * exp(r*t)
    # print(a) # prints 149.18246976412703

    # 2 raised to what power gives me 8?
    # x = log(8,2)
    # print(x) # prints 3.0
    # x, y = symbols('x y')
    # f = 2*x +3*y
    # plot3d(y)
    # x = [1,4,6,2]
    # n = len(x)
    # summation = sum(10*x[i] for i in range(0,n))
    # print(summation)
    # i,n = symbols('i n')
    # # iterate each element i from 1 to n
    # # then multiply and sum
    # summation = Sum(2*i,(i,1,n))

    # x = symbols('x')
    # expr = x**2 / x**5
    # print(expr) # x**(-3)

    # specify n as 5
    # iterating the numbers 1 through 5
    # up_to_5 = summation.subs(n,5)
    # print(up_to_5.doit()) # 30

if __name__ == "__main__":
    raise SystemExit(main())
