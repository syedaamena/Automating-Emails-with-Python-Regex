#Automating Emails with Python & Regex!

#Name
#data of birth [dd-mm-yy]
#mobile xxx-xxx-xxx
#instaid
#email text@gmail.com

import re

#Name
x = True
while x:
  pattern = re.compile(r'^[A-Za-z ]+')
  text = input("Enter Name: ")
  matches = pattern.fullmatch(text)
  if matches != None:
    name = matches.group()
    x = False
  else:
    print("Enter Name in correct format")
print(name)
x = True
while x:
  pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
  dob1 = input("Enter Date of Birth: ")
  matches = pattern.fullmatch(dob1)
  if matches != None:
    dob = matches.group()
    x = False
  else:
    print("Enter DOB in correct format")
print(dob)
x = True
while x:
  pattern = re.compile(r'\d{10}')
#  pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
  phone1 = input("Enter Mobile Number: ")
  matches = pattern.fullmatch(phone1)
  if matches != None:
    phone = matches.group()
    x = False
  else:
    print("Enter Mobile in correct format")
print(phone)
insta = input("Enter Insta Id: ")
print(insta)
x = True
while x:
  pattern = re.compile(r'^[a-zA-Z0-9]*+@gmail.com\Z')
  email1 = input("Enter Email: ")
  matches = pattern.fullmatch(email1)
  if matches != None:
    email = matches.group()
    x = False
  else:
    print("Enter Email in correct format")
print(email)
