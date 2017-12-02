def BiggestValue(values):
	numbers = values.split()
	value = int(numbers[0])

	for number in numbers:
		if int(number) > value:
			value = int(number)
	return value

def SmallestValue(values):
	numbers = values.split()
	value = int(numbers[0])
	for number in numbers:
		if int(number) < value:
			value = int(number)
	return value

#For example, given the following spreadsheet:
#5 1 9 5
#7 5 3
#2 4 6 8
#The first row's largest and smallest values are 9 and 1, and their difference is 8.
#The second row's largest and smallest values are 7 and 3, and their difference is 4.
#The third row's difference is 6.
#n this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.
def Test():
	test = "5 1 9 5\n7 5 3\n2 4 6 8"
	checksum = 0
	rows = 0
	for row in test.split("\n"):
		rows += 1
		if row != "":
			checksum += BiggestValue(row) - SmallestValue(row)
	if checksum == 18:
		return True
	else:
		return False

#main program
if (Test()):
	print "Test Passed\n"
else:
	print "Test Failed\n"

puzzle_input = ""

with open('input.txt', 'r') as puzzle_file:
    puzzle_input = puzzle_file.read()

checksum = 0
rows = 0
for row in puzzle_input.split("\n"):
	rows += 1
	if row != "":
		checksum += BiggestValue(row) - SmallestValue(row)

print "Checksum is: " + str(checksum)