# Here is a conspect file. Most of the blocks are executable on Jupiter NB
# This is not a new conspect. It has additions from ML course to KC_pythonzero

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
