# import tkinter as tk
# from tkinter.filedialog import askopenfilename, asksaveasfilename

# def open_file():
#     """Open a file for editing."""
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete(1.0, tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")

# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get(1.0, tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")

# window = tk.Tk()
# window.title("Simple Text Editor")
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)

# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
# btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")

# window.mainloop()

#................................................#

# # Python program to create a simple GUI
# # calculator using Tkinter

# # import everything from tkinter module
# from tkinter import *

# # globally declare the expression variable
# expression = ""


# # Function to update expression
# # in the text entry box
# def press(num):
#     # point out the global expression variable
#     global expression

#     # concatenation of string
#     expression = expression + str(num)

#     # update the expression by using set method
#     equation.set(expression)


# # Function to evaluate the final expression
# def equalpress():
#     # Try and except statement is used
#     # for handling the errors like zero
#     # division error etc.

#     # Put that code inside the try block
#     # which may generate the error
#     try:

#         global expression

#         # eval function evaluate the expression
#         # and str function convert the result
#         # into string
#         total = str(eval(expression))

#         equation.set(total)

#         # initialize the expression variable
#         # by empty string
#         expression = ""

#     # if error is generate then handle
#     # by the except block
#     except:

#         equation.set(" error ")
#         expression = ""


# # Function to clear the contents
# # of text entry box
# def clear():
#     global expression
#     expression = ""
#     equation.set("")


# # Driver code
# if __name__ == "__main__":
#     # create a GUI window
#     gui = Tk()

#     # set the background colour of GUI window
#     gui.configure(background="light green")

#     # set the title of GUI window
#     gui.title("Simple Calculator")

#     # set the configuration of GUI window
#     gui.geometry("270x150")

#     # StringVar() is the variable class
#     # we create an instance of this class
#     equation = StringVar()

#     # create the text entry box for
#     # showing the expression .
#     expression_field = Entry(gui, textvariable=equation)

#     # grid method is used for placing
#     # the widgets at respective positions
#     # in table like structure .
#     expression_field.grid(columnspan=4, ipadx=70)

#     # create a Buttons and place at a particular
#     # location inside the root window .
#     # when user press the button, the command or
#     # function affiliated to that button is executed .
#     button1 = Button(gui, text=' 1 ', fg='black', bg='red',
#                     command=lambda: press(1), height=1, width=7)
#     button1.grid(row=2, column=0)

#     button2 = Button(gui, text=' 2 ', fg='black', bg='red',
#                     command=lambda: press(2), height=1, width=7)
#     button2.grid(row=2, column=1)

#     button3 = Button(gui, text=' 3 ', fg='black', bg='red',
#                     command=lambda: press(3), height=1, width=7)
#     button3.grid(row=2, column=2)

#     button4 = Button(gui, text=' 4 ', fg='black', bg='red',
#                     command=lambda: press(4), height=1, width=7)
#     button4.grid(row=3, column=0)

#     button5 = Button(gui, text=' 5 ', fg='black', bg='red',
#                     command=lambda: press(5), height=1, width=7)
#     button5.grid(row=3, column=1)

#     button6 = Button(gui, text=' 6 ', fg='black', bg='red',
#                     command=lambda: press(6), height=1, width=7)
#     button6.grid(row=3, column=2)

#     button7 = Button(gui, text=' 7 ', fg='black', bg='red',
#                     command=lambda: press(7), height=1, width=7)
#     button7.grid(row=4, column=0)

#     button8 = Button(gui, text=' 8 ', fg='black', bg='red',
#                     command=lambda: press(8), height=1, width=7)
#     button8.grid(row=4, column=1)

#     button9 = Button(gui, text=' 9 ', fg='black', bg='red',
#                     command=lambda: press(9), height=1, width=7)
#     button9.grid(row=4, column=2)

#     button0 = Button(gui, text=' 0 ', fg='black', bg='red',
#                     command=lambda: press(0), height=1, width=7)
#     button0.grid(row=5, column=0)

#     plus = Button(gui, text=' + ', fg='black', bg='red',
#                 command=lambda: press("+"), height=1, width=7)
#     plus.grid(row=2, column=3)

#     minus = Button(gui, text=' - ', fg='black', bg='red',
#                 command=lambda: press("-"), height=1, width=7)
#     minus.grid(row=3, column=3)

#     multiply = Button(gui, text=' * ', fg='black', bg='red',
#                     command=lambda: press("*"), height=1, width=7)
#     multiply.grid(row=4, column=3)

#     divide = Button(gui, text=' / ', fg='black', bg='red',
#                     command=lambda: press("/"), height=1, width=7)
#     divide.grid(row=5, column=3)

#     equal = Button(gui, text=' = ', fg='black', bg='red',
#                 command=equalpress, height=1, width=7)
#     equal.grid(row=5, column=2)

#     clear = Button(gui, text='Clear', fg='black', bg='red',
#                 command=clear, height=1, width=7)
#     clear.grid(row=5, column='1')

#     Decimal= Button(gui, text='.', fg='black', bg='red',
#                     command=lambda: press('.'), height=1, width=7)
#     Decimal.grid(row=6, column=0)
#     # start the GUI
#     gui.mainloop()



#..................................................#


from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        # create screen widget
        self.screen = Text(master, state='disabled', width=30, height=3,background="yellow", foreground="blue")

        # position screen in window
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''

        # create buttons using method createButton
        b1 =  self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B",None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=',None,34)

        # buttons stored in list
        buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1,5):
            for column in range(4):
                buttons[count].grid(row=row,column=column)
                count += 1
        # arrange last button '=' at the bottom
        buttons[16].grid(row=5,column=0,columnspan=4)

    def createButton(self,val,write=True,width=7):
        # this function creates a button, and takes one compulsory argument, the value that should be on the button

        return Button(self.master, text=val,command = lambda: self.click(val,write), width=width)

    def click(self,text,write):
        # this function handles what happens when you click a button
        # 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen
        if write == None:

            #only evaluate code when there is an equation to be evaluated
            if text == '=' and self.equation: 
                # replace the unicode value of division ./.with python division symbol / using regex
                self.equation= re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == u"\u232B":
                self.clear_screen()
            
            
        else:
            # add text to screen
            self.insert_screen(text)
        

    def clear_screen(self):
        #to clear screen
        #set equation to empty before deleting screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        # record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state ='disabled')

root = Tk()
my_gui = Calculator(root)
root.mainloop()