name = input ("What is your name: ").upper()
print ("Hi " + name)

age = int(input("Please enter your age: "))
gender = str(input("Please select your gender, (M for Male and F for Female): ")).upper()
parent = str(input("Do you have children? Y/N: ")).upper()


if age < 18:
	if gender == "M" and parent == "N":
		print ("You are a Son")
	else:
		print ("You are a Daughter")

elif age >= 18 and age <65:
	if gender == "M" and parent == "Y":
		print ("You are a Father") 
	else:
		print ("You are a Mother")
else:
	if gender == "M" and parent == "Y":
		print ("You are a Grandfather")
	else:
		print ("You are a Grandmother")

# age = int(input("Enter your age: "))
# print ("You are " + str(age)