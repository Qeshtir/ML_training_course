# Here is a conspect file. Most of the blocks are executable on Jupiter NB
# This is not a new conspect. It has additions from ML course to KC_pythonzero
# This file should be (?) refactored as .ipynb conspect

# region 2 Base Info - variables, data types
# разметка - CTRL + ALT + T если есть содержимое
my_name: str = "Igor"  # type hint
my_age: int = 32
my_full_age: float = 32.64
like_Python: bool = True
type(like_Python)  # определение типа переменной

if like_Python:  # Это аналогично like_Python == True
    print(my_name, my_age)

# Инвертирование if
if not like_Python:
    pass
else:
    print(my_name, my_age)

# Пример задачи - объявить переменные
cat_name = "xOxO"
cat_age = 5
is_fluffy = True
print(cat_name, cat_age, is_fluffy)  # Проверка

# Ключевые слова Python
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# Арифметические операции
# - — вычитание
# * — умножение
# ** — возведение в степень
# / — деление
# // — целочисленное деление, арифметическая операция, результатом которой
# является целая часть частного, полученного делением одного целого числа на
# другое целое число
# % — остаток от деления

# из целого числа в строку
a = 42  # целое число 42
str(a)  # получаем строку '42'

# из строки в целое число
a = '42'
b = int(a)  # получаем 42

# из дробного числа в целое
a = 3.5
b = int(a)  # получаем 3

# из логического типа в число
a = True
b = int(a)  # получаем 1

# и наоборот
a = 1
b = bool(a)  # получаем True

my_bool = 3 > 2  # True
my_bool1 = 3 < -5  # False
my_bool2 = 5 != 6  # пять не равно шести, это правда, поэтому здесь получаем True
my_bool3 = 10 == 10  # True
my_bool4 = ('el' in 'hello')  # True
my_bool5 = (3 < 5 ^ 3 < 4)  # True (xor)

a = 5
b = 10
c = 15
print(a < b and b < c)  # вернет True, оба условия выполнились
print(a < b and b > c)  # вернет False, одно уcловие не выполнилось

age = 17
print(age < 18 or age > 60)  # вернет True, первое уcловие выполнилось
print(age < 16 or age > 60)  # вернет False, ни одно уcловие не выполнилось

is_admin = True
print(not is_admin)  # вернет False

# calc order () -> not -> and -> or

# endregion

# region 3 Slice, List, Tuple, Set
# Список (list) - упорядоченный набор элементов произвольного типа
# my_list = [1, 2, 3, "String", 1/2, False]

student_1 = "Anna"
student_2 = "Anastasia"
student_3 = "Alla"

python_students = [student_1, student_2, student_3]

student_4 = "Aglaia"
student_5 = "Anastasia"
student_6 = "Astra"

sql_students = [student_4, student_5, student_6]

# Slices
# использование среза порождает копию

python_students[1]  # Индексация с 0
python_students[0:2]  # Индексация по диапазону. Правая граница не включается
python_students[1:41]  # Что же случится? Правая граница за пределами списка проигнорируется
python_students[:]  # Весь диапазон
python_students[1:]  # Одна граница

my_index = 2
python_students[my_index]  # Индексация через переменные вполне работает
python_students[-1]  # Отрицательная индексация работает от обратного. -1 = последнему элементу.
# Так же получим out of range за границей слева

my_list = list(range(10, 60))  # создать список из 50 элементов от числа до числа
# Tip! range возвращает тип данных - range
my_list[0:10:2]  # шаг индексации, не включая правую границу, если она кратна ему
my_list[10:0:-2]  # индексацию можно перевернуть в лоб
my_list[-1::-2]  # шаг индексации обратно что эквивалентно:
my_list[::-2]  # разворот списка работает только с указанием шага.
my_list[-1:]  # вернет только последний элемент
my_list[-2:-1] # верная обратная индексация

a = [1, 5, 8, 3, 4]
a[3:1:-1]  # учтите, что в квадратных скобках индексы задаются от неразвернутого листа
# тут левый конец больше правого - при обратном порядке это нормально

#Срезы работают над кортежами и строками:
(1, 5 ,9)[1:]
"hello"[:1:-1]

# Значение среза можно сконструировать с помощью функции slice:

first_two = slice(2)
each_odd = slice(None, None, 2)
print(each_odd)  # => slice(None, None, 2)
l = [1, 2, 3, 4, 5]
print(l[first_two])  # => [1, 2]
print(l[each_odd])  # => [1, 3, 5]


# У списка есть функции для работы с ним
python_students.append("Anfisa")  # Добавление в конец. Методы добавляются точкой к имени переменной
python_students.extend(["Angelina", "Athena"])  # Список к концу списка. Работает через переменные типа list
# список не гарантирует уникальности
python_students.insert(0, "Alise")  # Вставить куда и что. Если будем вставлять список этим методом,
# он в элемент вставит список
python_students.pop(0)  # Удалить элемент + вернуть по индексу. По умолчанию (без аргумента) удалит последний
python_students.remove("Alise")  # Удалить первое вхождение элемента по названию. Если значения нет - ошибка.
python_students.reverse()  # разворачивает список
# keyword del
del python_students[2]

# Методы списков
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []

my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # [1, 2, 3]

my_list = [1, 2, 2, 3, 2]
count = my_list.count(2)
print(count)  # 3

my_list = [1, 2, 2, 3, 2]
index = my_list.index(2, 2, 5)
print(index)  # 2

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # [1, 4, 2, 3]

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # [3, 2, 1]

my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # [1, 2, 3]
my_list.sort(reverse=True)
print(my_list)  # [3, 2, 1]

# Полезные функции

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # выведет 5

my_list = [5, 2, 8, 1, 9]
print(max(my_list))  # выведет 9

my_list = [5, 2, 8, 1, 9]
print(min(my_list))  # выведет 1

my_list = [5, 2, 8, 1, 9]
sorted_list = sorted(my_list)
print(sorted_list)  # выведет [1, 2, 5, 8, 9]
sorted_list_descending = sorted(my_list, reverse=True)
print(sorted_list_descending)  # выведет [9, 8, 5, 2, 1]

# Множества (set)
# Игнорирует порядок (сортирует дефолтно) и задают уникальность элементов.
# Элементы могут быть разных типов. Индексация не работает, можно добавлять только неизменяемые объекты
my_set = {1, 1, 2, 3}
empty_set = set() # если указать empty_set = {} получим dict
students_set = set(python_students)
sql_students_set = set(sql_students)
students_set.difference(sql_students_set)  # Верни только тех, кто есть в 1, и нет в 2
students_set.intersection(sql_students_set)  # Верни только тех, кто есть и в 1, и в 2
list(set(python_students))  # хитрая штука - сделать список уникальным и отсортировать его
students_set.add("Afdotia")
students_set.remove("Afdotia")  # Удалить вхождение элемента по названию. Если значения нет - ошибка.
students_set.union(sql_students_set)  # объединение множеств

# Симмтрическая разность (объединение двух разностей)
a = {"a", (1, 2), 3}
b = {3, (1, 2), "unique"}
a.symmetric_difference(b)  # не пересечение (OUTER_JOIN)

a - b  # Разность, вернёт "a". Порядок важен
b - a  # Вернёт "unique"

# Методы множеств

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # выведет set()

fruits = {"apple", "banana", "cherry"}
new_fruits = fruits.copy()
print(new_fruits)  # выведет {'banana', 'cherry', 'apple'}

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # выведет {'cherry', 'apple'}

fruits = {"apple", "banana", "cherry"}
fruits.discard("aaaaaaaa")
print(fruits)  # выведет {'cherry', 'banana', 'apple'}

set1 = {1, 2, 3}
set2 = {4, 5, 6}
disjoint_sets = set1.isdisjoint(set2)  # нет общих элементов
print(disjoint_sets)  # выведет True

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

result = set2.issubset(set1)  # 2 - подмножество 1
print(result)  # выведет True

# Полезные функции

my_set = {1, 1, 2, 2}
print(len(my_set))  # выведет 2

my_set = {5, 2, 8, 1, 9}
print(max(my_set))  # тоже выведет 9

my_set = {5, 2, 8, 1, 9}
print(min(my_set))  # тоже выведет 1

# А вот если отсортировать множество, то получится список!

my_set = {1, 1, 2, 2}
print(sorted(my_set))  # выведет [1, 2]

# концепция изменяемости объектов
# сохраним список в переменную my_list_1
my_list_1 = [3, 1, 2]

# в переменную my_list_2 сохраним список my_list_1
# NB! Это ссылка, а не копия

my_list_2 = my_list_1

# изменим список my_list_1
my_list_1.append(4)
my_list_1.sort()
my_list_1[0] = 100

# посмотрим на оба списка
print(my_list_1)  # => [100, 2, 3, 4]
print(my_list_2)  # => [100, 2, 3, 4]

# Работа с копией. Сохраним список в переменную my_list_1
my_list_1 = [3, 1, 2]

# в переменную my_list_2 сохраним список my_list_1 с методом copy()
my_list_2 = my_list_1.copy()

# изменим список my_list_1
my_list_1.append(4)
my_list_1.sort()
my_list_1[0] = 100

# посмотрим на оба списка
print(my_list_1)  # => [100, 2, 3, 4]
print(my_list_2)  # => [3, 2, 1]

# Ужасы документации. Разница между функцией и методом.
my_list = [1, 2, 3, -2]

# так правильно
my_list_ordered = sorted(my_list)  # функция sorted возвращает новый список, не изменяет список my_list
print(my_list_ordered)  # получим [-2, 1, 2, 3]
print(my_list)  # получим [1, 2, 3, -2]

# так неправильно
my_list_ordered = my_list.sort()  # метод sort ничего не возвращает, а только изменяет список my_list
print(my_list_ordered)  # получим None
print(my_list)  # получим [-2, 1, 2, 3]

# Tuple - кортеж, неизменяемый список ().
# Создадим кортеж
months = ('January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October', 'November', 'December')
my_tuple = (1, )  # Кортеж из одного элемента создаётся с помощью незначащей запятой

# попытаемся добавить тринадцатый месяц
months[12] = 'Undecember'

# или изменить второй месяц
months[1] = 'Февраль'

# Кортежи можно складывать - создастся новый кортеж, в который скопируются все значения из левого кортежа, затем -
# из правого
my_tuple + (5, 5)
(5, 5) + my_tuple
# Кортежи в основном используются в тех местах, где нужна эффективность и производительность.
# Кортежи занимают меньше места, чем списки, и обрабатываются быстрее. При этом кортежи,
# так же как и списки, поддерживают индексацию. Например, если мы хотим получить название первого месяца,
# можем использовать уже привычную запись:
month_index = 0
month_name = months[month_index]
print(month_name)  # => 'January'
# tuples are indeed an ordered collection of objects, but they can contain duplicates and unhashable objects,
# and have slice functionality

# Frozenset - неизменяемый аналог множества
my_frozenset = frozenset([1, 2, 3])

# endregion

# region 4 Dictionaries
# Словарь содержит пары ключ-значение.
# Ключи могут быть любого неизменяемого типа данных — числа, строки, кортежи,
# а значения могут быть любого типа данных — числа, строки, списки, словари и т.д
course_info = {"course_name": "Python_intro",
               "teacher": "Tolya",
               "n_lessons": 10,
               "n_students": 10422,
               "school_name": "KarpovCourses"}
# можно обращаться к значению словаря по имени ключа
course_info["n_students"]
# Создание новой пары ключ-значение. Новая пара добавляется на последнее место
course_info["start_date"] = "2023-06-26"
# изменение пары ключ-значение
course_info["teacher"] = "Anatoly"
my_keys = list(course_info.keys())
my_values = list(course_info.values())
my_items = list(course_info.items())
course_info.get("name")  # Если нет совпадений по ключу, не возвращает ничего.

# Внутри можно хранить списки.
course_info = {"course_name": ["Python_intro", "Introduction to Python"],
               "teacher": "Tolya",
               "n_lessons": 10,
               "n_students": 10422,
               "school_name": "KarpovCourses"}
# А тогда по спискам можно и индексировать:
course_info["course_name"][0]

# Внутри можно хранить словари.
course_info = {"course_name": {"en": "Python_intro", "ru": "Introduction to Python"},
               "teacher": "Tolya",
               "n_lessons": 10,
               "n_students": 10422,
               "school_name": "KarpovCourses"}
# А к внутренним словарям можно обращаться по их ключам. А ключи можно класть в переменные, естественно.
course_info["course_name"]["en"]
# Способы создания словарей
empty_dict = dict()
print(empty_dict)  # {}
fruit_dict = dict([('яблоко', 5), ('банан', 3), ('апельсин', 2)])
print(fruit_dict)  # {'яблоко': 5, 'банан': 3, 'апельсин': 2}

keys = ['a', 'b', 'c']
values = 0
my_dict = dict.fromkeys(keys, values)
print(my_dict)  # {'a': 0, 'b': 0, 'c': 0}

# Методы словарей
my_dict = {"one": 1, "two": 2, "three": 3}
print(my_dict.pop("two"))  # Вывод: 2
print(my_dict.pop("four",
                  "Key not found"))  # Вывод: Key not found, т.к. передан второй элемент - что писать, когда ошибка

my_dict = {"one": 1, "two": 2, "three": 3}
my_dict.clear()
print(my_dict)  # Вывод: {}

# Объединяет словарь с другими словарями или ключ-значение парами. Если ключ уже существует, то его значение будет обновлено
my_dict = {"one": 1, "two": 2, "three": 3}
new_dict = {"two": 22, "four": 4}
my_dict.update(new_dict)
print(my_dict)  # Вывод: {'one': 1, 'two': 22, 'three': 3, 'four': 4}

my_dict = {"one": 1, "two": 2, "three": 3}
new_dict = my_dict.copy()
print(new_dict)  # Вывод: {'one': 1, 'two': 2, 'three': 3}

# Возвращает значение по ключу. Если ключ отсутствует, то он будет вставлен в словарь с указанным значением
# (или None, если значение не указано)
my_dict = {"one": 1, "two": 2, "three": 3}
print(my_dict.setdefault("two", 22))  # Вывод: 2
print(my_dict.setdefault("four"))  # Вывод: None
print(my_dict)  # Вывод: {'one': 1, 'two': 2, 'three': 3, 'four': None}

# ZIP
x = [1, 2, 3]
y = ['a', 'b', 'c']

# Используем оператор zip() для объединения элементов из двух списков
result = zip(x, y)

# Преобразуем результат в список
result_list = list(result)

print(result_list)  # [(1, 'a'), (2, 'b'), (3, 'c')]
# Важно отметить, что результат zip() будет иметь длину, равную длине самой короткой из исходных последовательностей.
# Если длины последовательностей отличаются, то лишние элементы будут проигнорированы.
# Оператор zip() может использоваться в таких ситуациях, как итерация по нескольким последовательностям одновременно
# или совмещение элементов из нескольких списках.

# Помните, мы с вами говорили про frozenset? Одна из его полезных особенностей — frozenset можно использовать в
# качестве ключа словаря. Предположим, мы хотим в качестве ключа, хранить сразу пару значений —
# имя пользователя и его возраст.

students_courses = {}
name_age = frozenset(['Anatoly', 32])
students_courses.update({name_age: ['Python', 'C++']})
print(students_courses)  # => {frozenset({32, 'Anatoly'}): ['Python', 'C++']}

# Это один из примеров практического применения frozenset, если мы хотим создать словарь, где сам ключ —
# это массив из нескольких элементов, то frozenset сможет нам помочь. Список или обычный set использовать в качестве
# ключа для словаря не получится.

# endregion

# region 5 Strings
# Строки индексированы
name = "Igor Makarov"
name + " " + "likes Python"
name[::-1]
list(name)  # разобъёт строку на символы
set(name)
name.lower()
name.upper()
name.split(" ")  # разобъёт строку по символам

# Форматирование строк
# Комбинации кавычек
print("course_name 'ame' ")
print('course_name "ame" ')

course_info = {"course_name": {"en": "Introduction to Python", "ru": "Введение в Питон"},
               "teacher": "Tolya",
               "n_lessons": 10,
               "n_students": 10422,
               "school_name": "KarpovCourses",
               "start_date": "2023-06-24"}

user_name = "Nikita Kuzakin"
course_name = course_info["course_name"]["en"]
start_date = course_info["start_date"]
n_lessons = course_info["n_lessons"]

greetings_text = f'''Hi, {user_name}!
Welcome to the course {course_name}!
Course contains {n_lessons} lessons.
The course will start on {start_date}.
'''
# f-строка позволяет в скобки воткнуть выражение
x = 5
print(f"The value of x squared is {x ** 2}")

# Строки являются неизменяемыми объектами. Так неверно:
my_string = "abcde"
my_string[0] = "f"
# Так верно. Работа на основе строки
my_string = "abcde"
new_string = "f" + my_string[1:]
print(new_string)

my_str = "Hello, world!"
my_str.lower()  # вернет нам новую строку, никак не изменит str1

print('hello'.islower())
print('HELLO'.isupper())

my_list = [3, 2, 1]
my_list.append(4)  # ничего не вернет, изменит my_list

# Другой способ форматирования строк:
name = "Алексей"
age = 30
print("Меня зовут {}. Мне {} лет.".format(name, age))
# 0 и 1 это индексы аргументов метода format
print("Мне {1} лет. Меня зовут {0}.".format(name, age))
print("Меня зовут {name}. Мне {age} лет.".format(name='Алексей', age=30))
# Методы строк
string = "hello, world!"
capitalized_string = string.capitalize()
print(capitalized_string)  # "Hello, world!"

# count(substring[, start[, end]]) — возвращает количество вхождений подстроки в строку.
# Необязательные параметры start и end задают диапазон поиска:
string = "brown fox jumps over a lazy dog"
count = string.count("o")
print(count)  # 4

# replace(old, new[, count]) — заменяет все вхождения одной подстроки на другую.
# Необязательный параметр count задает максимальное количество замен:
string = "hello, world!"
new_string = string.replace("world", "there")
print(new_string)  # "hello, there!"

# split([separator[, maxsplit]]) — разбивает строку на список подстрок, разделенных разделителем separator.
# Необязательный параметр maxsplit задает максимальное количество разбиений:
string = "a, b, c, d"
list_of_strings = string.split(", ")
print(list_of_strings)  # ["a", "b", "c", "d"]

# strip([chars]) — удаляет из начала и конца строки указанные символы.
# Если символы не указаны, удаляются все пробельные символы:
string = "   hello, world!   "
new_string = string.strip()
print(new_string)  # "hello, world!"

# join(iterable) — объединяет список строк в одну строку, разделяя их указанным разделителем:
list_of_strings = ["a", "b", "c", "d"]
string = ", ".join(list_of_strings)
print(string)  # "a, b, c, d"

# Строка является коллекцией
"l" in "hello"

name, surname = input().split()
'   После опознания текста много    пробелов     '.strip().split()
# endregion

# region 7 Clauses
# Условия
score_1 = 85
score_2 = 65
threshold = 80
threshold_2 = 60
student_name = "Fedor"
if score_1 > threshold and score_2 > threshold:
    print(f"Student {student_name} has POSTUPIL on faculty of psychology!")
elif score_2 > threshold_2 and score_1 > threshold_2:
    print(f"Student {student_name} waiting in queue on faculty of psychology!")
else:
    print(f"Student {student_name} hasn't POSTUPIL on faculty of psychology!")
print("Here is end of 'if'")

# Пример 1: Проверка, что число является положительным и четным:
number = 8
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even")

# Пример 2: Проверка длины строки и ее первого символа:
string = "Hello, world!"
if len(string) > 0:
    if string[0] == "H":
        print("The string starts with 'H'")

# Зачем это всё?
# Каскадная проверка условий
# Уточнение условий
# Выполнение дополнительных действий

available_products = ['чай', 'кофе', 'сок']

if available_products:
    print(available_products)

#  Все дело в том, что непустой список интерпретируется как TRUE. Помните, мы уже говорили про приведение типов?
#  Таким образом, если после IF написано что-то, что не является TRUE или FALSE, программа попытается перевести это
#  в логический тип и результат приведения использовать для выполнения условия.
#  Пустые значения интерпретируются как False. Работает приведение типов.

# Тернарный оператор
x = 4
result = "четное" if x % 2 == 0 else "нечетное"
print(f"x - {result}")

# endregion

# region 8 Cycles
my_list = [4, 8, 10, 24, 76]
my_list_2 = []
for i in my_list:
    new_element = i - 1
    my_list_2.append(new_element)
    print(my_list_2)

my_list = [4, 8, 10, 24, 76]
my_list_2 = []
for i in my_list:
    if i > 10:
        my_list_2.append(i + 1)
    else:
        my_list_2.append(i - 1)
    print(my_list_2)

# распаковка списка
my_list = [[4, 8], [10, 24], [76, 1, 10]]
my_list_2 = []
for inner_list in my_list:
    for i in inner_list:
        my_list_2.append(i)

# Цикл в связке со строкой работает посимвольно
for a in my_name:
    if a == 'o':
        print("I found O!")
# Словарь итерируется по ключу
my_dict = {"courses": "Python", "n_lessons": 122}
for dict_key in my_dict:
    dict_val = my_dict[dict_key]
    print((dict_key, dict_val))

for i in my_dict.items():
    print(i)

# Целые числа не поддерживают итерацию. Приведение типов помогает.
a = 123
for i in str(a):
    print(i)
# List comprehension в Python — это компактный способ создания нового списка на основе существующего списка или другой
# итерируемой последовательности, например, строки. Он позволяет более элегантно и кратко написать код, делая его более
# читаемым и эффективным.
# expression  # выражение, которое будет применяться к каждому элементу исходного списка или последовательности - item -
# переменная, представляющая текущий элемент итерируемой последовательности;
# iterable  # исходный список или другая итерируемая последовательность;
# condition  # (необязательно) — условие, по которому будет фильтроваться исходная последовательность.
# new_list = [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
words = ["hello", "world", "python", "list"]
word_lengths = [len(word) for word in words]

# Найти строку с ключевой буквой и индекс этого элемента
my_list = ["abc", "fjd", "ijd", "rte", "dfp", "ytrf"]
target_letter = "p"
string_info = {}

# enumerate показывает номер итерации
for i, d in enumerate(my_list):
    print(i, d)
    if target_letter not in d:
        continue
    else:
        string_info[d] = i
        break

a = [4, 8, 10, 24, 76]
list(enumerate(a))

for n, i in enumerate(a):
    if i < 10:
        continue
    print(n, i)

# Распаковка списка заказов с помощью enumerate
orders = [
    {"номер": "001", "клиент": "John", "дата": "2022-01-01", "статус": "в обработке"},
    {"номер": "002", "клиент": "Alice", "дата": "2022-01-02", "статус": "выполнен"},
    {"номер": "003", "клиент": "Bob", "дата": "2022-01-03", "статус": "выполнен"},
    {"номер": "004", "клиент": "Eva", "дата": "2022-01-04", "статус": "в обработке"},
]
for index, order in enumerate(orders, start=1):
    print(f"Заказ {index}:")
    for key, value in order.items():
        print(f"{key}: {value}")
    print()

employees = [
    {'name': 'John', 'qualification': 'low'},
    {'name': 'Alice', 'qualification': 'high'},
    {'name': 'Bob', 'qualification': 'medium'},
    {'name': 'Eva', 'qualification': 'low'},
    {'name': 'Mike', 'qualification': 'high'},
    {'name': 'Lisa', 'qualification': 'medium'}
]
found_high_qualification_employee = False
for employee in employees:
    qualification = employee['qualification']
    if qualification == 'low':
        continue  # Пропускаем работника с низкой квалификацией
    elif qualification == 'high':
        found_high_qualification_employee = True
        high_qualification_employee = employee
        break  # Найден работник с высокой квалификацией, прекращаем поиск
if found_high_qualification_employee:
    print("Работник с высокой квалификацией найден!")
    print(high_qualification_employee)
else:
    print("Работник с высокой квалификацией не найден.")

# while
# range(start, stop, step) stop - excludes
my_list = list(range(100))
# cumsum
cumsum = 0
i = 0
while cumsum < 20:
    print(cumsum)
    cumsum = cumsum + my_list[i]
    i += 1

# правильно ли вводит пароль + 3 попытки
password = "secret"
pass_count = 0
while pass_count <= 3:
    users_password = input('Input password:')

    if users_password == password:
        print("Login successful!")
        break
    else:
        print("Password unsuccessful!")
        pass_count += 1
print(f"Login attempts more that {pass_count}")

number = 34624
count = 0
while number % 2 == 0:
    number //= 2
    count += 1
print(f' Остаток от деления {number}, поделили {count} раз')

# Хранение бесконечности
x = float('inf')

# endregion

# region 9 Functions
""" имейте в виду глобальное пространство имён - в функцию передаются переменные из глобального окружения, если они не
определены локально
Как только начинаете писать значения по умолчанию - все последующие аргументы также должны быть по умолчанию."""
def get_perimeter_and_area(a, b = 4, c = 5):
    perimeter = a + b + c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return perimeter, area

x1 = 4
x2 = 5
x3 = 6

perimeter_1, area_1 = get_perimeter_and_area(x1, x2, x3)


x = 10  # глобальная переменная
def some_function():
    global x
    x += 5  # изменение глобальной переменной
    print(x)
some_function()  # Вывод: 15
print(x)  # Вывод: 15

total_orders = 0  # глобальная переменная для хранения общего количества заказов
def make_order(num_items):
    global total_orders
    total_orders += 1
    print(f"Заказ сделан! Всего заказов: {total_orders}. Товаров в заказе: {num_items}")
make_order(5)  # Заказ сделан! Всего заказов: 1. Товаров в заказе: 5
make_order(3)  # Заказ сделан! Всего заказов: 2. Товаров в заказе: 3
print(f"Всего заказов: {total_orders}")  # Вывод: Всего заказов: 2

# лямбда функции

add = lambda x, y: x + y
print(add(5, 3))  # Вывод: 8

numbers = [2, 5, 1, 9, 3, 7]
sorted_numbers = sorted(numbers, key=lambda x: x % 3)
print(sorted_numbers)  # Вывод: [9, 3, 1, 7, 2, 5]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Вывод: [2, 4, 6, 8, 10]

# Неизвестное количество аргументов
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_numbers(1, 2, 3))  # Вывод: 6
print(sum_numbers(4, 5, 6, 7))  # Вывод: 22
# В этом примере функция sum_numbers  принимает произвольное количество позиционных аргументов,
# которые передаются в виде кортежа args. Функция складывает все числа и возвращает их сумму.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name='John', age=25)  # Вывод: name: John, age: 25
print_info(country='USA', occupation='Engineer')  # Вывод: country: USA, occupation: Engineer
# Здесь функция print_info  принимает произвольное количество именованных аргументов, которые передаются в виде
# словаря kwargs. Функция выводит на экран ключи и значения переданных аргументов.

def process_data(*args, **kwargs):
    for num in args:
        print(f"Number: {num}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
process_data(1, 2, 3, name='John', age=25)
# Вывод:
# Number: 1
# Number: 2
# Number: 3
# name: John
# age: 25

""" В этом примере функция process_data  принимает произвольное количество позиционных аргументов и произвольное количество
 именованных аргументов. Функция выводит на экран значения позиционных аргументов, а затем ключи и значения
 именованных аргументов.

 Представьте, что вы разрабатываете систему управления базами данных, где пользователи могут создавать таблицы с
 различным набором столбцов. Вам необходимо реализовать функцию, которая будет сохранять данные в таблицу."""
def save_data(table_name, **columns):
    # Здесь может быть ваш код для сохранения данных в таблицу
    print(f"Data saved to table '{table_name}':")
    for column, value in columns.items():
        print(f"- {column}: {value}")
# Пример использования функции save_data
save_data('students', name='John', age=25, grade='A')
# Вывод:
# Data saved to table 'students':
# - name: John
# - age: 25
# - grade: A
save_data('products', name='Apple', price=1.99)
# Вывод:
# Data saved to table 'products':
# - name: Apple
# - price: 1.99

""" Здесь функция save_data  принимает первым аргументом название таблицы, а затем произвольное количество именованных
 аргументов, которые представляют собой названия столбцов и значения, которые нужно сохранить в таблицу.
 Функция может быть использована для сохранения данных в различные таблицы с разным набором столбцов.
"""

# Call stack
"""
Одна функция в ходе выполнения может вызывать другую функцию. В этом случае выполнение «внешней» функции приостановится,
Python запомнит ее состояние и уйдет выполнять «внутреннюю» функцию. Когда «внутренняя» функция закончит выполняться, 
Python вернется к «внешней» функции и продолжит ее выполнять с того места, где остановился.
"""
def inner_func(m):
    print("считаем а")
    a = m // 2
    a = a * a
    print("возвращаем a")
    return a


def outer_func(num):
    num += 2
    print(num)
    print("входим во внутреннюю функцию")
    k = inner_func(num)  # Приостановка outer_func, запуск inner_func
    print("печатаем k")
    print(k, num)


outer_func(20)

# endregion

# region 10 Exceptions
# В блок try/except лучше всего писать как можно меньше кода

try:
    1 / 0
except ZeroDivisionError:
    print("Zero division")

print("Urgh, all fine... yet")

# Multiple exceptions
a = []  # 1, 0, 1

try:
    # Так как элементов в списке нет, вылетит ошибка
    # Ошибка называется IndexError
    print(a[2])
    print(a[0] / a[1])
except IndexError:
    print('Такого элемента нет')
except ZeroDivisionError:
    print('Где-то делят на 0')

# Useful test
def get_second_element(array):
    try:
        return array[1]
    except IndexError:
        print("### There is no element, printing array values###")
        for i, elem in enumerate(array):
            print(f"### {i}: {elem} ###")
    return None
get_second_element((1, 2))
get_second_element([1])

# endregion

# region 11 Referential Data Model + Memory Model
# append изменяет основной объект
id(5)
hash("5")

def can_purchase(amount, history, limit):
    # Добавим в history покупку
    history.append(amount)
    # Затем просуммируем все элементы в history, сравним с limit и вернем True или False
    return sum(history) <= limit

limit = 100
history = [50, 40]

# Приходит параллельно два запроса на покупки (ни одну еще не совершил по факту)
# Должно разрешить покупку, т.к 90 + 4 <= 100
print(can_purchase(4, history, limit))
# Тоже должно разрешить покупку т.к 90 + 7 <= 100. В реальности же будет 94 + 7, т.е. False
print(can_purchase(7, history, limit))

# делаем копию исходного объекта
def can_purchase(amount, history, limit, do_print=False):
    local_copy = history.copy()  # работаем с копией history
    local_copy.append(amount)
    if do_print:
        print(local_copy)
    return sum(local_copy) <= limit


limit = 100
client_history = [50, 40]

print(can_purchase(4, client_history, limit, do_print=True))  # True
print(can_purchase(7, client_history, limit, do_print=True))  # True

"""
Начать нужно с того, что память компьютера линейна. Это значит, что данные в ней лежат длинным сплошным списком из нулей
и единиц. Никаких двумерных матриц. Но мы уже знаем, что переменная позволяет записать некоторый объект в определенное 
имя, не задумываясь об устройстве памяти. Так мы записали в history список [50, 40]. Мы можем в него добавлять 
элементы, удалять их — и не думать о линейности памяти и ее внутреннем устройстве. Как же этого можно добиться?

При инициализации переменной происходит примерно следующее:

1. В памяти компьютера создается объект (например, наш список). Можно представить, что в этот момент создается ячейка и 
объект кладется в эту ячейку.
2. Данный объект имеет некоторый идентификатор, значение и тип.
3. Где-то еще в памяти компьютера резервируется место под имя переменной, и в него кладется два значения: имя переменной
и адрес в памяти, где должно лежать ее фактическое значение. В адрес памяти кладется фактический адрес созданного 
объекта.
4. Посредством оператора = создается ссылка между переменной и объектом.

Локальные переменные функции удаляются после выполнения функции, память высвобождается. Python ведёт счётчик ссылок на 
Объекты. Как только число ссылок на объект становится равно 0, объект уничтожается.

Существует парадигма - создать и сразу использовать через оператор +. Он не изменяет список, а создаёт новый из элементов
слева + элементов справа. Объект удалится при выходе из функции.
"""
def can_purchase(amount, history, limit):
    return sum(history + [amount]) <= limit

limit = 100
client_history = [50, 40]

print(can_purchase(4, client_history, limit))  # True
print(can_purchase(7, client_history, limit))  # True

# endregion

# region 12 Immutable and mutable objects
"""Неизменяемые типы данных:
Целые числа (int)

Давайте определим переменную x, имеющую значение 10. Встроенный метод id() используется для определения местоположения 
x в памяти, а type() используется для определения типа переменной. Когда мы пытаемся изменить значение x, оно успешно 
изменяется.

Стоит заметить, что адрес памяти тоже изменяется. Так происходит потому, что фактически мы не изменили значение x, а 
создали другой объект с тем же именем x и присвоили ему другое значение.

Строки (str)

То же самое верно и для строкового типа данных. Мы не можем изменить существующую переменную, вместо этого мы должны 
создать новую с тем же именем.

Кортежи (tuple)

Определим кортеж с 4 значениями. Воспользуемся функцией id() для вывода его адреса. Если мы захотим изменить значение 
первого элемента, то получим ошибку TypeError. Это означает, что кортеж не поддерживает присвоение или обновление 
элементов.

(frozenset)
"""

"""Изменяемые типы данных
Списки (list)

Определим список с именем x и добавим в него некоторые значения. После этого обновим список: присвоим новое значение 
элементу с индексом 1. Можем заметить, что операция успешно выполнилась.
"""

x = ['Яблоко', 'Груша', 'Слива']
x[1] = 'Ананас'
x   # выведет ['Яблоко', 'Ананас', 'Слива'] 

"""
Вышеописанные действия являются простым и базовым примером модификации. 

Множества (set)

Словари (dict)
Словари — часто используемый тип данных в Python. Давайте посмотрим на их изменчивость.
Определим словарь под именем dict с тремя ключами и их значениями. Когда мы распечатаем его, отобразится все его 
содержимое. Можно распечатать каждое значение словаря отдельно, а также использовать ключи вместо индексов. 
"""
dict = {'Name':'Алиса', 'Age':27, 'Job':'Senior Python Developer'}
dict
# Получим {'Name': 'Алиса', 'Age': 27, 'Job': 'Senior Python Developer'}
dict['Name'], dict['Age'], dict['Job']
# ('Алиса', 27, 'Senior Python Developer')
"""Давайте изменим какое-нибудь значение в нашем словаре. Например, обновим значение для ключа Name. 
Выведем обновленный словарь. Значение изменилось. При этом сами ключи словаря неизменяемы."""
dict['Name'] = 'Роберт'
dict   # {'Name': 'Роберт', 'Age': 27, 'Job': 'Senior Python Developer'}

"""
Есть еще одна причина, почему неизменяемость важна. Для всех встроенных в Python неизменяемых объектов можно подсчитать 
хэш. Это свойство называется _hashable_, т.е. верно утверждение "tuple is hashable".

Хэш — это некая функция, которая берет на вход объект и считает одно число, причем для разных объектов это число разное.
хэш-функции есть два главных свойства:

1. Она быстро считается.
2. При малейшем изменении объекта значение хэш-функции меняется лавинообразно.

Хэш-функции позволяют организовать быстрый поиск и быстрое обращение по элементу, поэтому их использует «под капотом» 
словарь и множество. Собственно, из-за этого ключом в словаре не может выступать изменяемый объект (например, list) — 
для него нельзя подсчитать хэш. В прошлом уроке это просто проговорили, теперь же мы знаем причину. Хэш автоматически
привязан ко всем стандартным неизменяемым типам данных.

Функция hash() возвращает хеш-значение объекта, если оно есть. Хэш-значения являются целыми числами.

hash('1')
-3723884734378080930 # Пример того, какое хэш-значение может иметь объект
"""
# endregion

# region 13 External libs
import datetime as dt
some_time = dt.datetime(2022, 3, 4, 13, 55, 34)
print(some_time)
print(f'Год: {some_time.year}')  # Свойство year объекта some_time
print(f'Месяц: {some_time.month}')
print(f'День: {some_time.day}')
print(f'Час: {some_time.hour}')
print(f'Минута: {some_time.minute}')
print(f'Секунда: {some_time.second}')

"""2022-03-04 13:55:34
Год 2022
Месяц 3
День 4
Час 13
Минута 55
Секунда 34"""

# Библиотека datetime даёт нам возможность проводить арифметические вычисления над датами. timedelta() представляет
# собой разницу между двумя датами или временем.
delta = dt.timedelta(days=0,
                     seconds=0,
                     microseconds=0,
                     milliseconds=0,
                     minutes=0,
                     hours=0,
                     weeks=0)
delta_1 = dt.timedelta(days=60)
#Прибавим 60 дней к дате 2021-03-12
some_date = dt.date(2021, 3, 12) + delta_1
print(some_date)
# output: 2021-05-11

# Если хотим импортировать одну функцию из библиотеки
from collections import defaultdict, Counter

# defaultdict() — это обычный словарь, но при обращении к несуществующему элементу, он не выбрасывает ошибку,
# а создает его.
d = defaultdict(int)  # При отсутствии элемента создаётся 0 (явно передаем название типа). Если объект не найден -
                      # вызови функцию int без аргументов
print(d)
print(d["this key does not exist"])  # int() -> 0, записан по указанному здесь ключу.
print(d)

# defaultdict(<class 'int'>, {})
# 0
# defaultdict(<class 'int'>, {'this key does not exist': 0}) #новый ключик!

array = [1, 3, 'a', 'm', 1, None, 3, 3, ()]

с = {}
for i in array:
    с[i] = array.count(i) # count() — подсчитывает количество экземпляров элемента в списке
print(с)

# Output: {1: 2, 3: 3, 'a': 1, 'm': 1, None: 1, (): 1}

"""Counter() — предназначен для подсчетов количества элементов в последовательности без использования цикла. Counter() 
принимает последовательность и возвращает словарь, где значения — это количества повторений элемента в 
последовательности, а ключи — сами элементы."""

array = [1, 3, 'a', 'm', 1, None, 3, 3, ()]
c = Counter(array)
print(c)

# Output: Counter({3: 3, 1: 2, 'a': 1, 'm': 1, None: 1, (): 1})
"""
Обратите внимание, что Counter — это такой же словарь, как и dict, а значит, ключами в словаре могут быть только 
неизменяемые (хэшируемые) объекты, поэтому на вход в Counter() могут поступать только списки с неизменяемыми объектами.
Соответственно Counter поддерживает все операции над словарём.
"""

import json as j
j.dumps({"a": True})  # принимает на вход словарь, а на выходе выдаёт строку

# pypi.org - repo

# .\имя_окружения\Scripts\activate - вход в venv
# Все пакеты venv устанавливаются отдельно

"""Будьте внимательны, что при вызове jupyter notebook в консоли — Ноутбук будет открываться только с помощью 
системного python. Чтобы это обойти придётся запустить jupyter notebook как модуль 
(перед этим его установив, конечно же)"""

# python -m jupyter notebook (работает и на venv с установленным пакетом)

# endregion

# region 14 Jupyter basics
"""
    esc — выйти из режима редактирования ячейки
    b (как _below_) — создать ячейку внизу с типом code
    a (как _above_) — создать ячейку сверху с типом code
    y — сделать выбранной ячейку (это ячейка, вокруг которой зеленая рамка) тип code
    m (как _markdown_) — сделать выбранной ячейке тип text
    dd (как _delete_, только дважды) — удалить выбранную ячейку
    x — удалить ячейку и сохранить во временную память (не Ctrl + C — у Jupyter на ячейки отдельный буфер обмена)
    c — скопировать ячейку и сохранить во временную память
    v — вставить ячейку из временной памяти под текущей
    V (shift + v) — вставить ячейку из временной памяти над текущей
    Ctrl + Enter — исполнить текущую ячейку
    Shift + Enter — исполнить текущую ячейку и выбрать ячейку ниже
    стрелка вниз — выбрать ячейку ниже
    стрелка вверх — выбрать ячейку выше
    
Магические команды (англ. _magic commands_) — это дополнительная функциональность Jupyter, которая дает возможность менять поведение кода, добавлять подсчеты и чуть-чуть упрощает работу.

Существует два типа магических команд:

    Строчные, обозначенные одним символом %. (Команда работает на одной строке кода)
    Ячеечные, обозначенные двойным символом % %. (Команда работает над всей ячейкой)

Посмотреть доступные магические команды можно с помощью %lsmagic. Возможный результат работы команды:
Available line magics:
%alias  %alias_magic  %autoawait  %autocall  %automagic  %autosave  %bookmark  %cat  %cd  %clear  %colors  %conda
%config  %connect_info  %cp  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history
%killbgscripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart
%logstate  %logstop  %ls  %lsmagic  %lx  %macro  %magic  %man  %matplotlib  %mkdir  %more  %mv  %notebook
%page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %prun  %psearch
%psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset
%reset_selective  %rm  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias
%unload_ext  %who  %who_ls  %whos  %xdel  %xmode

Available cell magics:
%%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown
%%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system
%%time  %%timeit  %%writefile

Automagic is ON, % prefix IS NOT needed for line magics.

%%time
# Cell magic - это магия, которая действует на всю ячейку
# cell magic обязательно должна быть первой строкой в ячейке
for i in range(int(1e6)):
    a = i**2

# Через ! можно сказать jupyter, что всю команду надо выполнить
# в терминале системы (откуда был запущен ноутбук)
# Jupyter поймет, что это не Python код
!pip install notebook

import numpy as np
%timeit np.array([i**2 for i in range(int(1e6))])
Output: 719 ms ± 48.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
Параметры timeit можно настраивать

Autoreload
%load_ext autoreload
%autoreload 2

Команда делает так, чтобы все модули пере-импортировались перед тем, как запускать код.

.pyenv ?

За выполнение кода Python в Jupyter отвечает ядро (англ. _kernel_). Нам здесь нужно знать две вещи: ядро можно менять 
на другое (скажем, то, где больше установленных пакетов) и ядро может зависать.

Ядро содержит в ОЗУ все когда-либо объявленные переменные ноутбука и может «жить» долго. В больших проектах это может 
привести к тому, что ядро станет занимать очень много ОЗУ.

Если вам кажется, что ядро «раздулось», до больших размеров, то его можно перезапустить кнопкой, находящейся справа от 
кнопки прерывания. Перезапуск ядра приведет к тому, что все переменные удалятся и все расчеты потеряются. Будьте готовы.

https://ipython.readthedocs.io/en/stable/interactive/magics.html
"""
# endregion

# region 15 Pandas, Numpy, Matplotlib overview
# Numpy - numeric python
import numpy as np

# Создаем матрицы
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)
# Обычные умножения делаются поэлементно. Немного непривычно для математиков
b = np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]])
print(a * b)
# матричные умножения делаются через np.dot
np.dot(a, b.T)

import pandas as pd  # чаще всего импортируют под именем pd

"""
Библиотека для работы с табличными данными. Подробнее познакомимся в следующем уроке, здесь же пройдемся обзорно.
Основные компоненты pandas – Series и DataFrame.
Series – что-то вроде столбца с данными, DataFrame – это таблица, созданная из столбцов Series.
"""

df = pd.DataFrame([("Python", 6), ("Python", 8), ("ML", 20)],
                  columns=['block', 'lessons'])
print(df)

# Можно фильтровать записи через логические условия
print(df[df['block'] == 'Python'])  # вернёт список индексов, который будет подставлен в DF

# создавать колонки
df["#"] = range(df.shape[0])
print(df)

# продвинуто создавать
result = []
for i in range(1, df.shape[0] + 1):
    result.append(f'course_{i}')
# list comprehension
# df['#'] = [f"course_{i}" for i in range(1, df.shape[0] + 1)]
df['#'] = result
print(df)

# Сгруппировать по колонке "block" и вывести сумму в пределах группы для каждой колонки
# Причём суммирование произойдёт только по числовым колонкам
df.groupby('block').sum()

# Сохраним результат в файл
df.to_csv('1.csv', index=False)  # При это сохранит столбец с нумерацией. При чтении нумерация выведется как
                                            # наименование колонки. Можно удалить колонку индекса при записи.

# Прочитаем файл
df_1 = pd.read_csv('1.csv', index_col=0)  # index_col убьёт колоку с нумерацией
print(df_1)

# %matplotlib inline
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 0.5)
y = x**2

plt.figure(figsize=(16, 9))  # размер графика
plt.plot(x, y)
plt.grid()
plt.title("График $y = x^2$")  # LaTeX
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("1.pdf")

plt.plot((0, 1, 2, 3, 4, 5, 6, 7), (0, 3, 1, 2, 1, 5, 4, 0))
plt.show()

plt.scatter([0, 1, 2, 3, 4 , 5], [0, 1, 2, 3, 4 , 5])
plt.show()

plt.hist([1, 1, 2, 3, 5, 5], bins=50)
plt.grid()

plt.bar([6, 7, 8], [10, 15, 21])
plt.show()
# endregion

# region 16 Pandas
import pandas as pd
d_f = pd.read_csv('.\\01_Python\\Unit_05_Pandas\\train.csv')

d_f.head(7)
d_f.describe()
"""
получить основные статистики таблицы. Возвращает таблицу, где для каждой колонки указаны количество заполненных записей 
(count), а также среднее (mean), стандартное отклонение (std), квантили (25%, 50%, 75%), минимум и максимум 
(min и max соответственно) для каждой колонки с числами.
"""
d_f.columns # имеет срезы d_f.columns[1:5]
# получить список колонок в виде объекта типа Index. Из него можно получать элементы по индексу и брать срезы.
d_f.dtypes
"""
получить типы данных колонок в таблице. Стоит отметить, что в pandas используются свои типы данных, не всегда такие как 
в базовом Python. В частности, строки не выделяются в отдельный тип, а записываются как произвольные объекты 
(тип object). Кроме того, pandas не всегда правильно определяет тип данных в колонке при чтении, поэтому иногда его 
нужно указывать явным образом. Это можно сделать непосредственно при чтении через функцию read_csv()
"""
d_f = pd.read_csv('.\\01_Python\\Unit_05_Pandas\\train.csv', dtype={'season': int})

# Можно фильтровать данные через квадратные скобки
d_f[d_f['workingday'] == 0]  # получить все поездки за выходные

# Этот запрос можно читать как "взять df, где у df поле workingday равно 0"

# Переносы строк внутри [] не играют роли - мы их делаем только для читаемости
d_f[
    (d_f['workingday'] == 1) & (d_f['season'] == 1)
]

# Получим весенние поездки в рабочие дни
"""
Только & в pandas означает логическое "И" – требование, чтобы оба условия выполнились. Обратите внимание, 
в Python для логического "И" в булевых выраженях можно также использовать оператор and.
В pandas так сделать нельзя. Это из-за того, что выражения df['workingday'] == 1 не являются булевыми типами.
Оба условия обернуты в скобки. В pandas так стоит делать всегда, так как без них оператор & будет выполняться 
в неправильном порядке, и код не запустится.
"""

# Либо влажность < 10%, либо температура в Цельсиях строго больше 30
d_f[
    (d_f['humidity'] < 10) | (d_f['temp'] > 30.)
]
# Заметьте, нельзя использовать питоновский or, как и в случае с логическим "И" (оператор &).

"""Логическое "НЕ" делается через символ ~. Точно так же, как в прошлых операторах, встроенный в Python not не подойдет.
Не забудьте про скобки, иначе ~ применится в неправильном порядке,
и мы получим некорректный результат"""
d_f[
    ~(d_f['workingday'] == 0)
]

# Получим все поездки не в выходные

# Когда объединяете "НЕ" с другими условиями, окружите его тоже скобками
d_f[
    (~(d_f['workingday'] == 0)) & (d_f['temp'] >= 10) & (d_f['temp'] < 30)
]
# Не рабочий день и температура от 10 включительно до 30 не включительно
# можно было использовать df['workingday'] != 0

# Взять df, где у df поле windspeed не заполнено
# Этот код не будет работать:
# df[df['windspeed'] is None]

# А этот будет:
d_f[d_f['windspeed'].isna()]

"""
Если мы хотим проверить, что нигде в таблице действительно нет пропусков, можно воспользоваться вспомогательной 
функцией .any(). Она проверяет, состоит ли срез данных целиком из значений False. Функция берёт все данные и смотрит 
их булевый тип. Возвращает True, если хотя бы одна из записей имеет значение True, иначе возвращает False.
"""

# Первый any сворачивает до уровня колонок, второй сворачивает в одно значение
if d_f.isna().any().any():
    print('есть пропуски')
else:
    print('пропусков нет')

# Этот код не будет работать:
# df[df['season'] in [1, 3, 4]]

# А этот будет:
d_f[d_f['season'].isin([1, 3, 4])]

d_f['season'] == 1
"""
Это объект типа Series. Его можно воспринимать как DataFrame с одной колонкой. У Series есть индекс (англ. index) – 
числа слева – и значения, в данном случае, булевые (что можно увидеть как dtype: bool).

Во всех примерах фильтры на самом деле возвращали объект Series, который мы передавали в df[...]. Далее pandas искал 
в Series значения True, запоминал их индекс, а затем в оригинальном датафрейме df забирал значения по этому индексу.

Логические операторы в фильтрах также работали с Series. Например, ~(df['season'] == 1) вернёт Series, аналогичный 
приведённому выше с точностью до наоборот – вместо True будет False, а вместо False – True.

Такое использование Series для логических проверок привело к тому, что встроенные в Python in и not не работают. 
Просто запомните, что вместо df["col1"] in [1, 2, 3] надо использовать df["col1"].isin([1, 2, 3]), 
а вместо not использовать символ ~.
"""

d_f.loc[4]
# Данный запрос вернёт объект Series с колонками, причём строковые названия колонок будут составлять индекс Series.
# К ним можно обращаться как к ключам в словаре:
d_f.loc[4]['temp']

# Сначала создаём копию DataFrame, чтобы иметь возможность
# продолжать работать с оригиналом
df_dt = d_f.copy().set_index('datetime')

# Полученный индекс имеет помимо прочего название (name) - datetime

# Обратиться по порядку, а не непосредственно по индексу можно с помощью .iloc:
d_f.iloc[4]  # Полезно в случае нечисловых индексов

df_dt.loc['2011-01-01 01:00:00', 'weather']  # значение одной колонки
df_dt.iloc[4]['weather']  # аналог на iloc
df_dt.loc['2011-01-01 01:00:00':'2011-01-01 03:00:00']  # краевые элементы входят оба

# Также можно указывать шаг
# df_dt.loc['2011-01-01 01:00:00':'2011-01-01 03:00:00':2]

df_dt.iloc[0:3]  # входит только левая граница

# Также можно указывать шаг
# df_dt.iloc[0:3:2]

# Перезапись значения
df_dt.loc['2011-01-01 04:00:00', 'weather'] = 234
df_dt.iloc[4]['weather']  # iloc возвращает копию слайса из оригинального DF

# Через .iloc это сделать нельзя, pandas выдаст предупреждение, и ничего не произойдёт
# df_dt.iloc[4]['weather'] = -2

# Возвращает копию, НЕ редактирует исходный DataFrame
df_dt.reset_index()

# Модифицирует исходный DataFrame
df_dt.reset_index(inplace=True)  # аргумент позволяет сделать команду в исходном DF (df_dt)

"""
1. Отбираем подмножество по определенному критерию.
2. Над подмножеством применяем функцию, которая вернет одно число (т.е. превратит целое подмножество в одно число).
3. Возвращаемся в п.1, отбираем другое подмножество, повторяем алгоритм.
4. Возвращаем все полученные агрегации.

Такие задачи решаются через группировку данных с последующей агрегацией. В pandas есть все инструменты для их решения.

Допустим, нас попросили посчитать среднюю температуру в разбивке по сезонам.
Для этого надо сгруппировать по сезонам, т.е. сделать 4 подмножества данных - по одному на каждый сезон,
затем каждую группу "схлопнуть" до одного числа - среднего по подмножеству.
Получим 4 числа - по одному среднему на каждую группу.
"""
# Рекомендуется использовать такой способ
d_f.groupby('season').agg({'temp': 'mean'})
# сначала группируем по значению season,
# затем просим из каждой группы взять колонку temp и подсчитать mean - среднее
# mean - это специальная строка, принимает только определенные значения

# доступные функции можно найти здесь
# https://stackoverflow.com/questions/53943319/what-are-all-python-pandas-agg-functions?rq=1

# группировать можно сразу по нескольким параметрам
# так мы подсчитаем среднее для всех колонок
d_f.groupby(['season', 'workingday']).mean()

# а так - только для humidity
d_f.groupby(['season', 'workingday'])['humidity'].mean()
# равнозначный код
# df.groupby(['season', 'workingday']).agg({'humidity': 'mean'})
d_f.groupby(['season', 'workingday']).agg({'humidity': 'mean', 'temp': 'mean'}).reset_index()

"""
В последних двух примерах в полученных объектах DataFrame и Series индекс представлен объектом MultiIndex. 
Работать с ним нетривиально, но его всегда можно сбросить через функцию .reset_index() или передав в функцию .groupby() 
ключ as_index=False.

Функция .groupby() возвращает данные в промежуточном, нечитаемом состоянии. Для того, чтобы с ними работать, 
к ним сначала нужно применить агрегирующую функцию.
"""
d_f.groupby('season', as_index=False).agg({'temp': 'mean'})
d_f.groupby('season').agg({'temp': 'mean'}).reset_index()

# Любой тип (не только datetime.datetime, но и строки, и числа)
# можно преобразовать к pd.datetime
pd.to_datetime(d_f['datetime'])  # после преобразования

# Для начала сохраним результат: создадим копию и в ней превратим колонку в pd.datetime
df_1 = d_f.copy()
df_1['datetime'] = pd.to_datetime(df_1['datetime'])

# Теперь можно вытягивать куски из даты и использовать в фильтрациях и аггрегациях
# Используйте .dt, чтобы вытащить не саму дату, а какую-то ее часть
df_1[df_1['datetime'].dt.month == 5]  # через .dt взяли месяц
# получили данные за пятый месяц

# Можно использовать .dt.month, чтобы сгруппировать по месяцам
df_1.groupby(
    df_1['datetime'].dt.month  # для каждого месяца
).agg({
    'temp': 'mean',  # узнаем среднюю температуру
    "humidity": 'min'  # и минимальную влажность
})  # в разбивке по месяцам

rents_by_week = df_1.groupby(
    df_1['datetime'].dt.isocalendar().week  # для каждой недели в году
).agg({
    'temp': 'count'
})

# sample(10) - это взять 10 случайных записей
# Чтобы была воспроизводимость, фиксируем состояние генератора случайности
rents_by_week.sample(10, random_state=42)
# количество поездок в разбивке по неделям

# самые простой способ - попросить pandas нарисовать, но контроля над картинками будет мало
rents_by_week.plot(
    # названия агрументов приходят из matplotlib.pyplot, см. ниже
    xlabel='Номер недели',
    ylabel='Число поездок',
    title='Количество поездок понедельно',
    grid=True,
    figsize=(16, 9)
)

# Также в pandas есть встроенная функция для постройки гистограмм
df_1['temp'].hist(bins=100, figsize=(16, 9))
# рисуем распределение температур

ax = rents_by_week.hist(bins=100, figsize=(16, 9))
# объект графика возвращается функцией .hist - его можно положить в переменную
# затем добавлять все, что хотим. Добавим title
ax[0, 0].set_title('Гистограмма числа поездок понедельно')

ax = df_1.groupby(
    df_1['datetime'].dt.dayofyear  # группируем по дням
).agg({
    'datetime': 'count'  # считаем количество записей в группе
}).hist(  # строим гистограмму
    bins=100,
    figsize=(16, 9)
)
ax = ax[0, 0]  # matplotlib возвращает двумерный массив, распакуем его
ax.set_title('Гистограмма количества поездок ежедневно')
ax.set_xlabel('Количество поездок')
ax.set_ylabel('Сколько раз было такое количество поездок')

# Через matplotlib.pyplot можно контролировать все аспекты
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
ax.plot(rents_by_week)
# добавим еще точки на тот же график - этого не делали в pandas
ax.scatter(
    # по оси X - индекс. Наша неделя ушла в индекс после группировки
    rents_by_week.index,
    # по оси Y - значение колонки 0. Она называется temp, можно было по имени обратиться
    rents_by_week.iloc[:, 0]
)
ax.set_xlabel('Номер недели')
ax.set_ylabel('Количество поездок')
ax.set_title('Количество поездок понедельно')
ax.grid(True)
# fig.show()  # не сработало

plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
plt.style.use('seaborn')

rents_by_week.to_csv('rents_by_week.csv', sep=';')
# sep - это разделитель. По умолчанию запятая,
# но ";" лучше читается, если открывать файл в русском Excel

# !pip install openpyxl
# Теперь можем писать в excel
# Обратите внимание на engine='openpyxl' - эту библиотеку мы только что установили
rents_by_week.to_excel('rents_by_week.xlsx', engine='openpyxl')
# Полученный файл можно открыть в MS Excel, а можно и в pandas
pd.read_excel('rents_by_week.xlsx', engine='openpyxl').head(5)

# endregion

# region 17 Database basics
"""
База данных (БД) – это организованное хранение информационных ресурсов в виде интегрированной совокупности файлов, 
обеспечивающее удобное взаимодействие между ними и быстрый доступ к данным.

Система управления базами данных или СУБД (англ. Database Management System, сокр. DBMS) — совокупность языковых и 
программных средств, предназначенная для создания, ведения и совместного использования баз данных многими 
пользователями.
"""
"""
Транзакции – операции обработки данных, которые переводят базу из одного состояния в другое. 

Транзакции подчиняются аббревиатуре ACID – атомарность, согласованность, изолированность и стойкость. 

    Атомарность – гарантирует, что никакая транзакция не будет зафиксирована в системе частично
    Согласованность – каждая успешная транзакция по определению фиксирует только допустимые результаты.
    Изолированность – при параллельном выполнении транзакции никак не влияют друг на друга.
    Стойкость – если транзакция выполнена, то результат будет точно сохранен вне зависимости от проблем с оборудованием.
"""

"""
select * from members;
select distinct firstname from members;

SELECT * FROM members
WHERE surname = 'Smith' OR firstname = 'David'; -- '' - строка

SELECT "name", membercost FROM facilities -- "" - упоминание в значении или имени колонки
WHERE membercost IN (0, 5, 10)
LIMIT 10;          -- через LIMIT можно задать количество строк для вывода
"""

"""
SELECT surname, COUNT(surname) 
FROM members 
WHERE recommendedby IS NOT NULL  -- проверка на прочерк, как в Python
GROUP BY surname;

Нельзя в SELECT выбирать колонки, по которым не было группировки в GROUP BY
Ещё одной важной особенностью языка SQL является последовательность выполнения запросов. Так, оператор GROUP BY может
быть использован только после WHERE, а не наоборот. Если нам нужно применить фильтр по уже сгруппированным данным, 
применяется оператор HAVING.

Так не сработает:
SELECT surname, COUNT(surname) 
FROM members
WHERE recommendedby IS NOT NULL AND COUNT(surname) > 1 -- здесь ещё нет агрегации, потому что не было группировки
GROUP BY surname;

А вот так - сработает:
SELECT surname, COUNT(surname) 
FROM members
WHERE recommendedby IS NOT NULL
GROUP BY surname
HAVING COUNT(surname) > 1; -- вот наша фильтрация на агрегат

HAVING может работать с агрегатами колонок, не имеющими агрегации в SELECT
SELECT surname, COUNT(firstname) 
FROM members
WHERE recommendedby IS NOT NULL
GROUP BY surname
HAVING COUNT(surname) > 1;

SQL поддерживает следующие агрегатные функции: 

MIN / MAX - узнать минимальное/максимальное значение по группе
SUM - суммировать все значения в группе
AVG - найти среднее значение по группе
COUNT - посчитать количество элементов группе

Важно отметить, что в отличии от python, в SQL агрегатные функции указываются перед группировкой, сразу после SELECT.
Агрегатные функции могут использоваться и без GROUP BY,  но тогда запрос SELECT не должен содержать простых столбцов 
(кроме как столбцов, служащих аргументами агрегатной функции). 
Результатом вычислений любой агрегатной функции является константное значение, отображаемое в отдельном столбце 
результата.
Аргументу агрегатной функции может предшествовать одно из двух возможных ключевых слов:
ALL -  вычисления выполняются над всеми значениями столбца (значение по умолчанию, указывать не обязательно).
DISTINCT - отбирает только уникальные значения столбца. 

Например, 
SELECT
    COUNT(DISTINCT surname)  --подсчитает число уникальных фамилий в столбце
FROM members;

SELECT COUNT('surname') AS "total_members" --выведет количество участников в колонку с названием total_members
FROM members;

ORDER BY — позволяет сортировать значения при выводе таблицы. По умолчанию сортировка происходит по возрастанию (ASC). 
Для того, чтобы упорядочить значения от большего к меньшему, нужно добавить DESC (англ. descending — убывающий):
SELECT * 
FROM bookings
ORDER BY starttime DESC;


Резюмируя вышесказанное, рассмотрим общую структуру запроса:
SELECT   --столбцы или * для выбора всех столбцов; обязательный запрос
FROM     --таблица; обязательный запрос
WHERE    -- условие/фильтрация; необязательный запрос
GROUP BY --столбец, по которому хотим сгруппировать данные; необязательный запрос
HAVING   --условие/фильтрация на уровне сгруппированных данных; необязательно
ORDER BY --столбец, по которому хотим отсортировать вывод; необязательно
"""

"""
JOIN – одна из наиболее часто используемых команд в SQL-синтаксисе, существующий только в реляционных базах данных. 
Предназначена для соединения двух или более таблиц из базы данных по ключу, который присутствует в обеих таблицах. 
Перед ключом ставится оператор ON.

SELECT f.name, b.starttime
FROM bookings b -- через пробел дали короткое имя (alias) b, чтобы в дальнейшем обращаться более коротким способом
JOIN facilities f on f.facid = b.facid;

SELECT f.name, b.starttime, m.firstname, m.surname
FROM bookings b
JOIN facilities f on f.facid = b.facid
JOIN members m on b.memid = m.memid
WHERE firstname = 'David' AND DATE(b.starttime) > '2010-01-01';


В зависимости от необходимого алгоритма формирования таблицы, к оператору JOIN можно подставлять ключевые слова: 
INNER, CROSS,FULL, LEFT, RIGHT. По умолчанию (если нет ключевых слов) используется INNER JOIN.
 
LEFT JOIN

Берет все данные из FROM, затем берутся соответствующе данные (не все!) в таблице после JOIN. Там, где нет результатов 
в таблице после JOIN, выставляет NULL (символ пропуска значения).

SELECT f.name, b.starttime
FROM bookings b
LEFT JOIN facilities f on f.facid = b.facid; -- Берутся все площадки. Если для какого-нибудь bookings по facid не 
-- найдется площадка в facilities,
-- то f.name будет заполнен NULL
 

RIGHT JOIN

Аналогичен LEFT JOIN, только теперь наоборот: сначала берутся все данные из таблицы в RIGHT JOIN, затем берутся 
соответствующие данные из таблицы в FROM (не все). Там, где нет соответствующих значений в таблице FROM, ставятся NULL:

SELECT f.name, b.starttime
FROM bookings b
RIGHT JOIN facilities f on f.facid = b.facid; -- Берутся все площадки. Если для какого-нибудь facid из facilities не 
-- найдется facid в bookings,
-- то b.starttime будет заполнен NULL.
-- В любом случае будут возвращены все записи из facilites!

INNER JOIN

Выдаст в результате только пересечения обеих таблиц, то есть записи, присутствующие в обеих таблицах. 
По сути представляет собой комбинацию последовательных запросов LEFT JOIN и RIGHT JOIN.

SELECT f.name, b.starttime
FROM bookings b
INNER JOIN facilities f on f.facid = b.facid;-- Возьмутся только те bookings, на которых найдется площадка в 
-- таблице facilities
-- и только те площадки, на которые найдется хотя бы одна запись в bookings.
-- Самый "узкий" из всех JOIN

FULL OUTER JOIN

Самый широкий JOIN. Берет все записи из обеих таблиц. Если нашлось соотвествие, то заполняет колонки, иначе помещает 
туда NULL.

SELECT f.name, b.starttime
FROM bookings b
FULL OUTER JOIN facilities f on f.facid = b.facid;-- Возьмутся все записи из bookings и все записи из facilities.
-- Там, где возможно установить соответствие, оно будет установлено.
-- Где соответствие провести нельзя, будет помещен NULL,
-- причем NULL может уйти как в таблицу слева, так и справа!
-- Самый "широкий" из всех JOIN
"""


import psycopg2

connection = psycopg2.connect(    # connection - это объект, который отвечает за соединение с БД
    database='exercises',         # database - это база данных (именно база, не СУБД)
    host='localhost',             # это говорит, что СУБД работает на моем компьютере
    user='postgres',              # имя пользователя
    password='password'           # пароль
    # port=5432,                  # порт не указываем, по умолчанию 5432
)
cursor = connection.cursor()      # cursor - это объект, который отвечает за взаимодействие с БД
# Делаем запрос
cursor.execute("""                   
SELECT *
FROM cd.bookings -- cd есть схема, bookings есть таблица
-- синтаксис "схема.таблица"
LIMIT 10
""")
results = cursor.fetchall()       # Получаем результаты (fetchall() - "получить всё")
results                           # Это будет стандартный Python-объект. Не очень удобно, но работает

cursor.close()
connection.close()

import pandas as pd

# второй аргумент будет специальная строка. Для PostgreSQL имеет вид:
# postgresql://имя:пароль@хост:порт/база_данных
conn_uri = "postgresql://postgres:password@localhost/exercises"

df = pd.read_sql(
    "SELECT * FROM cd.bookings",             # первый аргумент - SQL запрос
    conn_uri                                     # наша строка с подключением
)
df.head()

df_1 = pd.read_sql(
    """
    SELECT 
      b.starttime,
      b.slots,
      m.firstname,
      m.telephone
    FROM cd.bookings b
    INNER JOIN cd.members m
    ON b.memid = m.memid
    """,
    conn_uri,
    # можно явно указать, в каких колонках даты, их превратят в pd.datetime
    parse_dates=["starttime"]
)
df_1.sample(10, random_state=42) # выведет 10 выбранных случайным образом записей

# Тут все операции осуществляются в блоке SQL:
pd.read_sql(
    """
    SELECT b.starttime, COUNT(m.firstname)
    FROM cd.bookings b
    INNER JOIN cd.members m
    ON b.memid = m.memid
    GROUP BY b.starttime    
    """,
    conn_uri,
    # можно явно указать, в каких колонках даты, их превратят в pd.datetime
    parse_dates=["starttime"])

# А тут мы сначала выгрузили все необходимые данные из БД в формат датафрейма и после применили к ним функцию агрегации:
df_1 = pd.read_sql(
    """
    SELECT 
      b.starttime,
      b.slots,
      m.firstname,
      m.telephone
    FROM cd.bookings b
    INNER JOIN cd.members m
    ON b.memid = m.memid
    """,
    conn_uri,
    parse_dates=["starttime"]
)
df_1.groupby('starttime')['firstname'].count()

# С помощью pandas можно не только читать таблицу, но и записывать данные обратно. Для этого используется функция to_sql:
df.to_sql(
   "new_table",                    # имя таблицы, куда писать данные
    conn_uri,                      # строка для подключения к БД
    schema="cd",                   # Схема, в которой создать таблицу
    if_exists='replace'            # что делать, если уже существует. Одно из трех значений:
   )                               # 'fail' - выдать ошибку
                                   # 'replace' - снести и создать с новыми данными
                                   # 'append' - дополнить датафреймом, не трогая существующие данные

# endregion

# region 18 OOP & Classes
"""
    Объектно-ориентированное программирование (ООП) — методология программирования, основанная на представлении 
    программы в виде совокупности объектов, каждый из которых является экземпляром определённого класса, а классы 
    образуют иерархию наследования.
    
    Класс — определенный программистом прототип программируемого объекта с набором атрибутов (переменных и методов), 
    которые описывают данный объект. Доступ к атрибутам и методам осуществляется через точку.
    
    Переменная класса — переменная, доступная для всех экземпляров данного класса. Определяется внутри класса, но вне 
    любых методов класса.
    
    Абстрактные классы — это классы, которые объявлены, но не содержат реализации. Они не предполагают создание своих 
    объектов, т.е. служат только для того, чтобы хранить общие свойства между другими классами. Абстрактные классы 
    работают как шаблон для подклассов.
    
    Экземпляр класса — отдельный объект-представитель определенного класса.
    
    Переменная экземпляра класса — переменная, определенная внутри метода класса, принадлежащая только к этому классу.
    
    Метод — особая функция, определенная внутри класса.
    
    Наследование — передача атрибутов и методов родительского класса дочерним классам.
    
    Перегрузка функций — изменение работы метода, унаследованного дочерним классом от родительского класса.
    
    Перегрузка операторов — определение работы операторов с экземплярами данного класса.
    
    Инверсия зависимостей — модули верхних уровней не должны импортировать сущности из модулей нижних уровней.
    
    Полиморфизм — возможность обработки разных типов данных (т.е. принадлежащих к разным классам) с помощью «одной и 
    той же» функции, или метода.
    
    Магические методы — базовые методы, которые можно назначить любому классу.
"""
alexeys_car = ('Green', 'Ford', 'Mustang', 'Gasoline')
alexeys_car_2 = ('Blue', 'Volkswagen', 'Golf', 'Diesel')
# car = ('color', 'manufacturer', 'series', 'fuel_type')

# class - Ключевое слово
# Auto - Название класса(записывается в CamelCase(СлитноКаждоеСловоСЗаглавной))
# : - даёт понять python, что дальше идёт блок кода
# @dataclass - упрощает создание класса в нашем случае

from dataclasses import dataclass


@dataclass
class Auto:
    color: str
    manufacturer: str
    series: str
    fuel_type: str

car = Auto('Green', 'Ford', 'Mustang', 'Gasoline')

print(car)

#Output:
#Auto(color='green', manufacturer='Ford', series='Mustang', fuel_type='Gasoline')

# dataclass заменил нам объявление
# функция будет вызываться каждый раз, когда мы попросим создать новый объект.
class AutoShort:
    def __init__(self, color):  # self - сам объект, который будет создан, функция, объявленная внутри класса - метод.
        self.color = color  # создаваемому объекту задаем переменную color

# __init__ — это конструктор класса (метод, который автоматически вызывается при создании объектов),
# он объявляет Python то, как нужно создавать объекты класса.
colored_car = AutoShort('red')
colored_car.color  # наш синтаксис с точкой

# изменяем значение свойства
colored_car.color = 'blue'
colored_car.color

# Класс создаёт своё пространство имён, специальный словарь, в котором хранятся имена переменных и функции с их
# значениями. Определение свойств класса делается с помощью присваивания переменной какого-то значения (внутри класса):
class Car:
	car_color = "Black"


class AutoWithAlarm:
    # через  name: type  можно делать рекомендации типа
    def __init__(self, color, alarm_sound: str):
        self.color = color  # Принимаем объект и записываем в него свойство
        self.alarm_sound = alarm_sound

    # эта функция уйдет в каждый объект класса, он будет уметь ее вызывать
    def alarm(self):
        # внутри этой функции можем обращаться к свойствам объекта
        print(self.alarm_sound)

my_new_car = AutoWithAlarm('red', 'beep-beep-beeeeeep')
print(my_new_car.color)

#Output:
#'red'

print(my_new_car.alarm())

#Output:
#'beep-beep-beeeeeep'

# Посмотреть доступные атрибуты можно с помощью функции dir()
dir(AutoWithAlarm)

"""Output:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'alarm']
"""
"""
Суть наследования сводится к тому, что на базе одного класса (предка) возможно создать другой класс (дочерний), который 
получает все свойства и методы своего родительского класса (или класса-предка или суперкласса или базового класса). 
Вы берёте некоторый класс, забираете у него все поля и методы и строите свой класс на основе предыдущего.
"""


# Очень простое описание авто
class Auto:
    color = ''  # можно заранее создать поля, можно делать в __init__
    name = ''  # в этом примере сделаем и там, и там
    alarm_sound = ''

    def __init__(self, color: str, name: str, alarm_sound: str):
        self.name = name
        self.color = color
        self.alarm_sound = alarm_sound  #

    def beep(self):
        print(self.alarm_sound)


# Мы захотели его расширить: добавить звуковой сигнал
# синтаксис: после имени класса в круглых скобках пишем, от кого наследуемся
class AutoWithAlarm(Auto):
    # добавляем новый функционал
    def alarm(self):
        print('piy-piy')

car_sound = AutoWithAlarm('red', 'Polo', 'bepe')
print(car_sound.alarm())

#Output:
#piy-piy

"""При наследовании надо соблюдать несколько простых правил:

1.    Наследуемый класс (AutoWithAlarm) по логике должен расширять базовый класс, 
    а не перечеркивать его поведение и делать по-своему.
2.    Код должен продолжать работать, если заменить в нем базовый класс на какой-то из его наследников."""

class CarColor:
	color = 'red'
	name = 'Tesla'

class ModelS(CarColor):
	pass  #пропуск

class Cybertruck(CarColor):
	pass

# Есть очень удобная функция isinstance(). Она проверяет, имеет ли конкретный объект какой-то атрибут, который достался
# ему от любого родительского класса в цепочке наследования (иерархии):

cybertruck1 = Cybertruck()
print(isinstance(cybertruck1, CarColor))
#isinstace(проверяемый объект, класс который нужно проверить)
#Output:
#True

# Код выше проверяет, является ли переменная сybertruck1 экземпляром класса CarColor в цепочке наследования. Мы получили
# True, значит CarColor входит в цепочку наследования класса Сybertruck (это  его родительский класс).


# Инверсия зависимостей
# Общий, несколько абстрактный, класс - от него будут наследоваться детали
class GeneralAuto:
    color = ''
    name = ''

# добавляем специфичную функцию, не свойственную всем автомобилям
class AutoTransmissionCar(GeneralAuto):
    def set_position(self, position):
        if position == 'D': # движение вперёд
            print(f'going forward')
        # дальше сложный код по выстановке автоматической трансмиссии

class ManualTransmissionCar(GeneralAuto):
    def set_transmission(self, step):
        if step == 'R':
            print('going backwards')
        # сложный код по переключению передачи

# Перегрузка
class Auto:
    color = ''
    name = ''
    alarm_sound = ''

    def __init__(self, color: str, name: str, alarm_sound: str):
        self.name = name
        self.color = color
        self.alarm_sound = alarm_sound

    def beep(self):
        print(self.alarm_sound)


class AutoWithCustomBeep(Auto):
    # берем и нагло меняем поведение - переопределяем метод родителя
    def beep(self):
        # кстати, можно использовать родительскую версию
        super().beep()
        print('beep broke, sorry')

# Бывают ситуации, когда при переопределении метода в дочерних классах нужно затем передать выполнение обратно в
# родительский:

class Type:
    def __init__(self, car_type):
        self.car_type = car_type

class Car(Type):
    def __init__(self, brand):
        #super().__init__(name)
        self.brand = brand
"""
При такой реализации создать Car возможно только с брендом. Если надо определить еще и тип машины, то можно добавить 
свойство car_type в __init__ (в классе Car), но это бы нарушило принцип DRY (Don’t repeat yourself). Чтобы присвоить 
Car еще и тип нужно передать управление в  __init__ метод родительского класса. Для этого используется функция 
super().функция род.класса
"""

# Полиморфизм
print(1 + 1)
#Output:
#2

print('1'+'1')
#Output:
#'11'


"""Для разных типов данных используется один и тот же оператор сложения и получаются разные результаты (оба операнда 
должны относиться к одному типу). На самом деле, оператор плюс — это синтаксический сахар вызова магического 
метода __add__."""

'1'.__add__('1')
#Output:
#'11'
"""
Полиморфизм в Python — это разное поведение одного и того же метода для разных классов (релевантно, в первую очередь, 
для работы операторов). Возможность создавать один и тот же метод в классе, работающий с данными разного типа. В других 
языках этот пример бы сработал, но не в Python из-за его динамической типизации (он возьмет только лишь последнюю 
реализацию функции).
"""

class NumberPrinter:
    # для int
    def print_number(self, num: int):
        print(f'integer, {num}')

    # для float
    def print_number(self, num: float):
        print(f'float, {num}')


NumberPrinter().print_number(5.5)
NumberPrinter().print_number(5)

"""Output:
float, 5.5
float, 5

# В языке с не динамической типизацией мы бы получили:
Output:
float, 5.5
integer, 5"""

# Magic Methods
class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    # Добавит возможность складывать объекты
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

vec_1 = Vector3D(1, 3, 5)
vec_2 = Vector3D(-5, -3, 1)
sum_vec = vec_1 + vec_2 #Давайте просуммируем вектора
print(sum_vec)

#Output:
#<__main__.Vector3D object at 0x103875160>
# Какой некрасивый вывод

# Ещё есть возможность красиво печатать вектор, с помощью метода __str__, по сути он превращает наш объект в строку
class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # добавит красивую печать
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

class TriangleCalculator:
    def __init__(self, a):
        self.a = a

    # даёт возможность вызвать объект как функцию
    def __call__(self, b):
        return(self.a ** 2 + b ** 2) ** 0.5

calc = TriangleCalculator(a=3)
calc(4)

# Множественное наследование
class Auto:
    def ride(self):
	    print("Едет")
class Airplane:
    def fly(self):
        print("Летит")


class FlyCar(Auto, Airplane):
    pass


a = FlyCar()
a.ride()
a.fly()

"""
Классы-наследники могут использовать родительские методы. Но что, если у нескольких родителей будут одинаковые методы? 
Какой метод в таком случае будет использовать наследник?

Эта ситуация — так называемая проблема ромбовидного наследования (The Diamond Problem). Классический пример:

"""


class A:
    def hello(self):
        print("it`s A")


class B(A):
    def hello(self):
        print("it`s B")


class C(A):
    def hello(self):
        print("it`s C")


class D(B, C):
    pass

"""
Класс D является дочерним классом классов B и C. Классы B и C являются дочерними классами класса A. 
Давайте вызовем метод hello() у экpемпляра класса D:
"""
s = D()
s.hello()

#Output:
#it`s B

"""
Мы получили надпись "it`s B", потому что он наследует свойство в соответствии с правилами MRO.

В 3-й версии Python интерпретатор будет искать метод hello() в классе B (он указан первым родителем D), если его там нет
— в классе С, потом в классе A и далее по иерархии. Соответственно, порядок, в котором указываются родители класса 
(при множественном наследовании), имеет значение.

В Python можно посмотреть, в каком порядке будут проинспектированы родительские классы при помощи метода класса mro():
"""
D.mro()

#Output:
#[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

"""
В связи с наличием множественного наследования в Python есть идея миксинов (mixin, классы-примеси). Это маленькие 
классы, которые имеют не очень большой функционал и как бы «подмешиваются» к другим классам за счёт того, что они 
тоже становятся родителями этого класса. Идея миксинов предполагает их использование только вместе с другими классами 
(для кастомизации, расширения функционала и т.д).

Предположим, мы программируем класс для автомобиля. Мы хотим, чтобы у нас была возможность слушать музыку в машине. 
Конечно, можно просто добавить метод radio() в класс Car.

class Car:
    def ride(self):
        print("Едет")
 
    def radio(self, song):
        print("Сейчас играет: {} ".format(song))

Но что, если у нас есть еще и телефон или любой другой девайс, с которого мы хотим слушать музыку? 
В таком случае лучше вынести функционал проигрывания музыки в отдельный класс-миксин:
"""
class MusicPlayerMixin:
    def radio(self, song):
        print("Сейчас играет: {}".format(song))
class FlyCar(Auto, Airplane, MusicPlayerMixin):
   pass

a = FlyCar()
a.ride()
a.fly()
a.radio('Mozart - Queen of the Night')

# Output:
# Едет
# Летит
# Сейчас играет: Mozart - Queen of the Night

"""
Целесообразно использовать миксины в ситуации, когда необходимо обеспечить какой-то класс дополнительной
(но не очень важной) функциональностью или когда нужно добавить какую-то конкретную фичу большому количеству 
не связанных «родственными узами» классов.
"""

# Об MRO https://tirinox.ru/mro-python/
# print(Z.mro())
# [<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.A'>, <class '__main__.K2'>, <class '__main__.B'>,
# <class '__main__.K3'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.O'>,
# <class 'object'>]

# сделаем понагляднее вывод, печатая только имена классов со стрелочками:
def print_mro(T):
    print(*[c.__name__ for c in T.mro()], sep=' -> ')

# print_mro(Z)
# Z -> K1 -> A -> K2 -> B -> K3 -> C -> D -> E -> O -> object

# Интерфейс
import time

# Создаем класс с функцией, которую требуется реализовать
class Connectable:
    def connect(self, conn_uri: str):
        raise NotImplemented("you should override this method")

# И наследуемся от нее во всех классах
class PostgresqlConnection(Connectable):
    # теперь мы получили в наследство неисправную функцию
    # надо ее переопределить на исправную версию
    def connect(conn_uri: str):
        print('connecting to postgres')
        time.sleep(3)  # имитируем подключение к postgres :)
        print('connection done')

"""
Класс Connectable в этом случае будет называться интерфейсом. Грубо говоря, интерфейс — это класс, который ничего не 
делает по существу и только дает обязательства на реализацию того или иного метода.

Интерфейсы используются, чтобы напоминать другим разработчикам, какие методы они должны реализовать для нормальной 
работы класса в остальной системе.
"""

# Инкапсуляция
"""
Инкапсуляция — это набор инструментов для управления доступом к данным или методам, которые управляют этими данными. 
Суть инкапсуляции заключается в создании объекта, который содержит в себе некоторые методы для работы с данными, 
при этом во вне объекта реализация методов не выставляется.

На этапе реализации и проработки идеи класса важно подумать: какие данные и методы необходимо скрыть от пользователя, 
чтобы у него не было к ним доступа. Этот процесс сокрытия реализации и называется инкапсуляцией (от In-Capsula). 
Простыми словами, инкапсуляция — это управление способностью пользователя видеть/изменять внутреннее содержимое класса. 
"""
class Auto:
    def __init__(self, manufacturer, series):
        self._series = series
        self._manufacturer = manufacturer
        self.series = f'{self._manufacturer} {self._series}'

# Создадим экземпляр класса
p = Auto('Ford', 'Mustang')
print(p.series)

# Output:
# Ford Mustang
# Свойства _series и _manufacturer являются приватными (т.е их использование вне этого класса не предполагается).




# endregion

# region 19 Git
'''
Полезные команды git
git init
git add
git status
git commit
git config --global core.editor "nano" # Переставить текстовый редактор
git diff --staged # Работает только при наличии добавленных в сэйджинг файлов. Без флага не учитывает untracked файлы
git log --graph 
cat @file@ - вывести содержимое файла в bash
git checkout @hashsum@ - перейти на коммит без использования ветки
git diff <имя одной ветки (от кого)> <имя другой ветки (к кому)> позволяет сравнить изменения между двумя коммитам
git branch <имя ветки> - без имени ветки выведет все ветки
git checkout -b <имя ветки> - Одновременно создать ветку и переключится на неё
git checkout HEAD~1 - перемещение на 1 коммит назад 
git tag
git merge <имя ветки> - мерж будет осуществлён из ветки, откуда укажем в команде, туда где мы стоим HEAD-ом
git merge --abort
git clone <ссылка на репозиторий> - работа с абстракцией Remote
git pull - изменений из удаленного репозитория в локальный репозиторий. Чтобы добавить коммиты из репозитория на сервере 
в локальный репозиторий нужно выполнить команду.
git push - Добавление изменений из локального репозиторий в удаленный репозиторий.
git push --tags - пуш тэгов
fork - клонирование удалённого репозитория себе удалённо на аккаунт.
fetch - предложение внести изменения fork-a обратно в оригинальный репозиторий.
git remote -v - посмотреть удалённый репозиторий
git checkout --track origin/dev  -- локальная копия удалённой ветки dev

Ручная настройка origin
git remote add <name> <url> - <name> = origin
git push --set-upstream origin <branch_name> - первая отправка ветки. Если хотим отправить все ветки:
git push --all

Полезные команды VIM
Insert - редактировать файл
Esc - выйти в окружение с командами из редактирования
Shift + ; - открыть prompt
w - записать файл
q - выйти из VIM
wq - записать и выйти
file - изменение имени файла

> Этапы загрузки репозитория на удаленный сервер

1.     Создание репозитория на github/gitlab
2.     Добавление URL репозитория в remote git remote add <origin> <URL>
3.     Отправка ветки в репозиторий git push --set-upstream origin <имя ветки>
4.     Отправка всех веток в репозиторий git push --all
5.     Отправка тэга в репозиторий git push --tag

'''
# endregion

# region 20 Backend. FastAPI
# all code is in appML.py
# appML.py is a Unit 09 continuous task
# uvicorn app:app --reload
"""
FAST API понимает, что словарь в функции следует преобразовывать в JSON и возвращать в JSON

Dependency Injection - способ прописать заранее объекты, которые необходимы для дальнейшей работы 
(dependencies - зависимости). После этого система (в нашем случае FastAPI) сможет использовать (inject) эти зависимости.
Данный метод позволяет избежать повторения кода.

Для имплементации dependency Injection используется класс Depends(), которому в качестве аргумента передается функция.

from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons
    
    
http://localhost:8000/docs - локальная документация
"""
cursor.fetchone()  # 1 element
cursor.fetchall()  # array
"""result = cursor.fetchall()
    if result == []:
        raise HTTPException(404, "user not found")
    else:
        return result
result = cursor.fetchone()
    if not result:
        raise HTTPException(404, "user not found")
    else:
        return result"""

"""
Функция post/{id}
cursor.fetchone() возвращает dict-объект, который может иметь любые ключи.
PostResponse попытается из этого dict-объект создать объект класса PostResponse, валидируя при этом входные данные (т.е. данные из словаря).
Если ошибок валидации нет, то объект класса создается, затем тут же передается в return у функции-обработчика endpoint.
FastAPI видит, что в return ушел объект из модели pydantic и понимает, что его надо сериализировать в JSON (превратить в JSON).
FastAPI делает сериализацию, работая с провалидированным объектом.
FastAPI возвращает ответ на запрос в формате JSON.
Пользователь получает данные строго в том формате, в каком они описаны в классе PostReponse.
"""

# endregion

# region 21 ORM
'''
См. файлы урока 10
Настрой PYTHONPATH
'''


# endregion

# region 22 Airflow
# Look into Unit_11_Airflow file
"""
В Airflow имеется логическая дата (передается как ds). Она говорит, какую дату обрабатывает конкретный запуск.

Логическая дата не всегда совпадает с датой запуска! В нормальном функционировании Airflow запускает даг после окончания
 логической даты, чтобы убедиться в доступности всех данных.

Например, если даг настроен на ежедневный запуск, то в день 2022-02-12 даг запустится с логической датой 2022-02-11 
(вчера), потому что за 12-ое число данных еще может не быть.

Бывает необходимым передать информацию от одной задачи к другой. В целом, Airflow задуман больше как оркестратор, 
а не полная платформа для контроля исполнения задач. Поэтому Airflow имеет только простой интерфейс передачи данных - 
XCom (сокращенно от Cross Communication). XCom передает данные в формате ключ-значение и предназначен для хранения 
небольших данных (примерно до 1 Гб).

Если вам нужно передавать большие данные между задачами, стоит сохранять их в отдельную от Airflow базу данных, 
либо в некое отдельное хранилище (S3, HDFS и т.п.).

Всё домашнее задание по этому блоку хранится в отдельном локальном проекте, потому не может быть слито сюда из-за 
особенностей удалённого репозитория. См. проект airflow
"""


# endregion

# region 23 Useful things in overall programming
"""
Пример кода с хорошими практиками в локальном проекте PythonBestPractices
1. Фиксируйте версии библиотек.
2. Храните логины и пароли к БД в переменных окружения. Используйте .env файлы и библиотеку dotenv.

def get_db():
    with psycopg2.connect(
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        host="postgres.lab.karpov.courses",
        port=6432,
        database="startml"
    ) as conn:
        return conn
        
        # Очень небезопасно для открытого кода


3. Защититесь от SQL инъекций.
4. Вынесите настройки в конфиг-файлы.
5. Разделяйте проект на файлы, обращайтесь к файлам используя Path.
6. Следите за Pythonpath.
7. Поддерживайте идемпотентность кода.
7.1 Константы называйте заглавными буквами.
"""
# endregion

# region 24 Useful tricks in data analysis
data = pd.read_csv('ks_crashed.csv')

# Заполнить пропуски средним
mean = data['Цель в долларах'].mean()
data['Цель в долларах'].fillna(mean)

# Заполнить пропуски самым популярным классом
popular_category = data['Главная категория'].value_counts().index[0]
data['Главная категория'] = data['Главная категория'].fillna(popular_category)

# Заполнить пропуски новой категорией
data['Валюта'] = data['Валюта'].fillna('Неизвестная валюта')

# Заполнить пропуски, ориентируясь на похожие объекты
grouped_means = data.groupby('Главная категория')['Цель в долларах'].transform("mean")
data['Цель в долларах'] = data['Цель в долларах'].fillna(grouped_means)

from sklearn.feature_extraction.text import TfidfVectorizer

# Зафиттим наши данные в TfidfVectorizer
data = data.dropna()
tfidf = TfidfVectorizer()
tfidf.fit(data['Название'])

### Посмотрим как выглядит наш первый документ (первое описание)
first_document = data['Название'][0]

### Векторизуем данное описание через tf-idf
tfidf.transform([first_document])
tfidf.transform([first_document]).todense()
tfidf.get_feature_names()

### Посмотрим на содержимое этого вектора
df = pd.DataFrame(tfidf.transform([first_document]).T.todense(),
                  index=tfidf.get_feature_names(),
                  columns=['tfidf'])



# endregion

