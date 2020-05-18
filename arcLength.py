from sympy import Integral, Derivative, Symbol, sympify

def arcLength(f, var, var0, var1):
    # derivative of f function
    d = Derivative(f, var)

    i = (1+d**2)**0.5

    # integral to calculate arc length
    ig = Integral(i, (var, var0, var1)).doit().evalf()

    return ig

if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable to differentiate with respect to: ')
    var0 = float(input('Enter the initial value of the variable: '))
    var1 = float(input('Enter the ending value of the variable: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        length = arcLength(f, var, var0, var1)
        print('From initial value {0} to ending value {1}'.format(var0, var1))
        print('Arc length of func {0} is {1}'.format(f, length))
