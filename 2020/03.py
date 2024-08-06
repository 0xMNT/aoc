import sys

# 3 right 1 down
# 7 Trees found in 03.txt


f = open(sys.argv[1])
lines = [line.replace("\n", "") for line in f]
f.close()

right = [1,3,5,7,1]
down = [1,1,1,1,2]
full = 1


for i in range(len(right)):
    counter = 0
    r = right[i]
    d = down[i]
    pos_x = 0

    for pos_y in range(0, len(lines), d):
        if lines[pos_y][pos_x] == "#":
            counter += 1
        pos_x = (pos_x + r) % len(lines[0])
    full *= counter
    print(counter)


print(full)













