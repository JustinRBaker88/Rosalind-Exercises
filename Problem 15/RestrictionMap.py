from BioUtil.SortedList import SortedList

def partialDigest(L: SortedList):
    width = L.getLargestValue()
    X = SortedList.SortedList(0)
    #print("X: ", X)
    #print("L: ", L)
    L.remove(width)
    X.insert(width)
    place(L,X, width)
        
def place(L: SortedList, X: SortedList, width: int):
    if (L.size() is 0):
        print(X)
        return X

    #print("X: ", X)
    #print("L: ", L)
    y = L.getLargestValue()
    D0 = getD(y,X)
    D1 = getD(width - y, X)
    if isDInL(D0,L):
        X.insert(y)
        removeD(D0, L)
        place(L, X, width)
        X.remove(y)
        addDToL(D0, L)
    #else:
        #print("X: ", X)
        #print("Eliminating ", y)
        #print("D1: ", D1)    
    if isDInL(D1,L):
        X.insert(width - y)
        removeD(D1, L)
        place(L, X, width)
        X.remove(width - y)
        addDToL(D1, L)
    #else:
        #print("Eliminating ", width-y)  
    return

def getD(y: int, X: SortedList):
    D = SortedList.SortedList()
    for i in range(X.size()):
       D.insert(abs(y - X[i]))
        
    return D

def isDInL(D: SortedList, L: SortedList):
    for values in D:
        if (L.contains(values) is False):
            return False
    return True

def addDToL(D: SortedList, L: SortedList):
    for values in D:
        L.insert(values)
    

def removeD(D: SortedList, L: SortedList):
    for values in D:
        L.remove(values)

L = SortedList.SortedList([1,1,2,4,5,5,6,6,7,8,11,11,15,16,17,19,22,23,24,25,30])
partialDigest(L)