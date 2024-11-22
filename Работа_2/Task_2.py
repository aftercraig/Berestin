import math

def triangle_type(a, b, c):
    a, b, c = sorted([a, b, c])
    
    if a + b <= c:
        return "Некорректные стороны треугольника"
    elif a**2 + b**2 == c**2:
        return "Прямоугольный"
    elif a**2 + b**2 > c**2:
        return "Остроугольный"
    else:
        return "Тупоугольный"

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    while True:
        try:
            a = float(input("Введите длину стороны a: "))
            b = float(input("Введите длину стороны b: "))
            c = float(input("Введите длину стороны c: "))

            if a <= 0 or b <= 0 or c <= 0:
                print("Ошибка: стороны треугольника должны быть положительными числами.")
                continue

            triangle_type_name = triangle_type(a, b, c)
            if "Некорректные" in triangle_type_name:
                print(triangle_type_name)
                continue

            area = calculate_area(a, b, c)
            print(f"Вид треугольника: {triangle_type_name}")
            print(f"Площадь треугольника: {area:.2f}")
            break

        except ValueError:
            print("Ошибка: введите числовые значения.")

if __name__ == "__main__":
    main()