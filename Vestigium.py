from sys import stdin, stdout

def countRepeating (n, theLine):
    counter = [0 for i in range (n + 1)]
    for i in range(n):
        counter[theLine[i]] += 1
        if counter[theLine[i]] > 1:
            return 1
    
    return 0



t = int(input())

for i in range (1, t + 1):
    n = int(input())
    matrix = []

    repeatingRow = 0
    repeatingCol = 0

    for j in range (n):
        m = [int(x) for x in input().split()]
        repeatingRow += countRepeating(n, m)

        matrix.append(m)

    trace = 0
    for j in range (n):
        trace += matrix[j][j]

        theCol = []
        for k in range (n):
            theCol.append(matrix[k][j])
        repeatingCol += countRepeating(n,theCol)
        
    print("Case #%d: %s" %(i, (str(trace) + " " + str(repeatingRow) + " " + str(repeatingCol))))