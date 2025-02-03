Operators

1) Arithmetic Operators 
2) Assignment Operator 
3) Relational Operators 
4) Logical Operators 
5) Bitwise Operators (Most Imp) 
6) Membership Operators 
   a) in 
   b) not in 
7) Identity Operators 
   a) is 
   b) is not

1 Arithmetic Operator
Example:
Addition (+)
a=9
b=8
print(a+b)
17
a=987564
b=45687943
print(a+b)
46675507
Subtraction (-)

c=99
d=4567
print(c-d)
-4468
c=654
d=789
print(d-c)
135

Multiplication (*)

e=7854
f=62
print(e*f)
486948
e=20147
f=74123658
print(f*e)
1493369337726

Division (/)

a=258
b=123
print(a/b)
2.097560975609756
a=799
b=5
print(b/a)
0.006257822277847309

floor Division (//)

a=1599
b=7533
print(a//b)
0
print(b//a)
4

Modulo Division (%)

a=159
b=951
print(a%b)
159
print(b%a)
156

Exponentiation (**)

a=8
b=9
print(a**b)
134217728
print(b**a)
43046721

2 ASSIGNMENT OPERATORS

a+=b
a
12
print(a)
12
a-=3
a
9
print(a)
9
a*=9
a
81
a/=8
a
10.125
a//=7
a
1.0
a**=9
a
1.0
a%=5
a
1.0

3 COMPARISION OPERATORS

a=6
b=8
a<b
True
b>a
True
a<=b
True
b>=a
True
a>=b
False
a!=b
True
a==b
False
a=7
b=7
a==b
True

4 LOGICAL OPERATORS

a=8
b=12
a==b and b==a
False
a<b and b<a
False
a<=b and b>=a
True
a!=b and b>a
True
a==b or a!=b
True
a>b or b>a
True
not
SyntaxError: invalid syntax
not True
False

IDENTIFY OPERATORS

a=5.6
if type (a) is float:
    print("it is float")

    
it is float
if type (a) is not float:
    print("True")
else:
    print("False")

    
False

MEMBERSHIP OPERATORS

a=10,20,30,40,50,60
if 50 in a:
    print(50)

    
50
a=30,40,50,60,90
if 100 not in a:
    print(100)

    
100
if 60 not in a:
    print(60)

BITWISE OPERATORS
AND (&)
a=5
b=8
result=a&b
print(result)
0
OR (|)
a=8
b=4
result=a|b
print(result)
12
XOR (^)
a=9
b=8
result=a^b
print(result)
1
NOT (~)
a=5
result=~a
print(result)
-6
LEFT SHIFT (<<)
a=9
result=a<<1
print(result)
18
RIGHT SHIFT (>>)
a=8
result=a>>1
print(result)
4