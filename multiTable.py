'''
Multiplication table printer
'''
def multi_table(a, n):
    for i in range(1, n+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    n = input('Enter number of multiples: ')
    multi_table(float(a), int(n))