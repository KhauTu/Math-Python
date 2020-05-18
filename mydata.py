from readCSV import read_data
from findMode import calculate_mean, calculate_median, calculate_mode
from findVarianceSD import calculate_variance

mydata = read_data('mydata.txt')
mean = calculate_mean(mydata)
median = calculate_median(mydata)
mode = calculate_mode(mydata)
variance = calculate_variance(mydata)
std = variance**0.5
print(mydata)
print('mean: {0:.2f}\nmode: {1}\nmedian: {2:.2f}\nvariance: {3:.2f}\nstd: {4:.2f}'.format(mean, mode, median, variance, std))