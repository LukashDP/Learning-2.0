# Напишіть функцію check_even_odd, яка приймає число number і повертає рядок "Even", якщо число парне, і "Odd", якщо число непарне.

def check_even_odd(num1):
    if num1 % 2 == 0:
        return "Even"
    else:
        return "Odd"


our_result = check_even_odd(1)
print(our_result)