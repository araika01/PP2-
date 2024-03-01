def up_low():
    upper=0
    lower=0
    s = input()
    for char in s:
        if char.islower():
            lower+=1
        elif char.isupper():
            upper+=1
        else:
            pass
    return(upper, lower)
print(up_low())