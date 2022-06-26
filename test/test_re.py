import re

str = ' | Notes for your first day of work'

x = re.search(r'Welcome to Reed College|Notes for your first day of work', str)
print(x)