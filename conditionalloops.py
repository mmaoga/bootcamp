# fruits = ["Apple","Banana","Cherry"]
# for x in fruits:
# 	if x == "Banana":
# 		continue
# 	print (x)


# fruits = ["Apple","Banana","Cherry"]
# for x in fruits:
# 	if x == "Apple" :
# 		break
# print ( x )


#even numbers
# for num in range(1,100,3): # 1 is the start point, 100 is the end point and 3 is the step point
# 	if num%2==0:
# 		print(num)
# 	# num=num+3

#prime numbers

for num in range(1,100+1):
	if num>1:
		for j in range (2,num):
			if(num % j==0):
				break
		else:
			print(num)


# num = 407

# # num = int(input ("Please Enter a Number: ")
# 	if num > 1:
# 		for i in range (2,num):
# 			if (num % i) == 0:
# 				print (num, "is not a prime number")
# 				print (i,"times", num//i, "is",num)
# 				break
# 		else:
# 			print (num,"is not a prime number")
# 	else:
# 		prime(num,"is not a prime number")
