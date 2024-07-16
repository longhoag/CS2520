"""lab1.ipynb
I use Google Colab for the assignment!
Original file is located at
    https://colab.research.google.com/drive/1VXYXsWkYd6JUK2Fh0AVKakoaSg917Xhd
"""

#Name: Long Hoang
#Lab 1

"""#Task 1
This program will display name, age, and work information including company, annual salary and monthly salary
"""

print("Task 1")

name = input("Please enter your name: ")
age = int(input("Please enter your age: ")) #get age as int
company = input("Enter the company you wish to work for: ")
salary = float(input("Enter the annual salary you wish to earn in dollars: ")) #get salary as float

print("Hello!")
print(f"My name is {name}, my age is {age}")
print(f"I hope to work for {company} and earn ${round(salary / 12, 2)} a month") #round number to 2 digits after the decimal point

"""#Task 2
This program will prompt a user enter an item name to be purchase, # of units purchased, total price paid and the average price
"""

print("\nTask 2")

product = input("Please enter the product you purchased: ")
amount = int(input("Please enter the number of units you purchased: "))
total = float(input("Please enter the total price paid: "))
average = round(total / amount, 2) #round the average to 2 digits after the decimal point

print("The average price per item is ${}".format(average)) #using format string

print(f"The purchase of {amount} items of {product} is ${int(total)}, and the average price for each item is ${average}") #using f-string format

# output task 1:
'''
Please enter your name: Alice Wonderland
Please enter your age: 20
Enter the company you wish to work for: Google
Enter the annual salary you wish to earn in dollars: 98576
Hello!
My name is Alice Wonderland, my age is 20
I hope to work for Google and earn $8214.67 a month
'''

'''
Please enter your name: Long
Please enter your age: 20
Enter the company you wish to work for: Apple
Enter the annual salary you wish to earn in dollars: 212000
Hello!
My name is Long, my age is 20
I hope to work for Apple and earn $17666.67 a month
'''

# output task 2:

'''
Please enter the product you purchased: apple
Please enter the number of units you purchased: 3
Please enter the total price paid: 5
The average price per item is $1.67
The purchase of 3 items of apple is $5, and the average price for each item is $1.67
'''

'''
Please enter the product you purchased: orange
Please enter the number of units you purchased: 5
Please enter the total price paid: 11.29
The average price per item is $2.26
The purchase of 5 items of orange is $11, and the average price for each item is $2.26
'''

'''
Please enter the product you purchased: watermelon
Please enter the number of units you purchased: 2
Please enter the total price paid: 18.99
The average price per item is $9.49
The purchase of 2 items of watermelon is $18, and the average price for each item is $9.49
'''