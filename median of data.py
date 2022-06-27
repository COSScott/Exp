data = [[1, 5, 7, 12, 36], [3, 4, 15, 16, 48], [0, 0, 1, 3, 10], [12, 16, 18, 23, 100]]
repeat = True
row = 0
while repeat == True:
	if row > 2:
		repeat = False
	row_length = len(data[row])
	median = (row_length // 2)
	print(data[row][median])
	row = row + 1
