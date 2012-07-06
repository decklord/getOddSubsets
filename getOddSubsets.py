# written by clopez

import sys
import itertools
import time

def findSubsets(S,m):
    return set(itertools.combinations(S, m))

def getSetOfNumbers(number):

    allList = range(number+1)
    return allList[1:]

def getOddCardinalityList(number):

    allNumbers = range(number)[3:]
    oddList = []
    for i in allNumbers:
        if i%2 > 0:
            oddList.append(i)

    return oddList

import numpy as np

def binnings(n, k, cache={}):
    if n == 0:
        return np.zeros((1, k))
    if k == 0:
        return np.empty((0, 0))
    args = (n, k)
    if args in cache:
        return cache[args]
    a = binnings(n - 1, k, cache)
    a1 = a + (np.arange(k) == 0)
    b = binnings(n, k - 1, cache)
    b1 = np.hstack((np.zeros((b.shape[0], 1)), b))
    result = np.vstack((a1, b1))
    cache[args] = result
    return result

#if __name__ == '__main__':
#    import timeit
#    print timeit.timeit('binnings(20, 5, {})', setup='from __main__ import binnings', number=1)

number  = 0
setSize = 0

if len(sys.argv) > 1:
    number = int(sys.argv[1])
if len(sys.argv) > 2:
    setSize = int(sys.argv[2])

if not number:
    print "Please enter a number bigger than 3 and optionally the size of the set"

elif number < 4:
    print "The input should be a number bigger than 3"

else:

    start_time = time.time()
    theSetOfNumbers = getSetOfNumbers(number)
    if setSize:
        oddSizeListForSets = [setSize]#getOddCardinalityList(number)
    else:
        oddSizeListForSets = getOddCardinalityList(number)

    print "-> Get Base Data"
    listOfSubsets = []

    j = 0
    f = open('oddSubSetsWithFormat.txt','w')
    fn = open('oddSubSets.txt','w')

    for size in oddSizeListForSets:
        localSet = findSubsets(theSetOfNumbers,size)
        for i in localSet:
            j += 1
            setOnString = " ".join(map(str,i))
            setForInput = "set Sub[%d] := %s;" % (j,setOnString)
            fn.write(setOnString+"\n")
            f.write(setForInput+"\n")
    
    f.close()
    fn.close()

    elapsed_time = time.time() - start_time
    print elapsed_time




