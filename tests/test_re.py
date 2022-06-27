import re

str = 'power point'

x = re.compile('power\s?point', re.I)
y = x.search(str)
print(y)