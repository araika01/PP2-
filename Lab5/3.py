import re
s = input()
print(re.findall("^[a-z]+_[a-z]+$", s))