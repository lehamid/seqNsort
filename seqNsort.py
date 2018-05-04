#Lars-Eric Hamid - Project Grudat18



###################################
######### PACKAGE seqNsort ########
###################################



## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#########################################################################################
#########################################################################################
#### Definitions #### Definitions #### Definitions #### Definitions #### Definitions ####
#########################################################################################
#########################################################################################
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##



######################################################################
####### arithmetic sequence ############## arithmetic sequence #######
######################################################################

###################################
# def arithmetic(startValue,commonDiff,totElements):
# Input:
#       startValue = Startvärde (heltal) för den aritmetiska talserien.
#       commonDiff = "common difference" (heltal) för talserien.
#       totElements = Antalet element vi vill ha i talserien (icke-negativt heltal).
# Output:
#       En lista med en aritmetisk talföljd enligt de givna parameterna ovan.
###################################

def arithmetic(startValue,commonDiff,totElements):
    """Builds an arithmetic sequence from the given parameters"""
    if isinstance(startValue, int) == False or isinstance(commonDiff, int) == False or isinstance(totElements, int) == False:
        return "Wrong input"
    elif totElements < 0:
        return "Wrong input"

    elif totElements == 0:
        return []
    elif totElements == 1:
        return [startValue]

    else:
        myList = []
        myList.append(startValue)
        assert myList == [startValue]       #test

        counter = 1
        while counter < totElements:
            # Lägger till ett element i taget
            startValue = startValue + commonDiff
            myList.append(startValue)
            assert myList[counter] == startValue        #test
            counter = counter + 1

        return myList


######################################################################
####### geometric sequence ############### geometric sequence ########
######################################################################

###################################
# def geometric(startValue,commonRatio,totElements):
# Input:
#       startValue = Startvärde (heltal) för den geometriska talserien.
#       commonRatio = "common ratio" (heltal) för talserien.
#       totElements = Antalet element vi vill ha i talserien (icke-negativt heltal).
# Output:
#       En lista med en geometrisk talföljd enligt parameterna ovan.
###################################

def geometric(startValue,commonRatio,totElements):
    """Builds a geometric sequence from the given parameters"""
    if isinstance(startValue, int) == False or isinstance(commonRatio, int) == False or isinstance(totElements, int) == False:
        return "Wrong input"
    elif totElements < 0:
        return "Wrong input"

    elif totElements == 0:
        return []
    elif totElements == 1:
        return [startValue]

    else:
        myList = []
        myList.append(startValue)
        assert myList == [startValue]       #Test

        counter = 1
        while counter < totElements:
            # Lägger till ett element i taget
            startValue = startValue * commonRatio
            myList.append(startValue)
            assert myList[counter] == startValue        #test
            counter = counter + 1

        return myList


######################################################################
####### square/cube sequence ########### square/cube sequence ########
######################################################################

###################################
# def squareNcube(squareORcube,startValue,totElements):
# Input:
#       squareORcube = "square" or "cube" (vilken talföljd efterfrågas?
#                       kvadratisk: skriv <"square">, kubisk: skriv <"cube">)
#       startValue = Startvärde (kvadrattal eller kubtal beroende på valet i
#                    squareORcube) för den kvadratiska eller kubiska talserien.
#       totElements = Antalet element vi vill ha i den efterfrågade
#                     talserien (icke-negativt heltal).
# Output:
#       En lista med en kvadratisk/kubisk talföljd enligt parameterna ovan.
###################################

def _checkSqrtSnC(valueToCheck):
    """Check if valueToCheck (input) is a perfect square value. Returns True if perfect square value and False otherwise."""
    return int(round(valueToCheck ** (1. / 2))) ** 2 == valueToCheck

def _checkCubeSnC(valueToCheck):
    """Check if valueToCheck (input) is a perfect cube value. Returns True if perfect cube value and False otherwise."""
    return int(round(valueToCheck ** (1. / 3))) ** 3 == valueToCheck

def squareNcube(squareORcube,startValue,totElements):
    """Builds a square or cube sequence from the given parameters."""
    if isinstance(startValue, int) == False or isinstance(totElements, int) == False:
        return "Wrong input"
    elif startValue < 0:
        return "Wrong input"
    elif totElements < 0:
        return "Wrong input"

    elif squareORcube == "square":
        if _checkSqrtSnC(startValue) == False:
            return "Wrong input"
    elif squareORcube == "cube":
        if _checkCubeSnC(startValue) == False:
            return "Wrong input"

    if totElements == 0:
        return []
    elif totElements == 1:
        return [startValue]

    else:
        myList = []
        myList.append(startValue)
        assert myList == [startValue]       #Test

        counter = 1
        while counter < totElements:
            # Lägger till ett element i taget
            if squareORcube == "square":
                value = (int(round((startValue)**(1/2))) + counter)**2
                myList.append(value)
                counter = counter + 1
            elif squareORcube == "cube":
                value = int(round((startValue)**(1/3)) + counter)**3
                myList.append(value)
                counter = counter + 1

        return myList


######################################################################
####### triangular sequence ############## triangular sequence #######
######################################################################

###################################
# def triangular(startValue,totElements):
# Input:
#       startValue = Startvärde (triangeltal, ex 0,1,3,6,10,15,21,...) för den triangulära talserien.
#       totElements = Antalet element vi vill ha i talserien (icke-negativt heltal).
# Output:
#       En lista med en triangulär talföljd enligt parameterna ovan.
###################################

def _triValCheck(valueToCheck):
    """Check if valueToCheck (input) is a triangular value. Returns True if triangular value and False otherwise."""
    outVal = round(-(1/2) + ((1/4)+2*valueToCheck)**(1/2))
    if (outVal*(outVal+1))/2 == valueToCheck:
        return [True,outVal]
    else:
        return [False,None]


def triangular(startValue,totElements):
    """Builds a triangular sequence from the given parameters."""
    if isinstance(startValue, int) == False or isinstance(totElements, int) == False:
        return "Wrong input"
    elif startValue < 0:
        return "Wrong input"
    elif totElements < 0:
        return "Wrong input"
    elif _triValCheck(startValue)[0] == False:
        return "Wrong input"

    if totElements == 0:
        return []
    elif totElements == 1:
        return [startValue]
    elif _triValCheck(startValue) != False:
        myList = []

        counter = _triValCheck(startValue)[1]
        counterEnd = totElements + counter
        while counter < counterEnd:
            # Lägger till ett element i taget
            startValue = round((counter*(counter + 1)/2))
            myList.append(startValue)
            counter = counter + 1

        return myList


######################################################################
####### fibonacci sequence ############### fibonacci sequence ########
######################################################################

###################################
# def fibonacci(n,totElements):
# Input:
#       n = StartIndexet för det allra första fibonacci värdet i talföljden
#           (ex. _fibValue(3) = 2, _fibValue(6) = 8)
#       totElements = Antalet element vi vill ha i talserien (icke-negativt heltal).
# Output:
#       En lista med en fibonacci-talföljd enligt parameterna ovan.
###################################

def _fibValue(n):
    """Find the fibonacci value with index n. Input: index n. Output: the n:th fibonacci value."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fibValue(n-1) + _fibValue(n-2)      # En rekursiv relation för att finna

def fibonacci(n,totElements):
    """Builds a fibonacci sequence from the given parameters."""
    if isinstance(n, int) == False or isinstance(totElements, int) == False:
        return "Wrong input"
    elif n < 0:
        return "Wrong input"
    elif totElements < 0:
        return "Wrong input"

    if totElements == 0:
        return []
    else:
        myList = []
        counter = 1
        while counter < totElements + 1:
            # Lägger till ett element i taget
            myList.append(_fibValue(n))
            counter = counter + 1
            n = n + 1

        return myList


######################################################################
########### merge sort ####################### merge sort ############
######################################################################

###################################
# def mergeSort(myList):
# Input:
#       inList = En lista med reella element som skall sorteras.
# Output:
#       Returnerar sorterad inList.
###################################

def mergeSort(myList):
    """Sorting the elements in myList in order. Timecomplexity: O(n*log n).
    input: list. output: sorted list."""
    if len(myList) == None or len(myList) == 0:
        return []

    elif len(myList) != 1:
        mid = int(len(myList)/2)
        myList_halfA = mergeSort(myList[0:mid])
        myList_halfB = mergeSort(myList[mid:])

        doneList = []
        while len(myList_halfA)>0 and len(myList_halfB)>0:
            # sorting elements by the merge sort tecnique.
            if myList_halfA[0] > myList_halfB[0]:
                doneList.append(myList_halfB[0])
                myList_halfB.pop(0)
            else:
                doneList.append(myList_halfA[0])
                myList_halfA.pop(0)

        doneList = doneList + myList_halfA
        doneList = doneList + myList_halfB

        return doneList

    else:
        return myList


######################################################################
########### find sequence ################ find sequence #############
######################################################################

###################################
# def findSeq(inList):
# Input:
#       inList = en lista med element som skall sorteras.
# Output:
#       Returnerar en eventuelt en passande talföljd till elementen i inList
###################################

def _checkArithmetic(inList,listLen):
    """Checks if inList is an arithmetic sequence."""
    boolList = []
    for i in range(0,listLen-2):
        # checks the first difference with the second, then the second with the third so on.
        if inList[i+1] - inList[i] == inList[i+2] - inList[i+1]:
            boolList.append(True)
            # if first and second difference is same --> append True to boolList, otherwise append Fasle. Same for second and third, third and fourth so on.
        else:
            boolList.append(False)

    for i in boolList:
        # if all elements in boolList is True --> arithmetic sequence.
        if i == False:
            return False        # Inte arithmetic
    return True         # arithmetic talföljd

def _checkGeometric(inList,listLen):
    """Checks if inList is a geometric sequence."""
    boolList = []
    for i in range(0,listLen-2):
        # checks the first fraction with the second, then the second with the third so on.
        if inList[i] / inList[i+1] == inList[i+1] / inList[i+2]:
            # if first and second fraction is same --> append True to boolList, otherwise append Fasle. Same for second and third, third and fourth so on.
            boolList.append(True)
        else:
            boolList.append(False)

    for i in boolList:
        # if all elements in boolList is True --> geometric sequence.
        if i == False:
            return False        # Inte Geometric
    return True         # Geometric talföljd

def _checkFibonacci(inList,listLen):
    """Checks if inList is a fibonacci sequence."""
    boolList = []
    for i in range(0,listLen-2):
        # checks the values in inList with the definition for Fibonacci values. Def: FibValue(n-2) + FibValue(n-1) = FibValue(n).
        if inList[i] + inList[i+1] == inList[i+2]:
            # if element one and two equals element three --> return True, otherwise False. Same for element two and three --> equals element four, so on.
            boolList.append(True)
        else:
            boolList.append(False)

    for i in boolList:
        # if all elements in boolList is True --> fibonacci sequence.
        if i == False:
            return False        # Inte Fibonacci
    return True         # Fibonacci talföljd

def _checkTriangular(inList,listLen):
    """Checks if inList is a triangular sequence."""
    if triangular(inList[0],listLen) == inList:
        # checks all the elements in inList by comparing with the values from triangular().
        return True
    else:
        return False

def _checkSquare(inList,listLen):
    """Checks if inList is a square sequence."""
    if squareNcube("square",inList[0],listLen) == inList:
        # checks all the elements in inList by comparing with the values from squareNcube("square",...).
        return True
    else:
        return False

def _checkCube(inList,listLen):
    """Checks if inList is a cube sequence."""
    if squareNcube("cube",inList[0],listLen) == inList:
        # checks all the elements in inList by comparing with the values from squareNcube("cube",...).
        return True
    else:
        return False

def checkIfSorted(inList):
    """Checks if inList is sorted. Input: input, listLen.
    Output: True if sorted, False otherwise."""
    listLen = len(inList)
    for i in range(0,listLen-1):
        # comparing the actual value with the value before for inList.
        if inList[i] > inList[i+1]:
            return False
    return True


def findSeq(inList):
    """Finds the greneral sequence for the inList. if not found return "not a
    general sequence". If list not sorted --> sort first by merge sort."""
    listLen = len(inList)
    if listLen <= 2:
        return "not a general sequence"
    else:
        if checkIfSorted(inList) != True:
            # List not sorted.
            sorted_inList = mergeSort(inList)
        else:
            # List is already sorted.
            sorted_inList = inList

        # inList is now sorted and saved under sorted_inList. Now, try to find a matching sequence.
        if _checkArithmetic(sorted_inList,listLen) == True:
            # check if sorted_inList is an arithmetic sequence.
            return "arithmetic sequence"
        elif _checkGeometric(sorted_inList,listLen) == True:
            # check if sorted_inList is a geometric sequence.
            return "geometric sequence"
        elif _checkFibonacci(sorted_inList,listLen) == True:
            # check if sorted_inList is a fibonacci sequence.
            return "fibonacci sequence"
        elif _checkTriangular(sorted_inList,listLen) == True:
            # check if sorted_inList is a triangular sequence.
            return "triangular sequence"
        elif _checkSquare(sorted_inList,listLen) == True:
            # check if sorted_inList is a square sequence.
            return "square sequence"
        elif _checkCube(sorted_inList,listLen) == True:
            # check if sorted_inList is a cube sequence.
            return "cube sequence"
        else:
            # if not any of the sequence matches.
            return "not a general sequence"



## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
###################################################################################
###################################################################################
#### Asserts #### Asserts #### Asserts #### Asserts #### Asserts #### Asserts #####
###################################################################################
###################################################################################
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##



def mainAssertArithmetic():
    # part 1:
    assert arithmetic(0,0,0) == []
    assert arithmetic(0,-2,0) == []
    assert arithmetic(0,4,1) == [0]
    assert arithmetic(0,0,3) == [0,0,0]
    assert arithmetic(0,1,2) == [0,1]
    assert arithmetic(1,4,3) == [1,5,9]
    assert arithmetic(-44,12,6) == [-44, -32, -20, -8, 4, 16]
    assert arithmetic(42,-1,12) == [42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]
    # part 2:
    assert arithmetic(0,4,-3) == "Wrong input"
    assert arithmetic("str",4,33) == "Wrong input"
    assert arithmetic(8,"str",9) == "Wrong input"
    assert arithmetic(-2,4,"str") == "Wrong input"
    #print("All asserts OK!")
mainAssertArithmetic()


def mainAssertGeometric():
    # part 1:
    assert geometric(0,0,0) == []
    assert geometric(0,-2,0) == []
    assert geometric(0,4,1) == [0]
    assert geometric(0,4,3) == [0,0,0]
    assert geometric(0,0,5) == [0,0,0,0,0]
    assert geometric(5,1,2) == [5,5]
    assert geometric(1,4,3) == [1,4,16]
    assert geometric(-4,2,6) == [-4, -8, -16, -32, -64, -128]
    assert geometric(-4,-2,6) == [-4, 8, -16, 32, -64, 128]
    assert geometric(1,10,8) == [1,10, 100, 1000, 10000, 100000, 1000000, 10000000]
    assert geometric(2,5,10) == [2, 10, 50, 250, 1250, 6250, 31250, 156250, 781250, 3906250]
    # part 2:
    assert geometric(5,4,-3) == "Wrong input"
    assert geometric("8",3,5) == "Wrong input"
    assert geometric(80,"2",9) == "Wrong input"
    assert geometric(-24,8,"44") == "Wrong input"
    #print("All asserts OK!")
mainAssertGeometric()


def mainAssertSqureNCube():
    #squre:
    assert squareNcube("square",0,0) == []
    assert squareNcube("square",16,0) == []
    assert squareNcube("square",9,1) == [9]
    assert squareNcube("square",10,1) == "Wrong input"
    assert squareNcube("square",-2,3) == "Wrong input"
    assert squareNcube("square",3,4) == "Wrong input"
    assert squareNcube("square",9,-2) == "Wrong input"
    assert squareNcube("square",-4,-4) == "Wrong input"
    assert squareNcube("square",23,0) == "Wrong input"
    assert squareNcube("square",48,2) == "Wrong input"
    assert squareNcube("square",1,3) == [1,4,9]
    assert squareNcube("square",0,6) == [0,1,4,9,16,25]
    assert squareNcube("square",16,4) == [16, 25, 36, 49]
    assert squareNcube("square",1,8) == [1,4,9,16,25,36,49,64]
    assert squareNcube("square",2704,5) == [2704, 2809, 2916, 3025, 3136]
    assert squareNcube("square",49,18) == [49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576]
    #cube:
    assert squareNcube("cube",0,0) == []
    assert squareNcube("cube",27,0) == []
    assert squareNcube("cube",64,1) == [64]
    assert squareNcube("cube",10,1) == "Wrong input"
    assert squareNcube("cube",-2,3) == "Wrong input"
    assert squareNcube("cube",3,4) == "Wrong input"
    assert squareNcube("cube",9,-2) == "Wrong input"
    assert squareNcube("cube",-4,-4) == "Wrong input"
    assert squareNcube("cube",23,0) == "Wrong input"
    assert squareNcube("cube",48,2) == "Wrong input"
    assert squareNcube("cube",1,3) == [1,8,27]
    assert squareNcube("cube",0,6) == [0, 1, 8, 27, 64, 125]
    assert squareNcube("cube",8,4) == [8, 27, 64, 125]
    assert squareNcube("cube",1,8) == [1, 8, 27, 64, 125, 216, 343, 512]
    assert squareNcube("cube",140608,5) == [140608, 148877, 157464, 166375, 175616]
    assert squareNcube("cube",27,14) == [27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096]
    #print("All asserts OK!")
mainAssertSqureNCube()


def mainAssertTriangular():
    #part 1:
    assert triangular("str",3) == "Wrong input"
    assert triangular("str",-13) == "Wrong input"
    assert triangular(6,"str") == "Wrong input"
    assert triangular(-2,"str") == "Wrong input"
    #part 2:
    assert triangular(4,3) == "Wrong input"
    assert triangular(-44,6) == "Wrong input"
    assert triangular(3,-2) == "Wrong input"
    #part 3:
    assert triangular(0,0) == []
    assert triangular(0,1) == [0]
    assert triangular(0,2) == [0,1]
    assert triangular(1,5) == [1,3,6,10,15]
    assert triangular(595,3) == [595,630,666]
    assert triangular(15,12) == [15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136]
    #print("All asserts OK!")
mainAssertTriangular()


def mainAssertFibonacci():
    # part 1:
    assert fibonacci("str",3) == "Wrong input"
    assert fibonacci("str",-13) == "Wrong input"
    assert fibonacci(6,"str") == "Wrong input"
    assert fibonacci(-2,"str") == "Wrong input"
    assert fibonacci(-44,6) == "Wrong input"
    assert fibonacci(3,-2) == "Wrong input"
    # part 2:
    assert fibonacci(0,0) == []
    assert fibonacci(0,1) == [0]
    assert fibonacci(0,2) == [0,1]
    assert fibonacci(0,3) == [0,1,1]
    assert fibonacci(1,5) == [1,1,2,3,5]
    assert fibonacci(6,8) == [8,13,21,34,55,89,144,233]
    assert fibonacci(0,20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    #print("All asserts OK!")
mainAssertFibonacci()


def mainAssertCheckIfSort():
    assert checkIfSorted([]) == True
    assert checkIfSorted([3]) == True
    assert checkIfSorted([1,2,3]) == True
    assert checkIfSorted([2,1,3]) == False
    assert checkIfSorted([2,3,7,34,4564,3435435,456463656]) == True
    assert checkIfSorted([1,21,32,34,33,1000,2323232]) == False
    #print("All asserts OK!")
mainAssertCheckIfSort()


def mainAssertMergeSort():
    # part 1:
    vec1 = []
    vec2 = [1]
    vec3 = [-3]
    vec4 = [3,1,2]
    vec5 = [7,7,2,6,7,2,1,-2,-2,-10,5.005]
    vec6 = [987654321,-100,0,1,-1,0,0,-1,-789789,-100000000,1000000000000000,-22]
    # part 2:
    assert mergeSort(vec1) == []
    assert mergeSort(vec2) == [1]
    assert mergeSort(vec3) == [-3]
    assert mergeSort(vec4) == [1,2,3]
    assert mergeSort(vec5) == [-10,-2,-2,1,2,2,5.005,6,7,7,7]
    assert mergeSort(vec6) == [-100000000,-789789,-100,-22,-1,-1,0,0,0,1,987654321,1000000000000000]
    #print("All asserts OK!")
mainAssertMergeSort()


def mainAssertFindSeq():
    # arithmetic part 1:
    myList1a = []
    myList2a = [1]
    myList3a = [2,3]
    myList4a = [1,2,3,4,5]
    myList5a = [-2,-1,0,1,2,3,5,4]
    myList6a = [11,12,13,14,15]
    myList7a = [1,2,4,5,6]
    # arithmetic part 2:
    assert findSeq(myList1a) == "not a general sequence"
    assert findSeq(myList2a) == "not a general sequence"
    assert findSeq(myList3a) == "not a general sequence"
    assert findSeq(myList4a) == "arithmetic sequence"
    assert findSeq(myList5a) == "arithmetic sequence"
    assert findSeq(myList6a) == "arithmetic sequence"
    assert findSeq(myList7a) == "not a general sequence"
    # geometric part 1:
    myList1g = []
    myList2g = [1]
    myList3g = [3,9]
    myList4g = [1,3,9,27,81]
    myList5g = [-2,-4,-8,-16,-32]
    myList6g = [1,10,100,1000,10000]
    myList7g = [-1,-2,-4,-5,-8]
    # geometric part 2:
    assert findSeq(myList1g) == "not a general sequence"
    assert findSeq(myList2g) == "not a general sequence"
    assert findSeq(myList3g) == "not a general sequence"
    assert findSeq(myList4g) == "geometric sequence"
    assert findSeq(myList5g) == "geometric sequence"
    assert findSeq(myList6g) == "geometric sequence"
    assert findSeq(myList7g) == "not a general sequence"
    # fibonacci part 1:
    myList1f = []
    myList2f = [1]
    myList3f = [5,8]
    myList4f = [0,1,1,2,3,5,8]
    myList5f = [1,2,3,5,8,13,21,34]
    myList6f = [34,55,89,144,233,377,610,987,1597,2584,4181,6765]
    myList7f = [0,1,1,2,3,8,13,21]
    myList8f = [-1,-2,-4,-5,-8]
    # fibonacci part 2:
    assert findSeq(myList1f) == "not a general sequence"
    assert findSeq(myList2f) == "not a general sequence"
    assert findSeq(myList3f) == "not a general sequence"
    assert findSeq(myList4f) == "fibonacci sequence"
    assert findSeq(myList5f) == "fibonacci sequence"
    assert findSeq(myList6f) == "fibonacci sequence"
    assert findSeq(myList7f) == "not a general sequence"
    assert findSeq(myList8f) == "not a general sequence"
    # triangular part 1:
    myList1t = []
    myList2t = [10]
    myList3t = [1,3]
    myList4t = [0,1,3,6,10,15,21]
    myList5t = [6,10,15]
    myList6t = [1,3,6,10,15,21,28,36,45,55,66]
    myList7t = [3,6,10,21,28,36]
    myList8t = [0,3,6,10,15]
    # triangular part 2:
    assert findSeq(myList1t) == "not a general sequence"
    assert findSeq(myList2t) == "not a general sequence"
    assert findSeq(myList3t) == "not a general sequence"
    assert findSeq(myList4t) == "triangular sequence"
    assert findSeq(myList5t) == "triangular sequence"
    assert findSeq(myList6t) == "triangular sequence"
    assert findSeq(myList7t) == "not a general sequence"
    assert findSeq(myList8t) == "not a general sequence"
    # square part 1:
    myList1s = []
    myList2s = [6]
    myList3s = [6,10]
    myList4s = [1,4,9]
    myList5s = [16, 25, 36, 49]
    myList6s = [1,4,9,16,25,36,49,64,81]
    myList7s = [4,9,16,25,49,64]
    myList8s = [-4,1,4,9,16]
    # square part 2:
    assert findSeq(myList1s) == "not a general sequence"
    assert findSeq(myList2s) == "not a general sequence"
    assert findSeq(myList3s) == "not a general sequence"
    assert findSeq(myList4s) == "square sequence"
    assert findSeq(myList5s) == "square sequence"
    assert findSeq(myList6s) == "square sequence"
    assert findSeq(myList7s) == "not a general sequence"
    assert findSeq(myList8s) == "not a general sequence"
    # cube part 1:
    myList1c = []
    myList2c = [1]
    myList3c = [1,8]
    myList4c = [1,8,27]
    myList5c = [216,343,512]
    myList6c = [1, 8, 27, 64, 125, 216, 343, 512]
    myList7c = [1, 8, 27, 64, 216, 343, 512]
    myList8c = [1,8,8,27]
    # cube part 2:
    assert findSeq(myList1c) == "not a general sequence"
    assert findSeq(myList2c) == "not a general sequence"
    assert findSeq(myList3c) == "not a general sequence"
    assert findSeq(myList4c) == "cube sequence"
    assert findSeq(myList5c) == "cube sequence"
    assert findSeq(myList6c) == "cube sequence"
    assert findSeq(myList7c) == "not a general sequence"
    assert findSeq(myList8c) == "not a general sequence"
    #print("All asserts OK!")
mainAssertFindSeq()


###########################################################################
####################### TRY THE PACKAGE DOWN BELOW! #######################
###########################################################################

def main():
    """Try the package here!"""
    print(findSeq([3,2,1]))

main()
