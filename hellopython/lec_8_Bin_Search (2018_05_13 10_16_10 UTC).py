def search(L, e):
    for elem in L:
        if elem == e:
            return True
        if elem > e:
            return False
    return False
def bSearch(L, e, low, high):
    global numCalls
    numCalls += 1
    if high - low < 2:
         return L[low] == e or L[high] == e
    mid = low + int((high - low)/2)
    if L[mid] == e:
         return True
    if L[mid] > e:
         return bSearch(L, e, low, mid - 1)
    else:
        return bSearch(L, e, mid + 1, high)

def search(L, e):
    return bSearch(L, e, 0, len(L) - 1)
L = range(100)
numCalls = 0
print search(L, 3)
print numCalls