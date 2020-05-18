# a program that will take a set of numbers in a file and 
# display the number that corresponds to a specific percentile supplied as an input to the program.

def percentile_num(data, p):
    import math
    data.sort()
    i = (len(data) + 1) * p / 100 # i = np/100 + 0.5
    print('i =', i)
    k = math.floor(i) # integral part of i
    f = i - k # fractional part of i
    print('k =',k)

    num = (1-f)*data[k - 1] + f*data[k]
    return num # number at percentile p

if __name__ == '__main__':
    data = [5, 1, 9, 3, 14, 9, 7]
    p = 50
    num = percentile_num(data, p)
    print('{0} percentile of data is {1}'.format(p, num))
