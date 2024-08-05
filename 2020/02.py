import sys
import re

lines = []
with open(sys.argv[1]) as f:
    lines = f.readlines()

# 10-12 j: jjjjjjjjjzjjdj
pattern = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"

part1 = 0
part2 = 0
for i in lines:
    match = re.search(pattern, i )
    low = int(match.group(1))
    high = int(match.group(2))
    char = match.group(3)
    string = match.group(4)
    count = string.count(char)

    # Part 1
    if count >= low and count <= high:
        part1 += 1
    
    # Part 2
    if (string[low-1] == char) ^ (string[high-1] == char):
        part2 += 1

print("part1:", part1)
print("part2:", part2)

