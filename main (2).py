from tkinter import *

main = Tk()
main.title("Calculator App")

e = entry = Entry(main, width=60, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)



# Functions


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonclear():
    e.delete(0, END)

def buttonadd():
    number_one = e.get()
    global number1
    global calculator
    calculator = "addition"
    number1 = int(number_one)
    e.delete(0, END)

def buttonequal():
    numbertwo = e.get()
    e.delete(0, END)


    if calculator == "addition":
        e.insert(0, number1 + int(numbertwo))
    elif calculator == "subtraction":
        e.insert(0, number1 - int(numbertwo))
    elif calculator == "division":
        e.insert(0, number1 / int(numbertwo))
    elif calculator == "multiplication":
        e.insert(0, number1 * int(numbertwo))
    elif calculator  == "square":
        e.insert(0, number1**2)
    elif calculator == "square root":
        sqrt = number1 ** 0.5
        e.insert(0, sqrt(number1))
    elif calculator == "decimal":
        e.insert(float(0))


def buttonminus():
    number_one = e.get()
    global number1
    global calculator
    calculator = "subtraction"
    number1 = int(number_one)
    e.delete(0, END)

def buttonmultiply():
    number_one = e.get()
    global number1
    global calculator
    calculator = "multiplication"
    number1 = int(number_one)
    e.delete(0, END)

def buttondivide():
    number_one = e.get()
    global number1
    global calculator
    calculator = "division"
    number1 = int(number_one)
    e.delete(0, END)

def buttonsquare():
    number_one = e.get()
    global number1
    global calculator
    calculator = "square"
    number1 = int(number_one)
    e.delete(0, END)

def buttonsquareroot():
    number_one = e.get()
    global number1
    global calculator
    calculator = "square root"
    number1 = int(number_one)
    e.delete(0, END)

def buttondot():
    number_one = e.get()
    global number1
    global calculator
    calculator = "decimal"
    number1 = float(number_one)
    e.delete(0, END)



# buttons

label_1 = Button(text="1",  padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(1))
label_2 = Button(text="2",  padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(2))
label_3 = Button(text="3" ,  padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(3))
label_4 = Button(text="4", padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(4))
label_5 = Button(text="5", padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(5))
label_6 = Button(text="6", padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(6))
label_7 = Button(text="7", padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(7))
label_8 = Button(text="8", padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(8))
label_9 = Button(text="9", padx=40, pady=20, bg="Powder Blue", command=lambda: button_click(9))
label_0 = Button(text="0", padx=39.5, pady=20, bg="Powder Blue", command=lambda: button_click(0))

label_equal = Button(text="=", padx=45, pady=20, bg="Powder Blue", width=9, command=lambda: buttonequal())
label_plus = Button(text="+", padx=40, pady=20, width=9, bg="Powder Blue", command=lambda: buttonadd())
label_minus = Button(text="-", padx=40, pady=20, width=9, bg="Powder Blue", command=lambda: buttonminus())
label_multiply = Button(text="x", padx=40, pady=20, width=9, bg="Powder Blue", command=lambda: buttonmultiply())
label_divide = Button(text="/", padx=40, pady=20, width=9, bg="Powder Blue", command=lambda:buttondivide())
label_clear = Button(text="C", font=15, padx=37, pady=17, bg="Powder Blue", command=lambda: buttonclear())
label_square = Button(text="Sq", padx=30, pady=20, bg="Powder Blue", command=lambda: buttonsquare())
label_squareroot = Button(text="Sqrt", padx=35, pady=20, bg="Powder Blue", command=lambda: buttonsquareroot())
label_dot = Button(text=".", padx=35, pady=55, bg="Powder Blue", command=lambda: buttondot())




#for alignment

label_1.grid(row=3,column=0)
label_2.grid(row=3,column=1)
label_3.grid(row=3, column=2)
label_divide.grid(row=1, column=3)
label_4.grid(row=2, column=0)
label_5.grid(row=2, column=1)
label_6.grid(row=2, column=2)
label_multiply.grid(row=2, column=3)
label_7.grid(row=1, column=0)
label_8.grid(row=1, column=1)
label_9.grid(row=1, column=2)
label_minus.grid(row=3, column=3)
label_0.grid(row=4, column=1)
label_equal.grid(row=5, column=3)
label_plus.grid(row=4, column=3)
label_clear.grid(row=4, column=0)
label_square.grid(row=5, column=0)
label_squareroot.grid(row=5, column=1)
label_dot.grid(row=4, column=2, rowspan=2)






main.mainloop()
