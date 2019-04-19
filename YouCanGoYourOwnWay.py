T = int(input())

N = []
P = []

for i in range (T):
    N.append(int(input()))
    P.append(str(input()))

for i in range (T):
    a = list(P[i])
    for j in range (len(a)):
        if (a[j] == "E"):
            a[j] = "S"
        elif(a[j] == "S"):
            a[j] = "E"
    
    print("Case #" + str(i + 1) + ":", "".join(a))