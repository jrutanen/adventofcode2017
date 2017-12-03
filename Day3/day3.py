# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...


# While this is very space-efficient (no squares are skipped), requested data must be carried
# back to square 1 (the location of the only access port for this memory system) by programs
# that can only move up, down, left, or right. They always take the shortest path:
# the Manhattan Distance between the location of the data and square 1.

# For example:

# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.

def GetCornerValues(rows):
	#top right corner, top left corner, bottom left corner, bottom right corner
	corner_values = [0, 0, 0, 0]
	first_number = (rows - 2)*(rows - 2) + 1
	corner_values[0] = first_number + rows - 2
	for i in range(1, 4):
		corner_values[i] = corner_values[i-1] + rows - 1
	return corner_values

def GetPosition(value, rows):
	#up/down, left/right
	values = [0, 0]
	distance = rows/2
	#if maximum for layer
	if(value == rows * rows):
		values[0] = rows / 2
		return values

	corners = GetCornerValues(rows)

	#value minus first value of this layer
	#quarter 0, max left then up/down
	if value <= corners[0]:
		midpoint = corners[0] - rows/2
		values[0] = abs(value - midpoint)
		values[1] = distance
	#quarter 1, max down and left/right
	elif value <= corners[1]:
		values[0] = distance
		midpoint = corners[1] - rows/2
		values[1] = abs(value - midpoint)
	#quarter 2, max right and up/down
	elif value <= corners[2]:
		midpoint = corners[2] - rows/2
		values[0] = abs(value - midpoint)
		values[1] = distance
	#quarter 3, max up and left/right
	else:
		values[0] = distance
		midpoint = corners[3] - rows/2
		values[1] = abs(value - midpoint)
	
	return values

def CountSteps(value):
 	# row and column of the item is base on the layer. Each layer has values
	# currentrow^2 - previousrow^2
	# first value is located in the last column (current) and in the next last row
	# (last row in previous layer)
	if value == 1:
		return 0
	nbr_of_rows = CountNumberOfRows(value)
	steps = GetPosition(value, nbr_of_rows)
	stepcount = steps[0] + steps[1]
	return stepcount

def CountNumberOfRows(value):
	# each layer adds + 2 in rows +2 in columns
	# number of values in each layer is rows * columns
	rows = 1
	total_memory = 0
	while total_memory < value:
		total_memory = rows * rows
		if (total_memory < value):
			rows += 2
	return rows

def Test():
	result = True
	if CountSteps(1) != 0:
		result = False
		print "Count Memory Test 1 failed"

	if CountSteps(12) != 3:
		result = False
		print "Count Memory Test 2 failed"

	if CountSteps(13) != 4:
		result = False
		print "Count Memory Test 5 failed"

	if CountSteps(17) != 4:
		result = False
		print "Count Memory Test 6 failed"

	if CountSteps(21) != 4:
		result = False
		print "Count Memory Test 7 failed"

	if CountSteps(23) != 2:
		result = False
		print "Count Memory Test 3 failed"

	if CountSteps(1024) != 31:
		result = False
		print "Count Memory Test 4 failed"

	return result

#main
if(Test()):
	print "Tests passed"
else:
	print "Tests failed"

print str(CountSteps(347991))