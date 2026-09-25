n = int(input())

def get_mn(n):
    if n < 2:
        return []
    for i in range(2, n+1):
        if n%i==0:
            return [i] + get_mn(int(n/i))




print(get_mn(n))
