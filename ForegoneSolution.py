T = int(input())
N = []

for i in range (T):
    N.append(int(input()))



for i in range (T):
    a = list(str(N[i]))
    b = list(str(N[i]))
    for j in range (len(a)):
        if (a[j] == "4"):
            a[j] = "3"
            b[j] = "1"
        else:
            b[j] = "0"

    k = 0
    while (b[k] == "0"):
        b[k] = ""
    
    print ("Case #" + str(i+1) + ":", "".join(a), "".join(b))
