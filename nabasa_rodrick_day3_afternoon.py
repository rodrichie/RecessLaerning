#exercise1
#question1 Create a list with 5 items (names of people) and write a python program to output the 2nd item

names=['ronald', 'ethan', 'sam','leynae','calvin']
print (names[1])

#question2 Write a python program to change the value of the first item to a new value
names[0]='atuhaire'
print (names[0])

#question3  Write a python program to add a sixth item to the list
names.append('rodrick')
print(names)

#question4 Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2,'bathel')
print(names)

#question5 Write a python program to remove the 4th item from the list
names.pop(3)
print(names)

#question6  Use negative indexing to print the last item in your list
print(names[-1])

#question7 Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
new_list=['gun','bullet','ball','waters','ship','cargo','bill']
print(new_list[2:5])

#question8 Write a list of countries and make a copy of it
countries=['Brazil','France','Germany','Netherlands','United Kingdom','United States']
countries_copy=countries.copy()
print(countries_copy)

#question9  Write a python program to loop through the list of countries
for country in countries:
    print(country)

#question10 Write a list of animal names and sort them in both descending and ascending order.
animal_names = ['lion', 'goat', 'zebra', 'eagle', 'anaconda' ]
animal_names.sort()
print(animal_names)

animal_names.sort(reverse=True)
print(animal_names)

#question11 . Using the list above, write a python program to output only animal names with the letter 
#‘a’ in them
for name in animal_names:
    if 'a' in name:
        print(name)

#question12  Write two lists, one containing your first names and the other your second names. Join 
#the two lists.    
first_names=['John','Peter','Smith','Bob' ]
second_names=['Atuhaire','Nabasa','Aine','Aheebwa']  
names=first_names + second_names
print(names)

#exercise 2
#question1
x = ("samsung", "iphone", "tecno", "redmi")
favorite="samsung"
if favorite in x:
    print(favorite)

#question2 Use negative indexing to print the 2nd last item in your tuple
print(x[-2])    

#question3 using the phones list above, write a python program to update “iphone” to “itel”
y=list(x)
y[1]="itel"
x=tuple(y)
print(x)

#question4 Write a python program to add “Huawei” to your tuple.
y=list(x)
y.append("Huawei")
x=tuple(y)
print(x)

#question5 Write a python program to loop through the tuple above.
for i in x:
    print(i)

#question6  Write a python program to remove/delete the first item in your tuple
y=list(x)
y.pop(1) 
x=tuple(y)   
print(x)

#question7  Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(("Kampala", "Mbarara", "Jinja" ,"Gulu" ,"Mbale", "Hoima")) # note the double round-brackets
print(cities)

#question8 write a python program to unpack your tuple.
(green, yellow, red , black , orange, white) = cities

print(green)
print(yellow)
print(red)
print(black)
print(orange)
print(white)

#question9  Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print(cities[1:4])

#question10 . Write two tuples, one containing your first names and the other your second names. Join 
#the two tuples.
first_names = ('John', 'Alice', 'Michael')
last_names = ('Smith', 'Johnson', 'Williams')

full_names = first_names + last_names

print(full_names)

#question11 Create a tuple of colors and multiply it by 3.
colors = ('red', 'green', 'blue')

multiplied_colors = colors * 3

print(multiplied_colors)

#question12 . Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)

print(count_8)

#exercise3
#question1 . Use the set() constructor to create a set of 3 of your favorite beverages.
favorite_beverages = set(['coffee', 'tea', 'juice'])

print(favorite_beverages)

#question2 Use the correct method to add 2 more items to the beverages set.
favorite_beverages.update(['soda', 'smoothie'])
print(favorite_beverages)

#question3 Given the set below;
#Check if microwave is present in the set.
mySet = {"oven","kettle","microwave","refrigerator"}
if "microwave" in mySet:
  print ("microwave is present in the set")

#question4 Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print(mySet)

#question5 write a python program to loop through the set above.
for mySet in mySet:
    print(mySet)

#question6  Write a set of 4 items and a list of two items. Write a python program to add elements in 
#the list to elements in the set.   
mySett={"ball","water","pool","car"}
mylist=["Moon","sun"]
mySett.update(mylist)
print (mySett)

#Write two sets, one containing your ages and the other your first names. Join the two 
#sets.
ages = {25, 30, 35}
first_names = {'John', 'Alice', 'Michael'}

joined_set = ages.union(first_names)

print(joined_set)

#exercise4
#question1 Declare two variables, an integer and a string and use the correct method to concatenate 
#the two variables
my_integer = 10
my_string = "Hello"

concatenated_string = str(my_integer) + my_string

print(concatenated_string)

#question2 Consider the example below;
#Output the string without spaces at the beginning, in the middle and at the end
txt = " Hello, Uganda! "

stripped_txt = txt.strip()

print(stripped_txt)

#question3  Write a python program to convert the value of ‘txt’ to uppercase.
uppercase_txt = txt.upper()

print(uppercase_txt)

#question4 . Write a python program to replace character ‘U’ with ‘V’ in the string above.
modified_txt = txt.replace('U', 'V')

print(modified_txt)

#question5  Using the code below, write a python program to return a range of characters in the 2nd
#, 
#3
#rd and 4th position.
#y = “I am proudly Ugandan”
y = "I am proudly Ugandan"

substring = y[1:4]

print(substring)

#question6 . The piece of code below will give an error when output;
#x = “All “Data Scientists” are cool!” 
#Write a python program to correct it.
#x = 'All "Data Scientists" are cool!'
# or
x = "All \"Data Scientists\" are cool!"

print(x)

#exercise 5
#question1 With reference to the dictionary below, write a python program to print the value of the 
#shoe size. 
#Add this dictionary to your .py file
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

shoe_size = Shoes["size"]
print(shoe_size)

#2 Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)

#3  Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)

#4 . Write a python program to return a list of all the keys in the dictionary above.
keys_list = list(Shoes.keys())
print(keys_list)

#5  Write a python program to return a list of all the values in the dictionary above.
values_list = list(Shoes.values())
print(values_list)

#6  Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("Key 'size' exists")
else:
    print("Key 'size' does not exist")

#7   Write a python program to loop through the dictionary above
for key, value in Shoes.items():
    print(key, ":", value)

#8 . Write a python program to remove “color” from the dictionary.
del Shoes["color"]
print(Shoes)

#9   Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)

#10 write a dictionary of your choice and make a copy of it
original_dict = {"key": "value"}

# Method 1: Using the dict() constructor
copied_dict1 = dict(original_dict)

# Method 2: Using the copy() method
copied_dict2 = original_dict.copy()

print(copied_dict1)
print(copied_dict2)

#11   Write a python program to show nested dictionaries
nested_dict = {
    "outer_key": {
        "inner_key1": "value1",
        "inner_key2": "value2"
    }
}

print(nested_dict)






