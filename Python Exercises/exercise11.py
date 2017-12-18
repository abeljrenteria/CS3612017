#Exercise 11

def iteration(x):
	i = 1;
	element = x[0]
	if len(x) == 0:
		return 0
	while i < len(x):
		element = element * x[i]
		i = i + 1
	return element

def recursion(x):
	if len(x) == 1:
		return x[0]
	return recursion([x[0]]) * recursion(x[1:])