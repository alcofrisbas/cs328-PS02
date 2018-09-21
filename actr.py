"""
Ben Greene and Quinn Schiller

ACT-R Model for Homework 2

Anna Rafferty CS328 21 Sept. 2018

"""

from math import log
import pandas as pd


def baseline_activation(d, lags):
    s = 0
    for i in lags:
        if str(i) == "inf":
            continue
        else:
                s += (1.0/(i**d))
    #print(s)
    if s == 0:
        return -float("Inf")
    else:
        return log(s)
        #return log(sum([1.0/i**d for i in lags]))

def compute_all_baselines(fname):
    with open(fname) as r:
        raw = ([i.strip().split(",") for i in r.readlines()])
        lines = map(list, zip(*raw)) #transpose it so there is a row for each verb
    l = []
    for line in lines:
        lags = [float(i) for i in  line]
        l.append(baseline_activation(0.5, lags))
    return l

if __name__ == "__main__":
    l = compute_all_baselines("data/lags.txt")
    print(l)
