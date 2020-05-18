'''
Draw a square
'''
from matplotlib import pyplot as plt
def draw_square():
    ax = plt.axes(xlim = (0, 6), ylim = (0, 6))
    square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed = True)
    ax.set_aspect('equal')
    ax.add_patch(square)
    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = plt.Circle((x, y), 0.5, fc = 'w')
            ax.add_patch(c)
            x += 1.0
        y += 1.0
    plt.show()

if __name__ == '__main__':
    draw_square()