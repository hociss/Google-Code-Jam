t = int(input())
outputX = [0] * t 
outputY = [0] * t     

for j in range(t):
    p, q = input().split()
    p = int(p)
    q = int(q)

    x = [0] * p
    y = [0] * p
    d = ["N"] * p 

    countX = [0] * (q + 1)
    countY = [0] * (q + 1)

    for i in range(p):
        x[i], y[i], d[i] = input().split()
        x[i] = int(x[i])
        y[i] = int(y[i])
    
        if (d[i] == "N"):
            for k in range (y[i] + 1, q + 1):
                countY[k] += 1
               
        if (d[i] == "S"):
            for k in range (y[i]):
                countY[k] += 1
            
        if (d[i] == "W"):
            for k in range (x[i]):
                countX[k] += 1
        
        if (d[i] == "E"):
            for k in range (x[i] + 1, q + 1):
                countX[k] += 1
        

        # print ("Count X =     ", countX)
        # print ("Count Y =     ", countY)


    
    outputX[j] = countX.index(max(countX))
    outputY[j] = countY.index(max(countY))

    # maxX = 0
    # maxY = 0
    # for i in range (q + 1):
    #     if (countX[i] > maxX):
    #         outputX[j] = i
    #         maxX = countX[i]
    #     if (countY[i] > maxY):
    #         outputY[j] = i
    #         maxY = countY[i]

    # print ("OutputX =    ", outputX)
    # print ("OutputY =    ", outputY)
    #     print ("maxX =      ", maxX)
    #     print ("maxY =      ", maxY)
        # print (output, j)

for j in range (t):
    print ("Case #" + str(j + 1) + ":", outputX[j], outputY[j])