'''
Fundamental Data Types
------------------------
In python there are four types of fundamental data types. They are 
1.Int
2.float
3.bool
4.complex

-> In python every data type is a class, to access the variables and to store the data of an physical entity we have to create
for the class. But object can store the data temporarily.

->In python all the fundamental data types are pre defined classes, these predefined are classes are used to allocate memory for
the values.

1) int : int is used to allocate memory space for storing integral values like Whole numbers without any decimal point 5 , -10 , 100 .
2)float : float is used to allocate memory space for storing Numbers with a decimal point or numbers written in exponential form, e.g., 3.14 , -0.001 ).
3)Boolean : In Python, a Boolean is a data type that can have one of two possible values: True or False
4)complex : The complex data type in Python represents complex numbers, which are numbers with both real and imaginary parts
'''

#int examples

_x=9
print(_x,type(_x))


x=10
print(x,type(x))

_x1=65452022
print(_x1,type(_x1))

x = 5454552
print(x,type(x))

x_1=52322622
print(x_1,type(x_1))




#float examples

_x=8.1
print(_x,type(_x))


x=88.5
print(x,type(x))

_x1=8.4785
print(_x1,type(_x))

x = 5.2545622144
print(x,type(x))

x_1=5.36325
print(x_1,type(x_1))

#bool examples

_x=True
print(_x,type(_x))


x=False
print(x,type(x))

_x=True
print(_x,type(_x))

x = False
print(x,type(x))

x_1=True
print(x_1,type(x_1))

#complex examples

_x=5+3j
print(_x,type(_x))


x=2+3j
print(x,type(x))

_x=-9
print(_x,type(_x))

x = 1-9j
print(x,type(x))

x_1=-4j
print(x_1,type(x_1))

x = 4.4e3
print(x,type(x))


# bool#


a= True
b= False
print(a+b)
print(True*False+True)
print(False+2+True+True)
print(True/True)
'''print(True/False)'''
print(2*False)
print(0b1111*True)
print(0b1111-True)