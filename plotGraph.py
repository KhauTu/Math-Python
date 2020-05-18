'''
Plot the graph of an input expression
'''
from sympy import Symbol, sympify, solve
from sympy.core.sympify import SympifyError
from sympy.plotting import plot

def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)

if __name__=='__main__':
    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        plot_expression(expr1)
        plot_expression(expr2)
    y = Symbol('y')
    plot(solve(expr1, y)[0], solve(expr2, y)[0])
    soln = solve((expr1, expr2), dict=True)
    print(soln)