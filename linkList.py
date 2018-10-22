class node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def nodeAppend(self,inpVal):
        #print "I am here"
        temp = self.next
        lastNode = self
        while temp != None:
            lastNode = temp
            temp = temp.next
        lastNode.next = node(inpVal)
        return self

def fetchIndx(n,idx):
    temp = n
    tempArr = []
    while temp != None:
        lnArr = len(tempArr)
        if lnArr == idx:
            tempArr.pop(0)
            tempArr.append(temp.val)
        else:
            tempArr.append(temp.val)
        temp = temp.next
    lnArr = len(tempArr)
    if lnArr < idx:
        retVal = None
    else:
        retVal = tempArr[0]
    return retVal

def printLL(n):
    temp = n
    while temp != None:
        print(temp.val)
        temp = temp.next

h = node(1)
h = h.nodeAppend(2)
h = h.nodeAppend(3)
h = h.nodeAppend(4)
h = h.nodeAppend(5)
h = h.nodeAppend(6)

#printLL(h)

print(fetchIndx(h,7))
print(fetchIndx(h,6))
print(fetchIndx(h,1))
print(fetchIndx(h,3))
