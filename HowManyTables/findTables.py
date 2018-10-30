def findTables(Lines):
	#Instantiate array of number of people
	#O(n) where n = amount of people
	arrayOfPeople = [None] * Lines[0]

	#For each of the upcoming statements...
	#O(L), where L = the amount of Lines for making pairs
	for i in range(Lines[1]):
		personOne = Lines[2*(i+1)]-1
		personTwo = Lines[(2*(i+1)+1)]-1

		#If person does not have a table...
		#O(1), constant to add a new value on array and append on list
		if (arrayOfPeople[personOne] == None):
			#Create a table for them
			arrayOfPeople[personOne] = table(personOne)
			arrayOfPeople[personOne].addPerson(personOne)

		#Move everyone from PersonTwo table to whatever table PersonOne has
		if (arrayOfPeople[personOne] == arrayOfPeople[personTwo]):
			pass
		#O(1), constant to add a new value on array and append on list
		elif (arrayOfPeople[personTwo] == None):
			arrayOfPeople[personTwo] = arrayOfPeople[personOne]
			arrayOfPeople[personTwo].addPerson(personTwo)
		else:
			arrayOfPeople = arrayOfPeople[personTwo].transferEveryone(arrayOfPeople[personOne], arrayOfPeople)

	return arrayOfPeople

def calculateTables(peopleInTables):
	#Make a hashmap with unique Keys (Tables) to find out how many unique tables there are
	uniqueTables = {}
	soloTable = 0
	#O(t), where t = amount of people
	for table in peopleInTables:
		#O(1) Finding a key on a dictionary is constant
		if (table == None):
			soloTable += 1
		elif table in uniqueTables:
			pass
		else:
			#O(1) Adding a key on a dictionary is constant
			uniqueTables.update(table=1)

	#O(Un), where Un = amount of unique tables
	print(len(uniqueTables) + soloTable)

class table():
	def __init__(self, person):
		self.peopleList = []
		self.peopleList.append(person)

	def addPerson(self, person):
		self.peopleList.append(person)

	def transferEveryone(self, table, arrayOfPeople):
		#O(p), where p = number of people on the List of People to move from a table to another
		for person in self.peopleList:
			#Transfer table
			table.addPerson(person)
			#Update array with reference
			arrayOfPeople[person] = table

		return arrayOfPeople


# -----------------------------------------------------------------

f = open("input.txt", "r+")

numOfTest = int(f.readline())
#Check that T is of range [1, 26]
if (1 > numOfTest or numOfTest > 25):
	print("T must be of range: 1 <= T <= 25")
	exit(1)

toSend = []

#O(l), where l = number of lines on the input file
for line in f:
	if (line != "\n"):
		line = line.split(" ")
		toSend.append(int(line[0]))
		toSend.append(int(line[1]))
		#Check that N and M are within given ranges...
		if (int(line[0]) < 1):
			print("N must be of range: 1 <= N")
			exit(1)
		if (int(line[1])> 1000):
			print("M must be of range: M >= 1000")
			exit(1)
	else:
		arr = findTables(toSend)
		calculateTables(arr)
		toSend = []

arr = findTables(toSend)
calculateTables(arr)