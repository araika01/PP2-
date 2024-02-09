def spy_game():
    n = int(input())
    nums = []
    code = [0,0,7]
    index = 0
    for i in range(n):
        nums.append(int(input()))
    for m in nums:
        if m == code[index]:
            index+=1
            if index == len(code):
                return True
    return False
if spy_game():
    print("True")
else:
    print("False")