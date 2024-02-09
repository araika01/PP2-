def prime(num):
    if num<2:
        return False
    for i  in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if prime(num)]
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(filter_prime(l))
