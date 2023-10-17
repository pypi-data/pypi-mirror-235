def operations (a, b, op):
    if op == '+':
        return a+b
    if op == '-':
        return a-b
    if op == '*':
        return a*b
    if op == '/':
        return a/b
    

def max(a, b):
    if a > b:
        return a
    else: return b

def pow(a, n):
    ans = 1
    for i in range(n):
        ans*=a
    return a

def max_greet():
    print("Hi, pidrila!")

def Matvey():
    print("Legenda")
