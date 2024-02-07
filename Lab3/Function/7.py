def has_33():
    if(l[i-1]!=3 and l[i]!=3):
        return False
    else:
        return True
    
n = int(input())
l = []
i=0
while i<n:
    l.append(input())
    i+=1
print(has_33(l))