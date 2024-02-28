import re
def camel():
    s = input()
    return ''.join(x.capitalize() or '_' for x in s.split('_'))
print(camel())