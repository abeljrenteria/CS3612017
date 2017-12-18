#Exercise 8

a = [1, 2, 3, 4]
b = a
b[1] = 3
c = a[:]
c[2] = 3

def set_first_elem_to_zero(l):
	l[0] = 0
	print l

def main():
	l = [1,5,10,13]
	set_first_elem_to_zero(l)
	print(l)

def __name__== "__main__":
	main()
