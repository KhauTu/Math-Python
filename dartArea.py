import random
import math

def dart_area(r, T):
    # r is radius of dartboard, T is number of throwing times
    a = 0
    b = r*2
    N = 0
    for i in range(T):
        # x, y is the coordinate of throwing dart on board
        x = random.uniform(a, b)
        y = random.uniform(a, b)
        # distance from (1, 1) to (x, y)
        distance = ((r-x)**2 + (r-y)**2)**0.5
        if distance <= r:
            N += 1
    f = N/T # the fraction of darts that land inside the circle.
    A = 4*(r**2)
    area = f * A # estimated area of circle
    p = 4 * f
    return area, p

if __name__ == '__main__':
    print('Radius: ', end = '')
    r = float(input())
    for T in [1000, 100000, 1000000]:
        a = math.pi * r**2
        area, p = dart_area(r, T)
        print('Area: {0}, Estimated ({1} darts): {2}'.format(a, T, area))
        print('Estimated pi: ', p)
