"""
Ben Greene and Quinn Schiller

ACT-R Model for Homework 2

Anna Rafferty CS328 21 Sept. 2018

"""

from math import log


def baseline_activation(d, lags):
    s = 0
    for i in lags:
        if i == "Inf":
            continue
        else:
                s += 1.0/float(i)**d
    print(s)
    return log(s)
    #return log(sum([1.0/i**d for i in lags]))

def compute_all_baselines(fname):
    with open(fname) as r:
        lines = [i.strip() for i in r.readlines()]
    l = []
    for line in lines:
        l.append(baseline_activation(0.5, [float(i) for i in line.split(",")]))
    return l

if __name__ == "__main__":
    l = compute_all_baselines("data/lags.txt")
    print(l)
