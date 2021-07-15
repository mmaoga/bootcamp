# def evenOdd (x):
# 	if (x % 2 == 0):
# 		print ("even")

# 		


def hello_func(greeting, name = "You"):
	return "{}, {}.".format (greeting, name)

# print (hello_func("Hi", name = "Dennis"))

# print (len('Test'))




def student_info (*args, **kwargs):
	print (args)
	print (kwargs)

courses = ["Marth", "Art"]
info = {"name": "John", "age": 23}

student_info (*courses, **info)




