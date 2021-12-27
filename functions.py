'''
functions
--------------------------------

def means define 

def(define) is a syntax

def function_name(parameters):
    """ doc_string """

'''

def welcome():
    """ THis is a document string"""
    
print(welcome.__doc__)

print('-'*30)

def welcome():
    print('Hello, Good Morning.')
    
welcome()

print('-'*30)

''' 
parameter

'''

def welcome1(name):
    print(f'Hello,{name} good morning')
    
welcome1('gulshan')

print('-'*30)

def welcome2():
    """This is a welcome message"""
    
print(welcome2.__doc__)

print('-'*30)

def welcome2(name,msg):
    print(f'Hello,{name} {msg}')

welcome2('gulshan','good evening')
    
print('-'*30)

def welcome3(name1,name2,name3,msg):
    print(f'Hello,{name1} {msg}')
    print(f'Hello,{name2} {msg}')
    print(f'Hello,{name3} {msg}')
    
welcome3('gulshan','rahman','tanny','good evening')

print('-'*30)

def welcome3(name1,name2,name3):
    print(f'Hello,{name1}')
    print(f'Hello,{name2}')
    print(f'Hello,{name3}')
    
welcome3('gulshan','rahman','tanny')

print('-'*30)

def welcome3(name1,name2,name3):
    print(f'Hello,{name1} good morning')
    print(f'Hello,{name2} good morning')
    print(f'Hello,{name3} good morning')
    
welcome3('gulshan','rahman','tanny')
print('-'*30)

import dis 
dis.dis(welcome3)