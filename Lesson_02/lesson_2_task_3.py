import math
def square(a):
    return math.ceil(a * a)
side = int(input("Сторона квадрата: "))
print(f"Площаль квадрата: {square(side)}")
