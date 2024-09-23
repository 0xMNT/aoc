import sys

# Part 1 = 913

with open("05") as f:
    lines = f.readlines()
   
seats = []

for i in lines:
    i = i.replace("\n", "")
    row = int(i[:7].replace("F","0").replace("B","1"), 2)  
    col = int(i[-3:].replace("L","0").replace("R","1"), 2)  
    seatID = row * 8 + col
    seats.append(seatID)

# Part 1
print(max(seats))

# Part 2
allSeats = set(range(min(seats),max(seats)+1))
print(allSeats-set(seats))

