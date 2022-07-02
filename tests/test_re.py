import re
import time
start_time = time.time()
str = r"I am the manager of the mailing group Chinese-eHouse@groups.reed.edu, and I wanted to add Satchel Petty (satpetty@reed.edu) as a second admin, as he'll be taking over my position as student coordinator this year."

x = re.compile('@groups.reed.edu', re.I)
y = x.search(str)
print(y)
end_time = time.time()

print("Time: ", end_time - start_time)