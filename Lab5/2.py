import re
s = str(input())
print(re.findall("ab{2,3}", s)) 