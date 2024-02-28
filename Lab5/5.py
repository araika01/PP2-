import re
s = input()
print(re.findall("a.*?b$", s))