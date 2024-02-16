def div():
    n = int(input())
    i=0
    while i<=n:
        if (i%3==0 and i%4==0):
            yield i
        i+=1
print(list(div()))