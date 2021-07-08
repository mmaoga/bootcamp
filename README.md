# Part A - Account Creation


## 0: Creating a GitHub account

Go to [github.com](https://github.com/) and create an account. After you have verified your email, create an empty repository in your new account, and name it **bootcamp**

# Part B - Terminal Commands
  

## 1: Our first command

Write a command that prints out the string “hello, world”. Extra credit: As in Listing 1, do it two different ways, both with and without using quotation marks.

<<<<<<< HEAD
	echo "Hello, World"

	echo Hello, World
=======
echo "Hello, World"
echo  Hello, World

>>>>>>> f902e375dac6b79bd787ba003227bb21cb3dc11f

## 2: Cleaning up

Clear the contents of the current tab.

	clear

## 3: Listing

What’s the command to list all the files (and directories) on your Desktop directory? 

	ls


## 4: Making directories

Make the directory **bootcamp** on your Desktop and, within it, the directory **labs** (i.e., ~/Desktop/bootcamp/labs).


	Denniss-MacBook-Air:~ dennismanyara$ mkdir bootcamp
	Denniss-MacBook-Air:~ dennismanyara$ cd bootcamp
	Denniss-MacBook-Air:bootcamp dennismanyara$ mkdir labs

## 5: Navigating directories

Change to your Desktop, then change to bootcamp directory, and then the lab directory.

	Denniss-MacBook-Air:~ dennismanyara$ cd desktop
	Denniss-MacBook-Air:desktop dennismanyara$ cd bootcamp
	Denniss-MacBook-Air:bootcamp dennismanyara$ cd labs

or

	Denniss-MacBook-Air:~ dennismanyara$ cd ~dennismanyara/desktop/bootcamp/labs

## 6: Creating files

Create an empty file called file01 in the lab directory. 

	Denniss-MacBook-Air:labs dennismanyara$ touch file01


## 7: Deleting directories

What is the command used to remove a directory named **food** and everything inside it. 

		rm -r food

# Part C - Github 

## 8: Download the GitHub desktop application

Download the [GitHub desktop application](https://desktop.github.com/).

## 9: Pushing work to GitHub

Using the GitHub desktop application, push your code to your new repository.
