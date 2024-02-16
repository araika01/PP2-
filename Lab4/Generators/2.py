def even():
    n = int(input())
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i=i+1
print(list(even()))