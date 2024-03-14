import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r'\b\d+\.\d+\b'
    for pat in re.finditer(pattern, text):
        yield float(pat.group())

def sum_profit(text: str, func: Callable):
    total = sum(func(text))
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


