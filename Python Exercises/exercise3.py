#Exercise 3

float(123)			#output: 123.0
float('123') 		#output: 123.0
float('123.23')		#output: 123.23
int(123.23)			#output: 123
int('123.23')		#output: ValueError, invalid literal 
int(float('123.23'))#output: 123
str(12)				#output: 12
str(12.2)			#output: 12.2
bool('a')			#output: True
bool(0)				#output: False
bool(0.1) 			#output: True