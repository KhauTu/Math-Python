'''
Quadratic function calculator
'''
import matplotlib.pyplot as plt

# Assume values of x
x_values = range(-7, 6)
y_values = []
for x in x_values:
    # Calculate the value of the quadratic function
    y = x**2 + 2*x + 1
    y_values.append(y)

plt.plot(x_values, y_values)
plt.title('Quadric Function')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
    
