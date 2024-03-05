import time
num = int(input())
t = int(input())
a = t
def root(n, t):
    t/=1000
    time.sleep(t)
    print('Square root of ' + str(n) + ' after ' + str(a) + ' miliseconds is ' + str(n**0.5))
root(num, t)