'''
#For Loop
for letters in 'Namara':
    print (letters)

#range
x=list(range(10))
y=list(range(2,10))
z=list(range(2,10,3))
------
for x in range (1,11):
    print(x)
--------------
#Multiblication Using for
for x in range(1,11):
    print("----------------")
    for y in range(1,11):
        print(f'{x} x {y} = {x*y}')
x=int( input('Enter Number: ' ))
for y in range(1,x+1):
    print(y)

----------

#Control statment
for x in range (1,10):
    if x==4:
        break
    print(x)
print("Welcome")
for y in range (1,10):
    if y==4:
        continue
    print(y)
print("Welcome")
'''

