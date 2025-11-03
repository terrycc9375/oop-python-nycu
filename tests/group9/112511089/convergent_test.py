import random
import math

x = random.randint(-10000, 10000)
y = int()
error = 1e-15
while True:
	y = math.sin(x)
	print(x)
	if (abs(y - x) < error):
		break
	x = y
