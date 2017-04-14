for x in range(99, 0, -1):
	print "{0} bottle{1} of beer on the wall\n{0} bottle{1} of beer\nTake one down, pass it around\n{2} bottle{1} of beer on the wall\n ".format(x, "s" if x != 1 else "", x - 1)
