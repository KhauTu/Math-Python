def read_data(path):
    numbers = []
    try:
        with open(path) as f:
            for line in f:
                try:
                    n = float(line)
                except ValueError:
                    print('Bad data: {0}'.format(line))
                    continue
                numbers.append(n)
    except FileNotFoundError:
        print('File not found')
    return numbers