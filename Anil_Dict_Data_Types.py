DICT DATA TYPES

'Dict' is one of the pre-defined class and treated as Dict Category Data Type =>The purpose of dict data type is that " To Organize / store the data in the form of (Key,Value).In (Key,Value), The values of Key represents Unique and values of Value may or may not be unique. 
In organize / store the data in the object of dict, those (Key,Value) must written with curly braces { }.
On the object dict we can't perform indexing and slicing operation becoz values of key itself acts index.
An object of dict maintains Insertion Order. 

Ex:
a={4:"Anil",17:"Rishi",8:"manu",7:"B"}
print(a,type(a))
{4: 'Anil', 17: 'Rishi', 8: 'manu', 7: 'B'} <class 'dict'>
a[4]="Rithu"
print(a,type(a))
{4: 'Rithu', 17: 'Rishi', 8: 'manu', 7: 'B'} <class 'dict'>
a[17]="Anil"
print(a,type(a))
{4: 'Rithu', 17: 'Anil', 8: 'manu', 7: 'B'} <class 'dict'>

We have two types of dict objects they are 
1.Empty Dict
2.Non-Empty Dict

Empty Dict : An Empty dict does not contain elements and whoser length is 0
Ex:
b={}
print(b,type(b),id(b))
{} <class 'dict'> 2837708520704
b[17]="AR"
b[4]="RA"
b[417]="DR"
b[174]="TA"
print(b,type(b),id(b))
{17: 'AR', 4: 'RA', 417: 'DR', 174: 'TA'} <class 'dict'> 2837708520704
(OR)
b=dict()
print(b,type(b),id(b))
{} <class 'dict'> 2837698165568
b[17]="AR"
b[4]="RA"
b[417]="DR"
b[174]="TA"
print(b,type(b),id(b))
{17: 'AR', 4: 'RA', 417: 'DR', 174: 'TA'} <class 'dict'> 2837698165568


Non-Empty Dict: An non-empty dict  contains any elements and whose length is >0 
Ex:
a={4:"Anil",17:"Rishi",8:"manu",7:"B"}
print(a,type(a))
{4: 'Anil', 17: 'Rishi', 8: 'manu', 7: 'B'} <class 'dict'>
a[4]="Rithu"
print(a,type(a))
{4: 'Rithu', 17: 'Rishi', 8: 'manu', 7: 'B'} <class 'dict'>
a[17]="Anil"
print(a,type(a))
{4: 'Rithu', 17: 'Anil', 8: 'manu', 7: 'B'} <class 'dict'>
(OR)
a={4:"Anil",17:"Rishi",8:"manu",7:"B"}
print(a,type(a),id(a))
{4: 'Anil', 17: 'Rishi', 8: 'manu', 7: 'B'} <class'dict'>3157572548992
a[17]="ma"
print(a,type(a),id(a))
{4: 'Anil', 17: 'ma', 8: 'manu', 7: 'B'} <class 'dict'> 3157572548992

Predefined Functions of Dict

Clear()
This is used for removing all the entires of dict objct. 
Ex:
a={4:"Anil",17:"Rishi",8:"manu",7:"B"}
print(a,type(a),id(a))
{4: 'Anil', 17: 'Rishi', 8: 'manu', 7: 'B'} <class 'dict'> 3157572548992
a.clear()
a
{}

Pop()
This function is used for removing (Key,Value) from dict object by passing Value    of Key.  
If the Value of Key does not exists in dict object then we get KeyError.
Ex:
 a={4:"Anil",17:"Rishi",8:"manu",7:"B"}
print(a)
{4: 'Anil', 17: 'Rishi', 8: 'manu', 7: 'B'}
a.pop(8)
'manu'

Pooitem()
This Function is used for removing the last (Key,Value ) from dict object 
When we call popitem() upon empty dict object then we get KeyError 


Ex:
c={"anil":4,"gopi":5,"shannu":6,"raji":7}
print(c)
{'anil': 4, 'gopi': 5, 'shannu': 6, 'raji': 7}
c.popitem()
('raji', 7)
print(c)
{'anil': 4, 'gopi': 5, 'shannu': 6}
c.popitem()
('shannu', 6)
c.popitem()
('gopi', 5)
c.popitem()
('anil', 4)
c.popitem()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c.popitem()
KeyError: 'popitem(): dictionary is empty'

get()
This function is used for obtaining  value of Value by passing value of Key. 
If the value of Key does not exists then we get None =>

Ex:
b={"anil":4,"gopi":5,"shannu":6,"raji":7}
b.get("anil")
4
b.get("kumar")
print(b.get("kumar"))
None
print(b.get("raji"))
7
c=b.get("gopi")
print(c)
5
c=b.get("shanmukh")
print(c)
None

Keys()
This Function obtains list of keys from non-empty dict object. 
when we call keys() upon empty dict then we get empty list

Ex:
b={"anil":4,"gopi":5,"shannu":6,"raji":7}
b.keys()
dict_keys(['anil', 'gopi', 'shannu', 'raji'])
ar=b.keys()
print(ar)
dict_keys(['anil', 'gopi', 'shannu', 'raji'])
for l in b.keys():
    print(l)

    
anil
gopi
shannu
raji
dict().keys()
dict_keys([])
{}.keys()
dict_keys([])

Values()
 
This Function obtains list of values from non-empty dict object. 
when we call values() upon empty dict then we get empty list 

Ex:
b={"anil":4,"gopi":5,"shannu":6,"raji":7}
print(b)
{'anil': 4, 'gopi': 5, 'shannu': 6, 'raji': 7}
ar=b.values()
print(ar)
dict_values([4, 5, 6, 7])
b.values()
dict_values([4, 5, 6, 7])
for val in b.values():
    print(val)

    
4
5
6
7

Items()
This function obtains all (key,value) from dict object in the form tuple.
When we call items() upon empty dict object then we get empty list.
Ex:
b={"anil":4,"gopi":5,"shannu":6,"raji":7}
b.items()
dict_items([('anil', 4), ('gopi', 5), ('shannu', 6), ('raji', 7)])
ar=b.items()
print(ar)
dict_items([('anil', 4), ('gopi', 5), ('shannu', 6), ('raji', 7)])
for ar in b.items():
    print(ar)

    
('anil', 4)
('gopi', 5)
('shannu', 6)
('raji', 7)

Copy()
This function is used for copying the content of one dict object into another dict object (shallow copy).

Ex:
a={"Apple":35.26,"kiwi":58.24}
print(a,id(a))
{'Apple': 35.26, 'kiwi': 58.24} 2837708520704
a1=a.copy()
print(a1,id(a1))
{'Apple': 35.26, 'kiwi': 58.24} 2837708521280
a1["Sberry"]=26.35
a["Guava"]=50
print(a,id(a))
{'Apple': 35.26, 'kiwi': 58.24, 'Guava': 50} 2837708520704
print(a1,id(a1))
{'Apple': 35.26, 'kiwi': 58.24, 'Sberry': 26.35} 2837708521280

Update()
Ex:
a1={"anil":"python","gopi":"java"}
a2={"shannu":"testing","spandana":"hk"}
a3=a1.update(a2)
print(a1)
{'anil': 'python', 'gopi': 'java', 'shannu': 'testing', 'spandana': 'hk'}
print(a2)
{'shannu': 'testing', 'spandana': 'hk'}
print(a3)
None
a1={"anil":"python","gopi":"java"}
a2={"shannu":"testing","spandana":"hk"}
a1.update(a2)
print(a1)
{'anil': 'python', 'gopi': 'java', 'shannu': 'testing', 'spandana': 'hk'}
print(a2)
{'shannu': 'testing', 'spandana': 'hk'}
