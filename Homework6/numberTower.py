### CS 4310 - Homework 6 Number Tower
### By: Oscar Vanderhorst
### Well this was fun lol

F = open(input("Input file name: "), "r+")
F.readline()
floors = F.readlines()[::-1]
bestPath = list(map(int, floors[0].split()))
for line in floors[1::]:
	for index, node in enumerate(line.split()):
		bestPath[index] = int(node) + (bestPath[index] if bestPath[index] > bestPath[index+1] else bestPath[index+1])
print(bestPath[0])