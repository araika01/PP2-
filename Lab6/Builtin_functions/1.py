n = int(input())
nums = []
sum = 1
for i in range(n):
    nums.append(int(input()))
for x in nums:
    sum*=x
print(sum)