import math

def get_triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Некорректные значения сторон"

    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    try:
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))

        triangle_type = get_triangle_type(a, b, c)
        if "Некорректные" in triangle_type:
            print(triangle_type)
            return

        area = calculate_area(a, b, c)
        print(f"Вид треугольника: {triangle_type}")
        print(f"Площадь треугольника: {area:.2f}")

    except ValueError:
        print("Ошибка: введите числовые значения.")

if __name__ == "__main__":
    main()