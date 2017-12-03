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

def CheckSum2(values):
	numbers = values.split()
	checksum_for_row = 0
	matched_values = [0, 0];
	for i in range(0, len(numbers)):
		b = int(numbers[i])
		for j in range(0, len(numbers)):
			a = int(numbers[j])
			if a % b == 0 and a != b:
				checksum_for_row = a/b
#				print "a: " + str(a) + ", b: " + str(b) + ", cs: " + str(checksum_for_row)
	return checksum_for_row

#For example, given the following spreadsheet:
# 5 1 9 5
# 7 5 3
# 2 4 6 8
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

def Test2():
	test = "5 9 2 8\n9 4 7 3\n3 8 6 5"
	checksum = 0
	rows = 0
	for row in test.split("\n"):
		rows += 1
		if row != "":
			checksum += CheckSum2(row)
			print checksum
	if checksum == 9:
		return True
	else:
		return False

#main program
if (Test()):
	print "Test Passed\n"
else:
	print "Test Failed\n"
if (Test2()):
	print "Test 2 Passed\n"
else:
	print "Test 2 Failed\n"

puzzle_input = ""

with open('input.txt', 'r') as puzzle_file:
    puzzle_input = puzzle_file.read()

checksum  = 0
checksum2 = 0
rows = 0
for row in puzzle_input.split("\n"):
	rows += 1
	if row != "":
		checksum += BiggestValue(row) - SmallestValue(row)
		checksum2 += CheckSum2(row)

print "Checksum is: " + str(checksum)
print "Checksum 2 is: " + str(checksum2)
