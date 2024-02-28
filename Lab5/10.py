import re
def camel():
    s = input()
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(camel())