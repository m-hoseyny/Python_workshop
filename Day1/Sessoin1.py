# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 08:50:50 2018

@author: microsoft
"""

0, 0j, False, None, {}, [], (), '', "", """"""

if 1 == 2:
    print("True")
else:
    print("false")
   
    
# shart
a = 4
b = 4
if a < b:
    print('avali kochektar az dovomi')
    print('break nazdik ast')
    a = 2 + 2
    b = 6
elif a > b:
    pass
else:
    print("mosavian dg")



# halghe ha

for i in range(10):
    print("Main loop : " + str(i))
    
    for i in range(1, 20, 2):
        print(i)

i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # i = i + 1

# EXp.1

s1 = input("Enter First string : ")
s2 = input("Enter second string : ")
s3 = ''
s4 = ''
s1 = s1.upper()
s2 = s2.upper()

for i in range(min(len(s1), len(s2))):
    if s1[i] <= s2[i]:
        s3 = s3 + s2[i]
        s4 += '2'
    else:
        s3 = s3 + s1[i]
        s4 += '1'
print(s3)

# LIST

l = [6, 2, 10, -2, 20]

for i in l:
    print(i)
    
l2 = [1,2 ,3] + ['a', 'b', 'c']
l2.append(1)
l2.append('r')

l2.pop()
del l2[0]
l2.sort()

l3 = [1, 2, 3]
l4 = [5, 6, 7]
l5 = []
for i in l3:
    for j in l4:
        l5.append([i, j])

## Bubble sort
l_raw = []
n = int(input("Enter Number of Numbers : "))
for i in range(n):
    local_variable = int(input())
    l_raw.append(local_variable)

for j in range(len(l_raw)):
    for i in range(len(l_raw) - 1):
        if l_raw[i] > l_raw[i+1]:
            l_raw[i], l_raw[i+1] = l_raw[i+1], l_raw[i]
print(l_raw)

l_exp = [4, 100, -5, 2.2, 5 + 6j, '1', 'mohammad', 'python', [1,2,3], 3, 5, 10]

l_int = [x for x in l_exp if isinstance(x, str)]
print(l_int)

# Initialize
l11 = [0] * 10
l12 = [0 for i in range(10)]
l13 = [[1, 2, 3]] * 10
l14 = [[1, 2, 3] for i in range(10)]
l15 = [i for i in range(1, 11)]

# tuples 
t1 = (1, 2, 4)
print(t1[0:1])
print(t1*2)
t2 = (3, 4, 5)
print(t1 + t2)

# sets
s1 = {1, 2, 3, 5, 1}
s1.add(7)

s1.add('a')
s1.remove(1)
print('1' in s1)
print(2 in s1)


l_s = list(s1)
s2 = set(l_s)

for s in s1:
    print(s)

# dict
d1 = dict()
    
d1 = {'a':10, 1:20, 'mohammad':"Hosseini", 'class':[1, 2,3]}
d1['UT'] = "University of Tehran"

d1.keys()
d1.values()

value = 10

for key in d1.keys():
    if d1[key] is value:
        print(key)



