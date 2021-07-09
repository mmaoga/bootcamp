age = int(input("Please enter your age: "))
gender = str(input("Please select your gender, (M for Male and F for Female): "))

if age < 18:
	if gender == "M":
		print ("Son")
	else:
		print ("Daughter")

elif age >= 18 and age <65:
	if gender == "M":
		print ("Father")
	else:
		print ("Mother")
else:
	if gender == "M":
		print ("Grandfather")
	else:
		print ("Grandmother")
