'''
Python Arbitrary Arguments

----------- Loop ---------------

 * means List
 
'''

def welcome1(*name):
    for x in name:
        print(f'hello {x}')
        
welcome1('gulshan','rahman','tanny')
         
print('-'*30)

def welcome2():
    return 'Hello world'

print(welcome2())