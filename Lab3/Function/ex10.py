def unique():
    n = int(input())
    dublicated_list = []
    dedublicated_list = []
    j=0
    while j<n:
        dublicated_list.append(input())
        j+=1
    for i in dublicated_list:
        if i not in dedublicated_list:
            dedublicated_list.append(i) 
    print(dedublicated_list)
unique()     