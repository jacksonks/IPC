def palavraFibonacci(n):
    if (n == 0):
        return "a"
    elif (n == 1):
        return "b"
    else:
        return palavraFibonacci(n-1) + palavraFibonacci(n-2)
    

print(palavraFibonacci(6))