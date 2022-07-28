import sys, string

data = sys.stdin.read().split()

pointCnt = int()
histData = []

while data:
    histData.append((data[0], int(data[1])))
    pointCnt += int(data[1])
    data.pop(0)
    data.pop(0)

for word in histData:
    print(word[0] + '\t[' + '*' * round(100*word[1]/pointCnt/5) + '] ' + str(round(100*word[1]/pointCnt)) + '%')