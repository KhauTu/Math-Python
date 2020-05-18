import random

def toss():
    # 0 -> Heads, 1-> Tails
    if random.random() < 1/2:
        return 0
    else:
        return 1

if __name__ == '__main__':
    print('Enter your starting amount: ')
    a = float(input())
    c = 0
    while a > 0:
        c += 1
        if toss():
            a += 1
            print('Heads! Current amount: ', a)
        else:
            a -= 1.5
            print('Tails! Current amount: ', a)
    print('Game over :( Current amount: {0}. Coin tosses: {1}'.format(a, c))