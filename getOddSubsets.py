# written by clopez

import sys
import itertools

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

number  = 0

if len(sys.argv) > 1:
    number = int(sys.argv[1])

if not number:
    print "Please enter a number bigget than 3"

elif number < 4:
    print "The input should be a number bigger than 3"

else:

    theSetOfNumbers = getSetOfNumbers(number)
    oddSizeListForSets = getOddCardinalityList(number)

    listOfSubsets = []

    for size in oddSizeListForSets:
        listOfSubsets.append( findSubsets(theSetOfNumbers,size) )
    
    j = 0


    f = open('oddSubSetsWithFormat.txt','w')
    fn = open('oddSubSets.txt','w')

    for localSet in listOfSubsets:
        for i in localSet:
            j += 1
            setOnString = " ".join(map(str,i))
            setForInput = "set Sub[%d] := %s;" % (j,setOnString)
            fn.write(setOnString+"\n")
            f.write(setForInput+"\n")

    f.close()
    fn.close()




