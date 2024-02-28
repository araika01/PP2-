import re
s = input()
word = re.findall("[A-Z][a-z]*", s)
print(' '.join((word)))