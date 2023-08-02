#inheritance
'''
class Animal:
   def __init__(self,name):
      self.name = name

   def eat(self):
      print(f"{self.name} is eating...")

class Dog(Animal):
   def bark(self):
      print(f"{self.name}is barking...woof!")

class Cat(Animal):
   def meow(self):
      print(f"{self.name} is meowing...")      

#create animal objects
animal = Animal("Generic Animal")
dog = Dog("spot")
cat = Cat("Fluffy")      
cat.eat()
cat.meow()        




# exercise 1  demonstrate using inheritance to calculate area and perimeter of circle and rectangle
#respectively 
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())





#multiple inheritance
class Animal:
   def __init__(self,name):
      self.name = name

   def eat(self):
      print(f"{self.name} is eating")

class Flyable:
   def fly(self):
      print(f"{self.name} is flying")

class Bird(Animal, Flyable):
   def __init__(self,name,species):
      super().__init__(name)
      self.species = species              

   def display_info(self):
      super().display_info()
      print(f"species:{self.species}")
      print(f"Name:{self.name}")

#create  a bird object
my_bird =Bird("Pigeon","bird")

#invoke the bird object
my_bird.eat()
my_bird.fly()
my_bird.display_info()

#Method overriding
class Animal:
   def make_sound(self):
      print("Animal is making sound")

class Dog(Animal):
   def make_sound(self):
      print("Dog is making sound")

class Cat(Animal):
   def make_sound(self):
      print("Cat is making sound")

def make_animal_sound(animal):
   animal.make_sound()

#create objects
animal = Animal()
dog = Dog()
cat = Cat()

#calling make animal sound function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)
'''
#polymophism
class Shape:
   def calculate_area(self):
      pass

class Rectangle(Shape):
   def __init__(self, length,width):
      self.length = length   
      self.width = width

   def calculate_area(self):
      return self.length*self.width

class Circle(Shape):
   def __init__(self, radius):
      self.radius = radius

   def calculate_area(self):
      return 3.14*self.radius*self.radius
   def calculate_circumference(self):   
      return 2*3.14*self.radius
   
#create shape objets
rectangle = Rectangle(5,4)
circle = Circle(5)

#calculate display area
print(f"Rectangle area = {rectangle.calculate_area()}")
print(f"Circle area = {circle.calculate_area()}")

#Abstraction
#allows youto focus on essential features and hide from them from unnecessary details
#example 
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
   @abstractmethod
   def start(self):
      pass
   
   @abstractmethod
   def stop(self):
      pass
class Car(Vehicle):
   def start(self):
      print("Starting car...")   
   def stop(self):
      print("Stopping car...")
       
class Truck(Vehicle):
   def start(self):
      print("Starting truck...")       

   def stop(self):
      print("Stopping truck...")

#creaate vehicleobjects
car = Car()
truck = Truck()

#start the vehicle
car.start()
truck.start()
#stop the vehicle
car.stop()
"""
#exercise2 demonstrate abstraction using calculating area of a circle and rectangles

from abc import ABC, abstractmethod
import tkinter as tk

class Printable(ABC):
    @abstractmethod
    def generate_printable(self):
        pass
   
class GroceryPrintable(Printable):
    def __init__(self, items):
        self.items = items

    def generate_printable(self):
        printable = "---------Grocery Printable---------\n"
        total_cost = 0
        for item, price in self.items.items():
            printable += f"{item}: shs {price}\n"
            total_cost += price
        printable += "------------------------\n"
        printable += f"Total: shs {total_cost}\n"
        return printable

class ClothingPrintable(Printable):
    def __init__(self, items):
        self.items = items

    def generate_printable(self):
        printable = "---------Clothing Printable---------\n"
        total_cost = 0
        for item, price in self.items.items():
            printable += f"{item}: shs {price}\n"
            total_cost += price
        printable += "-------------------------------------\n"
        printable += f"Total:  shs {total_cost}\n"
        return printable

def print_receipt():
    if selected_printable_type.get() == "Grocery":
        printable = GroceryPrintable({"Apple": 1500.0, "Banana": 500.0, "Bread": 3000.0})
    elif selected_printable_type.get() == "Clothing":
        printable = ClothingPrintable({"Shirt": 15000.0, "Pants": 30000.0, "Socks": 5000.0})
    else:
        return

    printable_text.delete("1.0", tk.END)
    generated_printable = printable.generate_printable()
    printable_text.insert(tk.END, generated_printable)

# GUI setup
root = tk.Tk()
root.title("Printable Printing Program")

selected_printable_type = tk.StringVar()
selected_printable_type.set("Grocery")

printable_label = tk.Label(root, text="Select Printable Type")
printable_label.pack()

grocery_radio = tk.Radiobutton(root, text="Grocery", variable=selected_printable_type, value="Grocery")
grocery_radio.pack()

clothing_radio = tk.Radiobutton(root, text="Clothing", variable=selected_printable_type, value="Clothing")
clothing_radio.pack()

print_button = tk.Button(root, text="Print Printable", command=print_receipt)
print_button.pack()

printable_text = tk.Text(root, height=10, width=40)
printable_text.pack()

root.mainloop()


