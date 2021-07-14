
# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen"]
# print (x)



# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen"]
# x = len(cars)
# print (x)


# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen"]
# cars.remove("Volvo") #removing by calling its name
# print (cars)


# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen"]
# cars.pop(0) #removing by calling its index
# print (cars)


# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen"]
# cars.append("Toyota") #adding stuff to the arrray by appending
# print (cars)



# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen"]
# cars.pop(2) #removing by calling its index
# print (cars)


# first_name =str(input('Please enter the first name: '))
# second_name =str(input('Please enter the second name: '))
# third_name =str(input('Please enter the third name: '))

# names = [first_name, second_name,third_name]

# names.reverse()
# print (names)

# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen", "Volvo"]
# fruits = ["Apple", "Oranges"]
# fruits.insert(1, "grapes")
# x = fruits.copy()
# cars.pop(1) #removing by calling its index

# cars.extend(fruits)
# print (cars)
# print (x)

# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen"]
# cars.clear()
# print (cars)


# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen", "Volvo"]
# x = cars.count("Volvo") # counting
# print (x)


# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen", "Volvo"]
# cars.sort(reverse = True) # sorting
# print (cars)


# cars = ["Ford", "Volvo", "BMW", "Range Rover", "Volkswagen", "Volvo"]
# cars.sort() # ascending SORTING
# print (cars)



# import stdio

# a = []
# for i in range (1000):
# 	a += [1]

# 	# x = a[1000]
# 	print(a)

# x = len(a)
# print (x)

# a = [1, 2, 3]
# for i in range(10):
# 	a[0] = i * i
# 	print(a)




# n = 10
# a = [0, 1]
# for i in range(2, n):
# 	a += [a[i-1] + a[i-2]]

# 	print(a)

import stdio
from array import array


a = stdarray.create1D(10, 0)
for i in range(10):
	a[i] = 9 - i
	for i in range(10):
		a[i] = a[a[i]]
		for v in a:
			stdio.writeln(v)

#Quiz number 4 create an array and add stuff.
#projects are to be completed by the end of the program by 28th July, 2021
