## 1 Compose a program that writes the Hello, World message 10 times. 

	print (“Hello, World\n”*10)        

or
	
	for i range (10):
	print (“Hello, World”)

## 2 Describe what happens if you omit the following in helloworld.py: the first ' the second ' the print() statement

	you get a syntax error (invalid syntax)
	the line with the error is indicated for ease of correction


## 3  Which one of the following is the correct way to execute useargument.py using the terminal: 
	• python3 useargument.py 

	• python useargument.py 
	


## 4 Modify helloworld.py to compose a program that takes three names and writes a proper sentence with the names in the reverse of the order they are given, so that, for example, python helloworld.py Alice Bob Carol writes the string 'Hi Carol, Bob, and Alice'

	first_name =str(input('Please enter the first name: '))
	second_name =str(input('Please enter the second name: '))
	third_name =str(input('Please enter the third name: '))

	print ("Hi", third_name,",",second_name, "and", first_name )
