import sys

x = []
with open(sys.argv[1]) as f:
    x = list(map(int,f.readlines()))
n = len(x)

for i in range(n):
    for j in range(i+1, n):
        if x[i]+x[j] == 2020:
            print("part1: ", x[i]*x[j])
        for k in range(j+1, n):
            if x[i]+x[j]+x[k] == 2020:
                print("part2: ", x[i]*x[j]*x[k])
