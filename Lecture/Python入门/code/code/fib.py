def fiber1(n):
    if n <= 2:
        return 1
    return fiber1(n-1)+fiber1(n-2)

def fiber2(n):
    a = [1]*n
    for i in range(2, n):
        a[i] = a[i-1]+a[i-2]
    return a[n-1]