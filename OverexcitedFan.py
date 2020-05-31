
t = int(input())

for test in range(1, t + 1):
    x, y, m = input().split()
    x = int(x)
    y = int(y)
    m = list(m)

    answer = 0
    position = [x, y]
    for i in range (len(m)):
        if m[i] == 'N':
            position[1] += 1
        elif m[i] == 'S':
            position[1] -= 1
        elif m[i] == 'E':
            position[0] += 1
        else:
            position[0] -= 1
        
        steps = abs(position[0]) + abs(position[1])
        if steps <= i + 1:
            answer = i + 1
            break
        if (i == len(m) - 1) and answer == 0:
            answer = "IMPOSSIBLE"

    print("Case #%d: %s" %(test, answer))