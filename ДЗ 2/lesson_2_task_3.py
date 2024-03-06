import math

def square(side):
    if isinstance(side, float):
        area = math.ceil(side*side)
    elif isinstance(side, int):
        area = side * side
    else:
        raise ValueError("Сторона не является числом.")
    return print(area)

square(10)
square(1.1)