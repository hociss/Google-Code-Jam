from sys import stdin, stdout

t = int(stdin.readline())
answers = []

for test in range(t):
    s = list(stdin.readline())

    s2 = []
    for i in range (len(s) - 1):
        # (
        if i == 0:
            for j in range (int(s[i])):
                s2.append("(")
        elif int(s[i]) > int(s[i-1]):
            for j in range(int(s[i]) - int(s[i-1])):
                s2.append("(")
        
        # the number
        s2.append(s[i])

        # )
        if i == len(s) - 2:
            for j in range (int(s[i])):
                s2.append(")")
        elif int(s[i]) > int(s[i + 1]):
            for j in range (int(s[i]) - int(s[i + 1])):
                s2.append(")")
        
    answers.append("".join(s2))

for i in range (t):
    stdout.write("Case #" + str(i + 1) + ": " + answers[i] + "\n")
                
