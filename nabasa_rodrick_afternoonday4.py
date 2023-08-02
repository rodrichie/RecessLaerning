#functions
def my_function():
  print("Hello from a function")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")  

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: **
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#modules
#outputs,maps

