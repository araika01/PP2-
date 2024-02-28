import re
s = input()
print(re.findall("[A-Z]{1}+[a-z]+", s))
