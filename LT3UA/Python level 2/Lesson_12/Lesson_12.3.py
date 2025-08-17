# Створити список (наприклад такий ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]). За допомогою методу із відео на уроці відсортуйте список за  зростанням довжини слів та зробіть вивід на екран.


list_1 = ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]
list_1.sort(key=len)
print(list_1)