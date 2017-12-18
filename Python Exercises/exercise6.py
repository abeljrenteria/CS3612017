#Exercise 6

	#a
def is_prime(n):
	if (n==1):
		return False
	elif (n==2):
		return True
	else:
		for x in range(2,n):
			if(n % x==0):
				return False
		return True

	#b
def is_prime(n):
	plus = 6n+1
	minus = 6n-1
	if(n==1):
		return False
	else:
		for i in range(2,n):
			if(n%i == 0):
				return False
		return True
	for i in range(3,n):
		if()