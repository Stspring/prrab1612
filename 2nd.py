def sum_digits(n):
  if n == 0:
    return 0
  else:
    return (n%10) + sum_digits(n//10)
  
a = (input("Введите число"))
print(sum_digits(a))