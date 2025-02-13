myfamily = ("mother", "father", "sister", "brother", "sister") 
print(myfamily)
print(type(myfamily))
print(myfamily[2], myfamily[4])  
try:
    myfamily.append('me')  
except AttributeError:
    print('We can not use append() for tuples')

try:
    myfamily.pop('brother') 
except AttributeError:
    print('We can not use pop() for tuples')
