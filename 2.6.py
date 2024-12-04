def find_password(n):
    result = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                result.append(f"{i}{j}")
    return ''.join(result)

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    print(f"Пароль для числа {n}: {find_password(n)}")
else:
    print("Число должно быть в диапазоне от 3 до 20!")