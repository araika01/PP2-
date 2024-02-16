def squares():
    a = int(input())
    b = int(input())
    for i in range(a, b):
        yield i**2
print(list(squares()))