import re
s = input()
print(re.findall("[A-Z][A-Z]*", s))