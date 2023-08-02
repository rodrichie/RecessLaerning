#operators
"""
x = 5 + 3  # Adds 5 and 3, assigns result (8) to x
print (x)
y = 7 - 2  # Subtracts 2 from 7, assigns result (5) to y
print (y)
z = 4 * 6  # Multiplies 4 and 6, assigns result (24) to z
print (z)
w = 10 / 3  # Divides 10 by 3, assigns result (3.3333...) to w
print (w)
v = 10 // 3  # Divides 10 by 3, assigns floor result (3) to v
print (v)
r = 10 % 3  # Calculates remainder of 10 divided by 3, assigns result (1) to r
print (r)
p = 2 ** 3  # Raises 2 to the power of 3, assigns result (8) to p
print (p)
#assignment operator
a = 10  # Assigns the value 10 to variable a
print (a)
b = 5
b += 3  # Equivalent to b = b + 3, assigns result (8) to b
print (b)
#comparison operator
x = 5 == 3  # Checks if 5 is equal to 3, assigns False to x
print (x)
y = 7 != 2  # Checks if 7 is not equal to 2, assigns True to y
print (y)
z = 4 > 6  # Checks if 4 is greater than 6, assigns False to z
print (z)
w = 10 < 3  # Checks if 10 is less than 3, assigns False to w
print (w)
v = 10 >= 3  # Checks if 10 is greater than or equal to 3, assigns True to v
print (v)
u = 5 <= 5  # Checks if 5 is less than or equal to 5
print (u)

#logical operator
x = 5 < 10 and 2 > 1  # Checks if 5 is less than 10 and 2 is greater than 1
y = 5 < 10 or 2 > 1  # Checks if 5 is less than 10 or 2 is greater than 1
z = not (5 < 10)  # Negates the condition "5 is less than 10"

#membership operators
x = 5 in [1, 2, 3, 4, 5]  # Checks if 5 is present in the list [1, 2, 3, 4, 5]
print(x)
y = 6 not in [1, 2, 3, 4, 5]  # Checks if 6 is not present in the list [1, 2, 3, 4, 5]
print(y)

#Identity Operators
x = "Hello"
y = "Hello"
z = x is y  # Checks if x and y refer to the same object
print(z)

a = [1, 2, 3]
b = [1, 2, 3]
c = a is not b  # Checks if a and b refer to different objects
print(c)

#bitwise operators
x = 5 & 3  # Performs a bitwise AND of 5 (binary: 101) and 3 (binary: 011)
print(x)
y = 5 | 3  # Performs a bitwise OR of 5 (binary: 101) and 3 (binary: 011)
print(y)
z = 5 ^ 3  # Performs a bitwise XOR of 5 (binary: 101) and 3 (binary: 011)
print(z)
w = ~5  # Performs a bitwise NOT on 5 (binary: 101)
print(w)
a = 5 << 2  # Shifts the bits of 5 (binary: 101) two positions to the left
print(a)
b = 5 >> 2  # Shifts the bits of 5 (binary: 101) two positions to the right
print(b)
"""



#Exercise create a simple calculator program that with a GUI interface. 
# make the title of the calculator program window with a name e.g"Nabasa Rodrick Simple Calculator."


import tkinter as tk

def calculate(operation):
    num1 = float(entry_number1.get())
    num2 = float(entry_number2.get())

    if operation == "addition":
        result = num1 + num2
    elif operation == "subtraction":
        result = num1 - num2
    elif operation == "multiplication":
        result = num1 * num2
    elif operation == "division":
        if num2 != 0:
            result = num1 / num2
        else:
            label_result.config(text="Error: Division by zero")
            return

    label_result.config(text="Result: " + str(result))

# Create the main window
window = tk.Tk()
window.title("Nabasa Rodrick Simple Calculator")

# Create input fields for numbers
label_number1 = tk.Label(window, text="Number 1:")
label_number1.grid(row=0, column=0)
entry_number1 = tk.Entry(window)
entry_number1.grid(row=0, column=1)

label_number2 = tk.Label(window, text="Number 2:")
label_number2.grid(row=1, column=0)
entry_number2 = tk.Entry(window)
entry_number2.grid(row=1, column=1)

# Create buttons for calculations
button_addition = tk.Button(window, text="Add", command=lambda: calculate("addition"))
button_addition.grid(row=2, column=0)

button_subtraction = tk.Button(window, text="Subtract", command=lambda: calculate("subtraction"))
button_subtraction.grid(row=2, column=1)

button_multiplication = tk.Button(window, text="Multiply", command=lambda: calculate("multiplication"))
button_multiplication.grid(row=3, column=0)

button_division = tk.Button(window, text="Divide", command=lambda: calculate("division"))
button_division.grid(row=3, column=1)

# Create a label to display the result
label_result = tk.Label(window, text="Result: ")
label_result.grid(row=4, columnspan=2)

# Start the main loop
window.mainloop()
