


 #  0 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

a = int(input("Номер элемента ряда Фибоначчи:"))
print(fibonacci(a))





