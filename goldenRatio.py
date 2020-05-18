def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x = range(1, 21)
    y_series = fibo(20)
    y = []
    for i in range(20):
        ratio = y_series[i + 1] / y_series[i]
        y.append(ratio)
    plt.plot(x, y)
    plt.title("Ratio between consecutive Fibonacci numbers")
    plt.xlabel("No.")
    plt.ylabel("Ratio")
    plt.show()