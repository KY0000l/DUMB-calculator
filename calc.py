#List of Correct operations
list = [1,2,3,4]
#askes for the users operation of choice
print ("Select an Operation")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
#check if the selected operation is correct
while True:
  operation = int(input())
  if operation not in list:
    print ("not in list")
  else:
    break
if operation == 1:#Addition Operation
  print ("First Number")
  num1 = int(input())
  print ("Number Two")
  num2 =int(input())
  print (num1+num2)
elif operation == 2:#Subtraction Operation
  print ("Number One")
  num1 = int(input())
  print ("Number Two")
  num2 =int(input())
  print (num1-num2)
elif operation == 3:#Multiplication Operation
  print ("Number One")
  num1 = int(input())
  print ("Number Two")
  num2 =int(input())
  print (num1*num2)
elif operation == 4:#Division Operation
  print ("Number One")
  num1 = int(input())
  print ("Number Two")
  num2 =int(input())
  print (num1/num2)
input()