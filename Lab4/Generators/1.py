def square():
    n = int(input())
    i=0
    while i<=n:
        yield i**2
        i+=1
print(list(square()))
    