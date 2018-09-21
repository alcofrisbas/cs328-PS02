"""
Ben Greene and Quinn Schiller

ACT-R Model for Homework 2

Anna Rafferty CS328 21 Sept. 2018

"""

from math import log, exp
from numpy import dot, prod


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

def retrieval_time(activation,f,F):
    return [(F*exp(-f*a)) for a in activation]

def regular_utility():
    G = 5
    C = 1.2
    P = 1
    return P * G - C
    
def retrieval_utility(freqFile,lagFile):
    G = 5
    #compute activation
    with open(lagFile) as r:
        raw = ([i.strip().split(",") for i in r.readlines()]) #read and split the data into a 2d array
        lags = map(list, zip(*raw)) #transpose it so there is a row for each verb
        activation = []
    for line in lags:
        lag = [float(i) for i in  line] #turn each number into a float
        activation.append(baseline_activation(0.5, lag)) #make a list of activations and return it
    
    #get frequencies (second column of frequency text file)
    with open(freqFile) as r:
        freq = ([i.strip().split(",")[1] for i in r.readlines()])[1:] #ge the second column and skip the header
        freq = [float(f) for f in freq] #turn all numbers into floats
    
    rTimes = retrieval_time(activation,0.25,0.5)
    
    #compute P
    activated_words = [1.0 if word>0.3 else 0.0 for word in activation]
    P = dot(activated_words,freq)/sum(freq) #sum of frequency of activated words over total frequency
    
    #compute C
    filt_freq = []
    for i in range(len(rTimes)): #set freq for non-activated words to 0 
        filt_freq.append(freq[i]* activated_words[i]) 
    C = dot(rTimes,filt_freq)/sum(filt_freq) #weighted average not including non-retrieved words
    
    return P * G - C
    
    

if __name__ == "__main__":
    l = compute_all_baselines("data/lags.txt")
    print(l)
