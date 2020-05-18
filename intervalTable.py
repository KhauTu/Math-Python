import matplotlib.pyplot as plt

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)
    
    # Width of each class
    width = (high - low)/n
    classes = []
    a = low
    b = low + width
    classes = []
    while a < (high-width):
        classes.append((a, b))
        a = b
        b = a + width
    # The last class may be of a size that is less than width
    classes.append((a, high+1))
    return classes

def interval_table(numbers, n):
    interval_lst = create_classes(numbers, n)
    freq = []
    
    for interval in interval_lst:
        count = 0
        for num in numbers:
            if interval[0] <= num < interval[1]:
                count += 1
        freq.append((num + 1, count))
    return interval_lst, freq

if __name__ == '__main__':
    numbers = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    n = 7
    interval_lst, freq = interval_table(numbers, n)
    
    freq_lst = []
    int_lst = []
    print('{:>15}\t{:^10}'.format('Interval', 'Frequency'))
    for i in range(len(interval_lst)):
        print('{:>15}\t{:^10}'.format(str(interval_lst[i]), str(freq[i][1])))
        freq_lst.append(freq[i][1])
        int_lst.append((interval_lst[i][0] + interval_lst[i][1])/2)

    plt.scatter(int_lst, freq_lst)
    plt.show()