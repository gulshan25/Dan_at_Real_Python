# The lambda keyword in Python provides a
# shortcut for declaring small and 
# anonymous functions:

add = lambda x,y: x+y
print(add(5,3))

print('-'*30)

def add(x,y):
    return x+y
print(add(5,5))

print('-'*30)

(lambda x,y: x+y)
print(5+7)
