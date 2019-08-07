#creation of set

s = {10,20,30,40}
print(s)
print(type(s))

s1 = set()
print(type(s1))

s2 = set(range(5))
print(s2)

#Important functiob of set:

s = {10,20,30,40}
s.add(40)
print(s)

s1 = {19,30,50,20}
l=['prati','shiv','atul',67]
s1.update(l,range(5))
print(s1)

s1.add(10)
print(s1)

# s1.add(10,20,30)  #cannot add more than 1 element..

# s1.update(10,20)

s1.update(range(1,10,2), range(0,10,2))
print(s1)

s = s1.copy()
print(s)

x = {10,20,15,20}

y = x.pop()
print(y)
x.remove(15)
print(x)
# x.remove(10)


x.discard(20)
print(x)
x.clear()
print(x)

x = {10,20,30,40}
y = {30,40,50,60}

print(x.symmetric_difference(y))

s = {2*n for n in range(5)}
print(s)
'''
print('program to eliminate duplicate in the list')
l = eval(input('Enter the list of values:'))
s = set(l)
print(s)

l = eval(input('Enter list of values:'))
l1 = []
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)
'''

w = input('Enter word to search:')
s = set(w)
v = {'a','e','i','o','u'}
d = s.intersection(v)
print(d)
