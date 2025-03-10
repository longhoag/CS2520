# -*- coding: utf-8 -*-
"""lab4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11KvxqrXqfD_HNbzElhQtfr_Wi0AGbdQA
"""

#Name: Long Hoang
#Lab 4

"""#Task 1

This program will take a string as parameter and returns two values, the counts of upper and lower case letters respectively
"""

def count_letters(sentence): #taking a string as parameter
  # Initialize count variables
  upper = 0
  lower = 0
  # Iterate over the string
  for char in sentence:
    if char.isupper(): #if uppercase
      upper += 1
    elif char.islower():#if lowercase
      lower += 1

  return upper, lower #return 2 count values

def task1():
  # 4 test cases
  sentence = ["The quick Brown Fox", "", "je suis francais", "ALLEZ LES BLEUS"]
  for sen in sentence:
    print(f"Input string: {sen}")
    upper, lower = count_letters(sen)
    print("No. of Upper case letters:", upper)
    print("No. of Lower case letters:", lower)
    print()

"""#Task 2

This program will calculate the price with given price, discount and tax rate
"""

def price_calculator (original_price, discount = 0, tax_rate = 0.08) : #with default sale tax and discount rate
  discount_price = original_price * (1 - discount) #calculate discounted price
  after_tax_price = discount_price * (1 + tax_rate) #calculate after tax price
  return round(after_tax_price, 2) #return proper dollar format

def formatPrinting(price, discount, tax): #to avoid code repitition
  print(f"Original Price: ${price}")
  print(f"Discount: {discount}")
  print(f"Tax Rate: {tax}")

def task2():

  formatPrinting(100, '20%', '8%') #format print the data before calculation
  print(f"After Tax Price: ${price_calculator(100, 20/100)}\n") #tax rate is default

  formatPrinting(523, 'none', '9.5%') #none is using the default
  print(f"After Tax Price: ${price_calculator(original_price=523, tax_rate=9.5/100)}\n") #discount rate is default

  formatPrinting(250, '35%', 'none')
  print(f"After Tax Price: ${price_calculator(original_price=250, discount=35/100)}\n") #tax rate is default

  formatPrinting(210, '5%', '9.8%')
  print(f"After Tax Price: ${price_calculator(210, 5/100, 9.8/100)}") #my test data

"""#Task 3

This program will take 0 or more string and then combine them.
"""

def address_book(*addr):
  result = ""
  for a in addr:
    result += a + "\n" #add \n
  return result

def task3():
  print(f"Address Book 1: {address_book()}\n") #0 argument

  print(f"Address Book 2: \n{address_book('Lan Cal Poly Pomona', 'Kay CSU Fullerton', 'Jane Microsoft')}")

  print(f"Address Book 3: \n{address_book('Long Cal Poly Pomona', 'Bocchi TU', 'Tim Apple', 'Huy CSULB', 'Hitori Google')}") #test data

def main():
  print("Task 1\n")
  task1()

  print("\nTask 2\n")
  task2()

  print("\nTask 3\n")
  task3()

main()

# output task 1

'''
Input string: The quick Brown Fox
No. of Upper case letters: 3
No. of Lower case letters: 13

Input string:
No. of Upper case letters: 0
No. of Lower case letters: 0

Input string: je suis francais
No. of Upper case letters: 0
No. of Lower case letters: 14

Input string: ALLEZ LES BLEUS
No. of Upper case letters: 13
No. of Lower case letters: 0
'''

# output task 2

'''
Original Price: $100
Discount: 20%
Tax Rate: 8%
After Tax Price: $86.4

Original Price: $523
Discount: none
Tax Rate: 9.5%
After Tax Price: $572.68

Original Price: $250
Discount: 35%
Tax Rate: none
After Tax Price: $175.5

Original Price: $210
Discount: 5%
Tax Rate: 9.8%
After Tax Price: $219.05
'''

# output task 3

'''
Address Book 1:

Address Book 2:
Lan Cal Poly Pomona
Kay CSU Fullerton
Jane Microsoft

Address Book 3:
Long Cal Poly Pomona
Bocchi TU
Tim Apple
Huy CSULB
Hitori Google
'''