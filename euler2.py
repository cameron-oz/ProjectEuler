s = []
x = 1
y = 1
z = 0
while x<4000000:
	z = x
	x = x+y
	y = z
	if x%2 == 0:
		s.append(x)

k = sum(s)
print(k)