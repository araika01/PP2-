from itertools import permutations
def perms(x):
    list = [''.join(p) for p in permutations(x)]
    return list
s = str(input())
print(perms(s))