# When To Use __repr__ vs __str__?
# Emulate what the std lib does:

import datetime
today = datetime.date.today()

print(str(today))

print('-'*30)

print(repr(today))

print('-'*30)

print(today)



