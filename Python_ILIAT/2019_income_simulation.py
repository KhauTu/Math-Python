# from sympy import FiniteSet
from itertools import product
import random
import csv

# 0. Function coverting variables to set of scenarios:
def set_scen(min,max,step):
    lst = []
    while min <= max:
        lst.append(min)
        if step == 0:
            break
        min += step
    s = set(lst)
    # s = FiniteSet(*lst)
    return s

# 1. List of all Variavles
# 1.1 inputVar variables:
inputVar = {
    'no_Class_set': {
        'level1': set_scen(2,4,1), # (1)
        'level2': set_scen(2,3,1), # (1)
        'level3': set_scen(1,2,1), # (1)
        '100': set_scen(1,2,1), # (1)
        '200': set_scen(1,1,0), # (1)
    },
    'no_Student_set': {
        'level1': set_scen(18,30,4), # (2)
        'level2': set_scen(16,24,4), # (2)
        'level3': set_scen(10,16,3), # (2)
        '100': set_scen(6,12,3), # (2)
        '200': set_scen(3,9,3), # (2)
    },
    'pct_Retake_set': {
        'level1': set_scen(.06,.15,.03), # (3)
        'level2': set_scen(.06,.15,.03), # (3)
        'level3': set_scen(.06,.15,.03), # (3)
        '100': set_scen(0,0,0), # (3)
        '200': set_scen(0,0,0), # (3)
    },
    'Price_set': {
        'level1': set_scen(7750000,9750000,500000), # (4)
        'level2': set_scen(8250000,10250000,500000), # (4)
        'level3': set_scen(8500000,10500000,500000), # (4)
        '100': set_scen(2400000,2400000,0), # (4)
        '200': set_scen(2400000,2400000,0), # (4)
    },
    'pct_Share_set': {
        'level1': set_scen(.07,.16,.03), # (5.1)
        'level2': set_scen(.07,.16,.03), # (5.1)
        'level3': set_scen(.07,.16,.03), # (5.1)
        '100': set_scen(0,0,0), # (5.1)
        '200': set_scen(0,0,0), # (5.1)
    },
    'pct_Group_of_2_set':{
        'level1': set_scen(.25,.40,.05), # (5.2)
        'level2': set_scen(.25,.40,.05), # (5.2)
        'level3': set_scen(.25,.40,.05), # (5.2)
        '100': set_scen(0,0,0), # (5.2)
        '200': set_scen(0,0,0), # (5.2)
    },
    'pct_Current_set': {
        'level1': set_scen(.12,.20,.02), # (5.3)
        'level2': set_scen(.12,.20,.02), # (5.3)
        'level3': set_scen(.12,.20,.02), # (5.3)
        '100': set_scen(0,0,0), # (5.3)
        '200': set_scen(0,0,0), # (5.3)
    },
    'pct_Tuition_be4_8_set': {
        'level1': set_scen(.35,.40,.05), # (5.4)
        'level2': set_scen(.35,.40,.05), # (5.4)
        'level3': set_scen(.35,.40,.05), # (5.4)
        '100': set_scen(0,0,0), # (5.4)
        '200': set_scen(0,0,0), # (5.4)
    },
    'pct_Tuition_be4_9_set': {
        'level1': set_scen(.35,.40,.05), # (5.5)
        'level2': set_scen(.35,.40,.05), # (5.5)
        'level3': set_scen(.35,.40,.05), # (5.5)
        '100': set_scen(0,0,0), # (5.5)
        '200': set_scen(0,0,0), # (5.5)
    },
    'room_Rent_set': {
        'level1': set_scen(250000,300000,50000), # (6)
        'level2': set_scen(250000,300000,50000), # (6)
        'level3': set_scen(250000,300000,50000), # (6)
        '100': set_scen(250000,300000,50000), # (6)
        '200': set_scen(250000,300000,50000), # (6)
    },
    'no_Lecture_set': {
        'level1': set_scen(36,36,0), # (7)
        'level2': set_scen(35,35,0), # (7)
        'level3': set_scen(34,34,0), # (7)
        '100': set_scen(15,15,0), # (7)
        '200': set_scen(15,15,0), # (7)
    },
    'no_Coach_set': {
        'level1': set_scen(17,17,0), # (8)
        'level2': set_scen(18,18,0), # (8)
        'level3': set_scen(18,18,0), # (8)
        '100': set_scen(9,9,0), # (8)
        '200': set_scen(10,10,0), # (8)
    },
    'wage_Lecture_set': {
        'level1': set_scen(500000,700000,100000), # (9)
        'level2': set_scen(600000,800000,100000), # (9)
        'level3': set_scen(600000,1000000,200000), # (9)
        '100': set_scen(500000,700000,100000), # (9)
        '200': set_scen(600000,800000,100000), # (9)
    },
    'wage_Coach_set': {
        'level1': set_scen(400000,500000,50000), # (10)
        'level2': set_scen(500000,600000,50000), # (10)
        'level3': set_scen(600000,600000,0), # (10)
        '100': set_scen(400000,500000,50000), # (10)
        '200': set_scen(500000,600000,50000), # (10)
    },
    'pct_Scholar_set': {
        'level1': set_scen(0,0,0), # (12)
        'level2': set_scen(0,0,0), # (12)
        'level3': set_scen(.04,.06,.02), # (12)
        '100': set_scen(.18,.22,.02), # (12)
        '200': set_scen(.08,.10,.02), # (12)
    },
    'material_Exp_set': {
        'level1': set_scen(20000,30000,10000), # (13)
        'level2': set_scen(20000,30000,10000), # (13)
        'level3': set_scen(20000,30000,10000), # (13)
        '100': set_scen(10000,20000,10000), # (13)
        '200': set_scen(10000,20000,10000), # (13)
    },
    'pct_Cal_set': {
        'level1': set_scen(.60,.70,.10), # (14)
        'level2': set_scen(0,0,0), # (14)
        'level3': set_scen(0,0,0), # (14)
        '100': set_scen(0,0,0), # (14)
        '200': set_scen(0,0,0), # (14)
    }
}

name_Class = ['level1', 'level2', 'level3', '100', '200']

for name in name_Class:
    no_Class = inputVar['no_Class_set'][name] # X1
    # print(no_Class)
    no_Student = inputVar['no_Student_set'][name] # X2
    # print(no_Student)
    pct_Retake = inputVar['pct_Retake_set'][name] # X3
    # print(pct_Retake)
    Price = inputVar['Price_set'][name] # X4
    # print(pct_Retake)

    pct_Share = inputVar['pct_Share_set'][name] # X51
    X51p = price_Share = 250000 # (5.1p) fixed # X51p

    pct_Group_of_2 = inputVar['pct_Group_of_2_set'][name] # X52
    X52p = price_Group_of_2 = 300000 # (5.2p) fixed # X52p

    pct_Current = inputVar['pct_Current_set'][name] # X53
    X53p = price_Current = 500000 # (5.3p) fixed # X53p

    pct_Tuition_be4_8 = inputVar['pct_Tuition_be4_8_set'][name] # X54
    X54p = price_Tuition_be4_8 = 1000000 # (5.4p) fixed # X54p

    pct_Tuition_be4_9 = inputVar['pct_Tuition_be4_9_set'][name] # X55
    X55p = price_Tuition_be4_9 = 500000 # (5.5p) fixed # X55p

    room_Rent = inputVar['room_Rent_set'][name] # X6

    no_Lecture = inputVar['no_Lecture_set'][name] # X7
    no_Coach = inputVar['no_Coach_set'][name] # X8
    wage_Lecture = inputVar['wage_Lecture_set'][name] # X9
    wage_Coach = inputVar['wage_Coach_set'][name] # X10

    X11 = Scholar	= 500000 # (11) fixed # X11
    pct_Scholar = inputVar['pct_Scholar_set'][name] # X12

    material_Exp = inputVar['material_Exp_set'][name] # X13

    pct_Cal = inputVar['pct_Cal_set'][name] # X14
    X15 = income_Cal	= 50000 # (15) fixed # X15

    X16 = RD_Exp	= 0.1 # (16) fixed # X16

    # scenarios = no_Class * no_Student * pct_Retake * Price * pct_Share * pct_Group_of_2 * pct_Current * pct_Tuition_be4_8 * pct_Tuition_be4_9 * room_Rent * no_Lecture *  no_Coach * wage_Lecture * wage_Coach * pct_Scholar * material_Exp * pct_Cal
    # print(name, ':\t',len(scenarios))
    scenarios = list(product(no_Class, no_Student, pct_Retake, Price, pct_Share, pct_Group_of_2, pct_Current, pct_Tuition_be4_8, pct_Tuition_be4_9, room_Rent, no_Lecture,  no_Coach, wage_Lecture, wage_Coach, pct_Scholar, material_Exp, pct_Cal))
    # print(type(scenarios))
    filename = name +'.csv'
    with open(filename, mode='w') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([
            'Gross Sales', 
            'Sales returns-allowances and discounts',
            'Retake', 
            'Discount', 
            'Net sales',
            'COGS', 
            'Gross margin', 
            'Operating Expense', 
            'R&D',
            'Labour', 
            'SG&A', 
            'Operating income', 
            'Other G/L', 
            'Calculator Income', 
            'Scholarship Expense', 
            'EBIT', 
            'Gross Margin', 
            'EBIT Margin'])
        for scen in scenarios:
            (X1, X2, X3, X4, X51, X52, X53, X54, X55, X6, X7, X8, X9, X10, X12, X13, X14) = scen
            # print(scen)
            # 2. Output variables:
            gross_Sales = X1 * X2 * X4 # (a) =	(1)	x	(2)	x	(4)

            retake = X1 * X2 * X3 * X4 # (b.1) =	(1)	x	(2)	x	(3)	x	(4)
            discount = X1 * X2 * (X51 * X51p + X52 * X52p + X53 * X53p + X54 * X54p + X55 * X55p)
            # (b.2) =	(1)	x	(2)	x	[(5.1)	x	(5.1p) + (5.2)	x	(5.2p) + (5.3)	x	(5.3p) + (5.4)	x	(5.4p) + (5.5)	x	(5.5p)]
            sale_reduce = retake + discount # (b) = (b.1) + (b.2)

            net_Sales = gross_Sales - sale_reduce # (c) = (a) - (b)

            COGS = X1 * X2 * X13 # (d) =	(1)	x	(2)	x	(13)

            gross_Margin = net_Sales - COGS # (e) = (c) - (d)

            RD = gross_Sales * RD_Exp # (f.1) =	(1)	x	(2)	x	(4)	x	(16)
            labour = X1 * (X7 * X9 + X8 * X10) # (f.2) =	(7)	x	(9)	+	(8)	x	(10)
            SGA = X1 * X6 * (X7 + X8) # (f.3) =	(7)	x	(6)	+	(8)	x	(6)
            operate_Exp = RD + labour + SGA # (f) = (f.1) + (f.2) + (f.3)

            operate_Income = gross_Margin - operate_Exp # (g) = (e) - (f)

            Cal_income = X1 * X2 * X14 * X15 # (h.1) =	(1)	x	(2)	x	(14)	x	(15)
            scholar_Exp = X1 * X2 * X12 * X11 # (h.2) =	(1)	x	(2)	x	(12)	x	(11)
            other_GL = Cal_income - scholar_Exp # (h) = (h.1) - (h.2)

            EBIT = operate_Income + other_GL # (i) = (g) + (h)

            pct_gross_Margin = gross_Margin/gross_Sales # (j) = (e)/(a)
            pct_EBIT_Margin = EBIT/gross_Sales# (k) = (i)/(a)
            
            data_writer.writerow([gross_Sales, sale_reduce, retake, discount, net_Sales, COGS, gross_Margin, operate_Exp, RD, labour, SGA, operate_Income, other_GL, Cal_income, scholar_Exp, EBIT, pct_gross_Margin, pct_EBIT_Margin])