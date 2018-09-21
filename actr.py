"""
Ben Greene and Quinn Schiller

ACT-R Model for Homework 2

Anna Rafferty CS328 21 Sept. 2018

"""

from math import log


def baseline_activation(d, lags):
    s = 0
    for i in lags:
        if str(i) == "inf": #ignore inf lags
            continue
        else:
                s += (1.0/(i**d))
    #print(s)
    if s == 0:
        return -float("Inf") #If there is no activation, avoid domain error of log(0) manually
    else:
        return log(s)
        #return log(sum([1.0/i**d for i in lags])) 

def compute_all_baselines(fname):
    with open(fname) as r:
        raw = ([i.strip().split(",") for i in r.readlines()]) #read and split the data into a 2d array
        lines = map(list, zip(*raw)) #transpose it so there is a row for each verb
    l = []
    for line in lines:
        lags = [float(i) for i in  line] #turn each number into a float
        l.append(baseline_activation(0.5, lags)) #make a list of activations and return it
    return l

if __name__ == "__main__":
    l = compute_all_baselines("data/lags.txt")
    print(l)
