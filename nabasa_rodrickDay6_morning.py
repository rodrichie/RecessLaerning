#Regular expression
"""
Character	Description	Example	Try it
[]	A set of characters---->	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)---->"\d"	
.	Any character (except newline character)---->"he..o"	
^	Starts with	--->"^hello"	
$	Ends with---->"planet$"	
*	Zero or more occurrences---->"he.*o"	
+	One or more occurrences	---->"he.+o"	
?	Zero or one occurrences----->"he.?o"	
{}	Exactly the specified number of occurrences----->"he.{2}o"	
|	Either or----->"falls|stays"	
()	Capture and group	 	 
"""
#example 1
"""
import re
txt = "Hello, my name is Jeff Geoff. I am a programmer with 15 years of experience"

#match first word
match = re.search(r"^\w+$",txt)

if match:
    print("Match: ", match.group(1))

matches =re.findall(r"\d+",txt)
if matches:
    print("Matches: ", matches)    
"""
#validate email format or address format
'''
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    #explanation of the regular expression pattern
    #^        -start of the string
    #[\w\.-]+  -one or more word characters,dots, or dashes
    #@         -literal @ symbol
    # [\w\.-]+ -one or more word characters,dots, or dashes
    # \.       -literal dot
    # \w+      -one or more word characters
    # $         -end of the string

    if re.match(pattern, email) :
        return True
    else :
        return False

#example usage
email1 = "nabasarodrick@gmail.com" 
email2 = "invalid_email" 

print(validate_email(email1))
print(validate_email(email2))
'''
#Generaators and iterators
#'yield' generator
#iterator ' --iter--' '__next__' iterator
"""
def factorial_generator():
    n = 0
    factorial =1

    while True:
        yield factorial
        n += 1
        factorial *=n

factorial_gen =factorial_generator()
for _ in range(6):
    print(next(factorial_gen))   
"""
'''
def factorial(n):
    if n == 0:
        yield 1
    else:
        yield n * next(factorial(n - 1))

# Calculate and print factorials of numbers 1 to 10
for num in range(1, 11):
    result = next(factorial(num))
    print(f"The factorial of {num} is: {result}") 
'''
#generate a function to print squares of numbers 
'''
def squares():
    for i in range(1,10):
        yield i ** 2

#create an iterator object that yields the square of numbers from 1 - 10
squares_iterator=squares()

#print the first 5 squares of numbers from 1-10
for i in range(5):
    print(next(squares_iterator))  
'''
#Decorators     
# they allow you to mdify the behaviour of functions or classes without 
# directly changing their source code 
# @my_decorator
def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
    return inner

@my_decorator
def outer_decorator():
    print("This is the outer decorator")

outer_decorator()                     