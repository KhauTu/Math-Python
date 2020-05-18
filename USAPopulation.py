# Age-population-age-24-male-interpolated-United-States
# File name: WHNP-USA_SP_POP_AG24_MA_IN.csv

from readCSV import read_data
from findMode import calculate_mean, calculate_median, calculate_mode
from findVarianceSD import calculate_variance
import matplotlib.pyplot as plt
import csv

def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        pop = []
        date = []
        for row in reader:
            pop.append(float(row[1]))
            date.append(row[0])
        diff = []
        for i in range(1, len(pop)):
            diff.append(pop[i-1]-pop[i])
    return diff, date

mydata, datedata = read_csv('WHNP-USA_SP_POP_AG24_MA_IN.csv')
mean = calculate_mean(mydata)
median = calculate_median(mydata)
mode = calculate_mode(mydata)
variance = calculate_variance(mydata)
std = variance**0.5
print(variance)

datedata.pop(0)

plt.plot(datedata, mydata, 'r*')
plt.title('Age-population-age-24-male-interpolated-United-States')
positions = range(1, len(datedata) + 1)
plt.xticks(positions, datedata, rotation = 90)
plt.xlabel('Timeline')
plt.ylabel('Population age 24')
plt.show()