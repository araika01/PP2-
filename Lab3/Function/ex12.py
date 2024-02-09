def histogram():
    n = int(input())
    l  = []
    for i in range(n):
        l.append(int(input()))
    for x in l:
        print("*" * x)
histogram()