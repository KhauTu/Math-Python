'''
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final, interval):
    
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    
    return numbers

def draw_trajectory(u, theta):
    
    theta = math.radians(theta)
    g = 9.8
    
    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    # Find time intervals
    intervals = frange(0, t_flight, 0.001)
    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)

def parameter(u, theta):
    theta = math.radians(theta)
    g = 9.8

    t_flight = 2*u*math.sin(theta)/g
    hor = u*math.cos(theta)*t_flight
    t = t_flight / 2
    ver = u*math.sin(theta)*t - 0.5*g*t*t

    print('Time of flight %.2f (s)' % t_flight)
    print('Maximum horizontal distance: %.2f (m)' % hor)
    print('Maximum vertical distance: %.2f (m)' % ver)

if __name__ == '__main__':
    '''
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u, theta)
        plt.show()
    '''

    print('How many trajectories?')
    N = int(input())

    # List of three different initial velocities
    for i in range(N):
        print("Enter the initial velocity for trajectory %d (m/s): " % (i + 1))
        u = float(input())
        print("Enter the angle of projection for trajectory %d (degrees): " % (i + 1))
        theta = float(input())
        draw_trajectory(u, theta)
        parameter(u, theta)
    # Add a legend and show the graph
    # plt.legend(['20', '40', '60', '45'])
    plt.show()