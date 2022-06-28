import re

str = r"I am the manager of the mailing group Chinese-eHouse@groups.reed.edu, and I wanted to add Satchel Petty (satpetty@reed.edu) as a second admin, as he'll be taking over my position as student coordinator this year."

x = re.compile('@groups.reed.edu', re.I)
y = x.search(str)
print(y)