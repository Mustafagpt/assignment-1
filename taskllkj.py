Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num1= float(input("enter the first number : ")
...             0
...             
SyntaxError: '(' was never closed
>>> num1= float(input("enter the first number : "))
...             
enter the first number : 
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    num1= float(input("enter the first number : "))
ValueError: could not convert string to float: ''
>>> num2= float(input("enter the second number : "))
...             
enter the second number : 
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    num2= float(input("enter the second number : "))
ValueError: could not convert string to float: ''
>>> print(f"addition : {num1+num2}")
...             
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(f"addition : {num1+num2}")
NameError: name 'num1' is not defined
>>> print(f"addition : {num1 + num2}")
...             
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(f"addition : {num1 + num2}")
NameError: name 'num1' is not defined
>>> print(f"substraction : {num1 + num2}")
...             
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(f"substraction : {num1 + num2}")
NameError: name 'num1' is not defined
>>> 
====================================================== RESTART: C:/Users/ngada/AppData/Local/Programs/Python/Python313/task 1.0.py =====================================================
enter the first number : 78
enter the second number : 98
addition : 176.0
addition : 176.0
substraction : -20.0
