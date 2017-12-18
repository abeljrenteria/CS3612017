#Exercise 13

import re
email = []
with open("~/Desktop/emails.txt") as file:
	counter = 1
	line = file.readLine()
	while line:
		reg = re.compile("([a-zA-Z0-9]*[@][a-zA-Z]*[.]['com'||'edu'||'co.uk'||'es']*)")
		for line in file:
			email += reg.findall(line)
            print(email)
            line = file.readline() 
            counter += 1 
