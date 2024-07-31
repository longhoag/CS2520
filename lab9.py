
"""lab9.ipynb
"""

#Name: Long Hoang
#Lab9

"""#Task 1

This program will create a room class with length and width as 2 data members, perform some class calculation
"""

class Room:
  #initialize
  def __init__(self, width, length):
    self.width = width
    self.length = length

  #special method
  def __str__(self):
    return f"This is a room of size {self.width}' width x {self.length}' length"

  #get length
  def get_length(self):
    return self.length

  #get width
  def get_width(self):
    return self.width

  #set length
  def set_length(self, length):
    self.length = length

  #set width
  def set_width(self, width):
    self.width = width

  #calculate area
  def calculate_area(self):
    return self.length * self.width

def task1():
  room1 = Room(30, 55)
  room2 = Room(65, 42)
  print(room1)
  print(room2)
  print(f"The area of Room 1 is {room1.calculate_area()} feet square")
  print(f"The area of Room 2 is {room2.calculate_area()} feet square")

  #2nd test run
  print()
  room3 = Room(10.5, 21)
  room4 = Room(22, 31.5)
  print(room3)
  print(room4)
  print(f"The area of Room 3 is {room3.calculate_area()} feet square")
  print(f"The area of Room 4 is {room4.calculate_area()} feet square")

"""#Task 2

This program will create a polygon class and its inheritance
"""

class Polygon:
  #initialize
  def __init__(self, n_sides):
    #declare number of sides
    self.n = n_sides
    #generate each side a length of 0
    self.sides = [0 for _i4 in range(n_sides)]

  def inputSides(self):
    #prompt to input the length of side
    self.sides = [float(input(f"Enter side {i+1} : ")) for i in range(self.n)]

  def displaySides(self):

    #display side information
    for i in range(self.n):
      print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
  #initialize
  def __init__(self):
    #triangle by default has 3 sides
    Polygon.__init__(self, 3)

  def findArea(self):
    #calculate the area from 3 sides
    a, b, c = self.sides
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    return area


def task2():
  p = Polygon(4)
  print("Create Polygon Object: ")
  p.inputSides()
  print("Polygon Object: ")
  p.displaySides()

  print("\nCreate Triangle Object: ")
  t = Triangle()
  t.inputSides()
  print("\nTriangle Object: ")
  t.displaySides()
  print("The area of the triangle is ", t.findArea())

def main():
  print("Task 1: ")
  task1()
  print("\nTask 2: ")
  task2()

main()

#output task 1

'''
This is a room of size 30' width x 55' length
This is a room of size 65' width x 42' length
The area of Room 1 is 1650 feet square
The area of Room 2 is 2730 feet square

This is a room of size 10.5' width x 21' length
This is a room of size 22' width x 31.5' length
The area of Room 3 is 220.5 feet square
The area of Room 4 is 693.0 feet square
'''

#output task 2

'''
Create Polygon Object:
Enter side 1 : 5
Enter side 2 : 5
Enter side 3 : 6
Enter side 4 : 9
Polygon Object:
Side 1 is 5.0
Side 2 is 5.0
Side 3 is 6.0
Side 4 is 9.0

Create Triangle Object:
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4

Triangle Object:
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0
The area of the triangle is  6.0
'''