# task 1
def circle_square(radius):
    return 3.14 * (radius**2)

# task 2

def zip_(list1, list2):
    zip_object = []
    i = 0
    min_len = min([len(list1), len(list2)])
    while i <= min_len - 1:
        zip_object.append((list1[i], list2[i]))
        i += 1
    return zip_object

# task 3
def final_balance(init_sum, interest_rate, years, round_num = 2):
    end_sum = init_sum * ((100 + interest_rate) / 100)**years
    return round(end_sum, ndigits = round_num)

final_balance(1000, 5, 10)
final_balance(700, 7, 10)

# task 4
# много другого кода, который тоже печатает
# ...
# Код коллеги
def print_array(array):
    print("###")
    print(array)
    print("###")

def math_task(data):
    answer = []
    # возводим в третью степень
    for elem in data:
        answer += [elem ** 3]
    print_array(answer)
    # берем остаток от деления на 7
    for i in range(len(answer)):
        answer[i] = answer[i] % 7
    print_array(answer)
    # прибавляем к остатку изначальный массив
    for i in range(len(answer)):
        answer[i] = answer[i] + data[i]
    print_array(answer)
    # возвращаем результат
    return answer

# print(math_task([1, 4, 5, 9])) # пример для самопроверки

# task 5
# то же самое что и task4 только название функции - print_array

# task 6
def sum_as_ints(elems):
    result = 0
    for i in elems:
        try:
            result += int(i)
        except ValueError:
            continue
    return result

# task 7
def reversed_(array):
    rv = []
    while array:
        rv.append(array.pop())
    return rv
arr = [1, 2, 3]
print(arr, reversed_(arr))  # изменяя оригинальный массив, мы не сможем использовать переменные правильно

# task 8
def reversed_(array):
    return array[::-1]

# task 9
string = "string is good"
string.find("string")

def find_substr(substr, str):
    return(str.find(substr), str.find(substr) + len(substr))

# task 10
def fifth_element(some_list: list) -> list:
    return some_list[len(some_list)-5::-5]

# task 11
def process_string(string):
    result = string.lower()[1:]
    return result.replace("intern", "junior")

process_string('IIntern reads a lot of books')


# task 12
def check_string(string):
    copied_string = string
    if string != copied_string.strip():
        result = False
    elif string != copied_string.capitalize():
        result = False
    elif string[-1] != ".":
        result = False
    else:
        result = True
    return result







