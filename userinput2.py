num = int(input("Please enter your scores:\n"))
if num<=100 and num>=80:
	print(" You have a perfect score of A+")
elif num<80 and num>=75:
	print("You have a perfect score of A-")
elif num<75 and num>=70:
	print("You have scored a grade of B+")
elif num<70 and num>=65:
	print("You have scored a grade of B")
elif num<65 and num>=60:
	print("You have scored a grade of B-")
elif num<60 and num>=55:
	print("You have scored a grade of C+")
elif num<55 and num>=50:
	print("You have scored an average grade of C")
elif num<50 and num>=45:
	print("You have scored a passing grade of C-")
else:
	print("You have scored a FAILED grade, Kindly prepare to retake this course next semester.")
