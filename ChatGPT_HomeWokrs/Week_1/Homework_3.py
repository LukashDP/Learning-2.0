# var = input("Print your word: ")
# list_3 = list(var)
# var_1 = list_3[::1]
# var_2 = list_3[::-1]
# assert var_1 == var_2, "Разные"
# print(f"{var} Одинаковые")

word = input("Print your word: ")
if word == word[::-1]:
    print(f"{word} - Ok" )
else:
    print(f"{word} - Bad" )