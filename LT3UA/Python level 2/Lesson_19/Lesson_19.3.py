# Напишіть функцію find_max, яка приймає три числа num1, num2, та num3 і повертає найбільше з них.

def find_max(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

print(find_max(5, 10, 7))