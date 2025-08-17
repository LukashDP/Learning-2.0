# У вас є 77 задач і 13 людей. Ви хочете розподілити задачі порівну між усіма людьми. Напишіть програму, яка визначить, скільки задач отримає кожна людина, і скільки задач залишиться нерозподіленими.

total_tasks = 77
total_persons = 13
tasks_per_person = total_tasks // total_persons
reminder_tasks = total_tasks % total_persons
print(tasks_per_person)
print(reminder_tasks)