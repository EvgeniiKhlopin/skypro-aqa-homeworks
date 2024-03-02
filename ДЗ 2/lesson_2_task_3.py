def square(side : int):
   result = round(side * side)
   return result

n = int(input('Введите сторону квадрата: '))
print(square(n))