#cannot create dict bcz it is a key value pair..rest 3 like liost.tuplke,set are create
'''
l = dict(range(0,8,2))
print(l)
print(type(l))
# list.append()
'''
s = 'Learning Python is very easy'
l=s.split()
print(l)
print(l[0])
print(type(l))

'''to create list we can use 3ways--> by using eval, by using list==>range(), 
by using string-->using split'''

'''Accessing elements of list'''
#By using index:
li = [10,20,30,'pratu','sujata','atul',11,23,15]
print(li[1])
print(li[4])
print(li[8])
print(li[-1])
print(li[1:7:2])
print(li[::-1])
print(li[4:100]) #it will print upto end wont give any error...
print(len(li))
print(li[len(li):0:-1])
#By using slice operator..
print('before added',li)
li[1]='aaru'
print(li)

#By using while loop
n = [0,1,2,3,4,5,6,7,8,9]
i = 0
while i<len(n):
    print(n[i])
    i+=1
n = ['a','b','c']
print(n)
# for index in enumerate(n):
#     print(index)
x = len(n)
for i in range(x):
    print(n[i],'is presnt at positive index',i,'and at -ve index:',i-x)

n = [1,1,2,2,4,5,4,4,2,2]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))
# print(n.index(1))
# print(n.index(2))
# print(n.index(3))
print(n.index(2))
print(2 in n)

li =[]
for list in range(101):
    if list%10==0:
        li.append(list)
print(li)

n =[1,2,3,4]
l=n.insert(3,222)
update_li=l #here we connot assign the value to variable
print(n)   #print updated value
print(update_li)  #none
n.insert(10,999)
n.insert(-10,777)
print(n)

li1 = ['ganesh','ashvin','amol','atul']
li2 = ['pratima','shrita','aarush']
li1.extend(li2)
li2.extend(li1)
print(li2)
print(li1)

order = ['bhurji','pulav','paneer']
order.extend('bhendi')
print(order)

# print(order.pop())
print(order.pop(1))
# order.remove('bhulrji')
print(order)

# empty=[]
# print(empty.pop())
order.reverse()
print(order)
l = [1,5,4,2,3,0]
l.reverse()
print(l)
l.sort()
print(l)
order.sort()
print(order)
order.sort(reverse=True)
print(order)
order.sort(reverse=False)
print(order)

clone = [1,2,3,9,4]
y=clone
print(id(y))
print(id(clone))
y[1]=77
print(y)
print(clone)

import copy
cpy =[1,2,3,9,4]
# p = cpy[:]
p=cpy.copy()
cpy[1]=77
print(id(cpy))
print(id(p))
p[1]=90
print(p)
print(cpy)

p1 =[10,20,19]
p2 = [90,20,40]
concat=p1+p2
print(concat)

repet=p1*2
print(repet)

n = [10,20,[30,50]]
print(n[2][-2])

# nested list as a matrix
n = [[10,20,30],[40,50,60],[70,80,90]]
print(n)
print('elements by rows')
for row in n:
    print(row)
print('elements by matrix')
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()

#list compression
s = [i*i for i in range(1,11)]
print(s)

p = [x for x in s if x%2==0]
print(p)

wrd = ['ashvin','amol','atul','aarush']
l = [i[0:2] for i in wrd]
print(l)

num1 = [10,20,30,40]
num2 = [30,40,70,80]
num3 = [i for i in num1 if i not in num2]
print(num3)
# common elemnt in both
num4 = [i for i in num1 if i in num2]
print(num4)
