# task 1
i = 3

# task 2
name = "Igor"
age = 32
is_student = True
# printing the output
print(name, age, is_student)

# task 3
# total_money # budget
# price # item price
jar_count = total_money // price

# task 4
a = 3
b = 7
c = -10

x_1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x_2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

# task 9
tasks_my = [1, 0]
tasks_friend = [1, 0]
tasks_my.extend(tasks_friend)
tasks_all = tasks_my.copy()

# task 11
# NB - все значения должны быть списки
tasks = {1: ["Полить цветы", "Забрать посылку"],
         0: ["Покормить кота"],
         2: ["Почитать книгу по программированию"],
         3: ["Ответить на письмо двоюродной тети"]}

# task 12
if 0 in tasks:
    print("есть срочные дела")
else:
    print("можно отдохнуть")

# task 13
values = []
for value in tasks:
    values.append(tasks[value])

# task 14
doings = []
for value in tasks:
    for task in tasks[value]:
        doings.append(task)

# task 15
answer = []
for value in tasks:
    for task in tasks[value]:
        if "кот" in task:
            answer.append(task)

# task 16
for value in tasks:
    if value >= 2:
        continue
    else:
        if len(answer) >= 2:
            break
        else:
            for task in tasks[value]:
                if "кот" in task:
                    answer.append(task)

# task 17
tasks = {
    0: ["Покормить кота", "Покормить кота"],
    1: ["Покормить кота", "Забрать посылку"],
    2: ["Покормить кота"],
    3: ["Покормить кота", "Забрать посылку", "Забрать посылку"]
}

# Результат
new_tasks = {
    0: ['Покормить кота'],
    1: ['Покормить кота', 'Забрать посылку']
}

# так принято, поправил условие
# tasks[value] на самом деле возвращает value, а здесь value это по сути key.
for value in tasks:
    if len(tasks[value]) > 1:
        tasks[value] = list(set(tasks[value]))
new_tasks = tasks.copy()

# так принято
for value in tasks:
    tasks[value] = list(set(tasks[value]))
new_tasks = tasks.copy()