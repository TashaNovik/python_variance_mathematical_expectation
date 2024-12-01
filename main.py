from typing import Tuple, List
# Расчет математического ожидания и дисперсии в питоне:
# Математическое ожидание
# M[x] = Σ (xᵢ * pᵢ)

#Дисперсия
# D[X] = M[X^2] - (M[X])^2


def get_data_for_calculating() -> tuple[list[float], list[float]]:
    x = []
    p = []
    all_values_from_file = []
    with open('table.txt', 'r') as file:
        for line in file:
            line = line.strip()
            values = line.split(' ')
            values = [float(value.strip()) for value in values]
            all_values_from_file.append(values)

    x = all_values_from_file[0]
    p = all_values_from_file[1]
    return x, p

def check_data(x: list[float], p: list[float]) -> bool:
    """Проверяет корректность входных данных для расчета дисперсии."""

    if len(x) != len(p):
        print("Ошибка: Длины списков значений и вероятностей должны быть одинаковы.")
        return False

    if not all(0 <= pi <= 1 for pi in p):
        print("Ошибка: Вероятности должны быть в диапазоне от 0 до 1.")
        return False

    if not abs(sum(p) - 1) < 1e-9:  # Проверка с учетом погрешности для чисел с плавающей точкой
        print("Ошибка: Сумма вероятностей должна быть равна 1 (с учетом погрешности).")
        return False

    return True  # Данные корректны

if __name__ == '__main__':
    x, p = get_data_for_calculating()
    if check_data(x, p):
        M = sum(x[i] * p[i] for i in range(len(x)))
        D = sum((x[i] - M) ** 2 * p[i] for i in range(len(x)))
        print(f"Математическое ожидание: {M}")
        print(f"Дисперсия: {D}")








