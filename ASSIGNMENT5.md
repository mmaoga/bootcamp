## 1 What is the difference between = and ==?
     = is used for assigning variables while == is used as a comparison operator for boolean functions or results

## 2 Can I leave out the colon in an if, while, or for statement? 
	 NO

## 3 Should I use tab characters to indent my code?
     YES

## 4 Compose a program that takes three integer command-line arguments and writes "equal" if all three are equal and "not equal"  otherwise
	num1 =int(input('Please enter the first number:'))
	num2 =int(input('Please enter the second number: '))
	num3 =int(input('Please enter the third number: '))

	if num1 == num2 == num3:
		print(" EQUAL")
	else:
		print("NOT EQUAL")

## 5 What is the value of j after each of the following code fragments is executed?

	## a 	j = 0
			for i in range (0, 10):
				j += i
				print (j)
		
		Output:		
			0
			1
			3
			6
			10
			15
			21
			28
			36
			45

	## b 	j = 1
			for i in range (0, 10):
				j += j
				print (j)
		
		Output:
			2
			4
			8
			16
			32
			64
			128
			256
			512
			1024

	## c  	for j in range (0, 10):
				j += j
				print (j)
		
		Output:
			0
			2
			4
			6
			8
			10
			12
			14
			16
			18

## 6 what are m and n after the following code is executed?

		n = 123456789
		m = 0
		while n != 0:
			m = (10 * m) + (n % 10)
			n //= 10
			print (m, n)

	Output:
		m    n
		9 12345678
		98 1234567
		987 123456
		9876 12345
		98765 1234
		987654 123
		9876543 12
		98765432 1
		987654321 0



## 7 What does this code do?

		f = 0
		g = 1
		for i in range (0, 10):
			f = f + g
			g = f - g
			print (f)

	Output:
		1
		1
		2
		3
		5
		8
		13
		21
		34
		55


## BONUS QN:  Is there an example for when the following for and while loops are not equivalent?

			for variable in range(start, stop):
				statement1
				statement2
				...


			variable = start
			while variable < stop:
				statement1
				statement2

				...

				variable +=1


	ANSWER: YES
			for i in range (0, 10):
			if (i == 5): 
				continue
			print (i)
		
			#...


			i = 0
			while i < 10:
				if i ==5:
					continue
				print (i)
				i += 1

		Output:
			1
			2
			3
			4
			6
			7
			8
			9
			0
			1
			2
			3
			4





