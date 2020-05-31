from sys import stdin, stdout

t = int(stdin.readline())

answers = []

for test in range (t):
    n = int(stdin.readline())

    result = []

    blocks = []
    for i in range (n):
        s, e = (int(x) for x in stdin.readline().split())
        blocks.append([i,s,e])
    
    blocks.sort(key=lambda x: x[1])

    c = 0
    j = 0

    for i in range (n):
        s = blocks[i][1]
        e = blocks[i][2]

        if s >= c:
            c = e
            blocks[i].append('C')
        elif s >= j:
            j = e
            blocks[i].append('J')
        else:
            result = "IMPOSSIBLE"
            break
    
    if result != "IMPOSSIBLE":
        blocks.sort(key=lambda x: x[0])

        for i in range (n):
            result.append(blocks[i][3])
    
    answers.append("".join(result))

for i in range (t):
    stdout.write("Case #" + str(i + 1) + ": " + answers[i] + "\n") 