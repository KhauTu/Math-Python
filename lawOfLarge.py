import random

def roll():
    return random.randint(1, 6)

def expect_value(trial):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    for i in range(trial):
        r = roll()
        if r == 1:
            count1 += 1
        if r == 2:
            count2 += 1
        if r == 3:
            count3 += 1
        if r == 4:
            count4 += 1
        if r == 5:
            count5 += 1
        if r == 6:
            count6 += 1
    # print(count1, count2, count3, count4, count5, count6)
    # print(sum([count1, count2, count3, count4, count5, count6]))
    eValue = (1*count1 + 2*count2 + 3*count3 + 4*count4 + 5*count5 + 6*count6)/trial
    print('Expected value: 3.5')
    print("Trials: {0} \tTrial average {1}".format(trial, eValue))

if __name__ == '__main__':
    for trial in [100, 1000, 10000, 100000, 500000]:
        expect_value(trial)