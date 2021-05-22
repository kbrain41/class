numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
x = 1
for i in numbers:
	x*=i
	print(i,'', end='')
print(' =', x)