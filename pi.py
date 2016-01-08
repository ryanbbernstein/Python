# coding: utf-8
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
from decimal import Decimal
ITTERATIONS = 1000000
pi = Decimal(0.0)
n = 1
while n <= ITTERATIONS * 2:
	pi += (Decimal(4.0)/Decimal(n))
	n += 2
	print pi
	pi -= (Decimal(4.0)/Decimal(n))
	n += 2
	print pi