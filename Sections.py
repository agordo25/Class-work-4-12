#write a function that finds and displays the smallest value in a list

section12A= [80, 75, 88, 80, 90, 77, 65]
section12B= [80, 75, 88, 80, 90, 77, 65]
section12C= [80, 75, 88, 80, 90, 77, 65]
section12D= [80, 75, 88, 80, 90, 77, 65]

def minMal(myList):
    print("Original values: ", myList)
    minMal=100
    for i in range(0,len(myList)):
        for myList[i] < minVal:
            minVal = myList[i]
    print("the smallest value in the list is", minVal)

findMinVal(section12A)
findMinVal(section12B)
findMinVal(section12C)
findMinVal(section12D)
