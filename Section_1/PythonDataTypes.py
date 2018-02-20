Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> arr = [1,2,3,4,5,6,7]
>>> list_1 = [4,5,6,'Hi','Hey',12.5,True]
>>> type(list_1)
<class 'list'>
>>> list_1[2]
6
>>> tup_1 = (4,5,6,'Hi','Hey',12.5,True)
>>> tup_1[3]
'Hi'
>>> tup_1[0:5]
(4, 5, 6, 'Hi', 'Hey')
>>> list_1[0] = 'Python'
>>> list_1
['Python', 5, 6, 'Hi', 'Hey', 12.5, True]
>>> tup_1[0] = 'Python'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tup_1[0] = 'Python'
TypeError: 'tuple' object does not support item assignment
>>> emp = {'name':'Ram','age':16,'college':'IP'}
>>> emp[1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    emp[1]
KeyError: 1
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp['address'] = 'Rohini'
>>> emp
{'name': 'Ram', 'age': 16, 'college': 'IP', 'address': 'Rohini'}
>>> emp['name']
'Ram'
>>> emp.keys()
dict_keys(['name', 'age', 'college', 'address'])
>>> emp.values()
dict_values(['Ram', 16, 'IP', 'Rohini'])
>>> emp.items()
dict_items([('name', 'Ram'), ('age', 16), ('college', 'IP'), ('address', 'Rohini')])
>>> set_1 = {2,4,6,7,8,9,12}
>>> set_2 = {5,8,9,0,4,2,1,4}
>>> set_1 & set_2
{8, 9, 2, 4}
>>> set_1 | set_2
{0, 1, 2, 4, 5, 6, 7, 8, 9, 12}
>>> set_1.union(set_2)
{0, 1, 2, 4, 5, 6, 7, 8, 9, 12}
>>> set_1 - set_2
{12, 6, 7}
>>> employees = [['ram','HCL','IT'],['shyam','TCS','HR'],['Anuj','Wipro','Data Analyst']]
>>> employees[0]
['ram', 'HCL', 'IT']
>>> employees[1]
['shyam', 'TCS', 'HR']
>>> employees[2]
['Anuj', 'Wipro', 'Data Analyst']
>>> employees[0][0]
'ram'
>>> name,age,salary = 'Ram',23,20000
>>> name
'Ram'
>>> age
23
>>> salary
20000
>>> emp = 'Ram',23,20000
>>> emp
('Ram', 23, 20000)
>>> emp
('Ram', 23, 20000)
>>> name,age,salary = emp
>>> name
'Ram'
>>> age
23
>>> salary
20000
>>> emp = 'Ram',23,20000,'HCL','Rohini'
>>> name,age,salary = emp
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    name,age,salary = emp
ValueError: too many values to unpack (expected 3)
>>> name,*details,salary = emp
>>> name
'Ram'
>>> salary
'Rohini'
>>> details
[23, 20000, 'HCL']
>>> 
