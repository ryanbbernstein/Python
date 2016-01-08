word = " bottles of beer"
for x in range(99, 0, -1):
	if x == 1: word = " bottle of beer"
	print "{0}{1} on the wall\n{0}{1}\nTake one down, pass it around\n{2}{1} on the wall\n ".format(x, word, x - 1)