d = {}
print(type(0))

b = dict()
d[100]='durga'
d[100]='pratu'
d[100]='mand'
print(d)

d = {100:'durga',300:'pratu',200:'atul'}
print(d[100])
print(d[200])
# print(d[400])

print(400 in d)

'''
rec = {}
n = int(input('enter number of student:'))
i = 1
while i<=n:
    name = input('enter student name:')
    marks = input('enter % marks of student:')
    rec[name]=marks
    i=i+1
# print('Name of student','\t','% of marks')
# for x in rec:
#     print(x,':', rec[x])
'''

d = eval(input('enter dictionary:'))
s = sum(d.values())
print('sum=',s)
