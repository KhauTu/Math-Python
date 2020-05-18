from VennDiagram import draw_venn
import csv
from sympy import FiniteSet

def read_csv(filename):
    football = []
    others = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == "1":
                football.append(row[0])
            if row[2] == "1":
                others.append(row[0])
    return football, others

f, o = read_csv('sports.csv')
f = FiniteSet(*f)
o = FiniteSet(*o)

draw_venn([f,o])