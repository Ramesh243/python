# -*- coding: utf-8 -*-
"""K4_Week1_Programs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fN4_Q2uxAj1icjqS4z4bs9uICi4YGiy-

Roll No: 20131A05K4

---
 Name: PUNNAMARAJU AJAY RAHUL PRASAD

VALUE ERROR
"""

try:
  a = int(input("Enter num1: "))
  b = int(input("Enter num2: "))
  print(a/b)
except ValueError as a:
  print("Value Error is handled")
else:
  print("NO Errors")

"""**INDEX ERROR**"""

try:
  list1 = [26,154,78,43,97,55]
  print(list1[7])
except IndexError:
  print("Index number do not exist. Index Error handled")
else:
  print("NO Errors!")

"""**NAME ERROR**"""

try:
  print(c)
except NameError:
  print("Variable not found. Name Error handled.")
else:
  print("NO Errors")

"""**TYPE ERROR**"""

try:
  num = 5
  print("Value of num is " + num)
except TypeError:
  print("Type Error is handled")
else:
  print("NO Errors")

"""**ZERO DIVISION ERROR**"""

print("ZeroDivErr")
a = int(input("Enter a number: "))
b = int(input("Enter num2: "))
try:
  c = a/b
  print(c)
except ZeroDivisionError:
  print("Zero Division Error is handled")
else:
  print("NO errors")

"""**All Exceptions at once**"""

print("ZeroDivError")
a = int(input("Enter a number: "))
b = int(input("Enter num2: "))
try:
  c = a/b
  print(c)
except ZeroDivisionError:
  print("Zero Division Error is handled")
else:
  print("NO errors")

try:
  list1 = [26,154,78,43,97,55]
  print(list1[7])
except IndexError:
  print("Index Error is handled")
else:
  print("NO Errors!")

try:
  num = 5
  print("Value of num is" + num)
except TypeError:
  print("Type Error is handled")
else:
  print("NO Errors")

try:
  print(c)
except NameError:
  print("Name Error is handled")
else:
  print("NO Errors")

print("Value Error")
try:
  a = int(input("Enter num1: "))
  b = int(input("Enter num2: "))
  print(a/b)
except ValueError as a:
  print("Value Error is handled")
else:
  print("NO Errors")

TAJ= "Tom and Jerry"
try:
  print(Maj)
except NameError:
  print("Name Error is handled")

"""*1st* question (b) - User Defined"""

class Error(Exception):
  pass
class Valuetoosmall(Error):
  pass
class Valuetoobig(Error):
  pass
number=10
while(True):
  try:
    n=int(input("Enter a number: "))
    if n<number:
      raise Valuetoosmall
      break
    if n>number:
      raise Valuetoobig
      break
    if n==number:
      print("You guessed the number correctly")
      break
  except Valuetoosmall:
      print("Value too small")
  except Valuetoobig:
      print("Value is too large")

"""**1st Question - c) Use of Try, Except, else, finally**"""

try:
  a=int(input("Enter a number: "))
  b=int(input("Enter 2nd number: "))
except:
  print("Enter only a number a dude!")
else:
  print(str(a)+str(b))
finally:
  print("_/\_Thank you for paying attention to this _/\_")

"""1st question (d) - Raise an exception"""

try:
  age=int(input("Enter age: "))
  if age<18:
    raise ValueError(Exception)
  else:
    print("You are eligible for voting")
except ValueError:
    print("Age should be greater than 18")