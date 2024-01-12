from itertools import chain
test_data = {
    "1": 24,
    "2": 19,
    "3": 10,
    "5": 24,
    #"5.6": 10,
    "6": 10,
    "9": 7,
    "10": 14,
    #"10.5": 6,
    "15": 2,
    "19": 86,
    "24": 5,
    "27": 0,
    "30": 4,
    "31": 11,
    "35": 12,
    "50": 16,
    "56": 11,
    "60": 43,
    "63": 13,
    "65": 3
}

test_for_coin_value = [9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 15, 15, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 30, 30, 30, 30, 31]
test_for_coin_value2 = [1, 3, 4]

intern_value = 85

biggest_list = []
for value in test_data:
    biggest_list.append([int(value)]*test_data[value])
biggest_list = list(chain.from_iterable(biggest_list))
print(biggest_list)

def greedy_coin(s, w_l):
    coins = []
    for x in reversed(w_l):
        coins += [x] * (s // x)
        s %= x
    return coins

def greedy_coin2(s, w_l):
    coins = []
    sum = s
    for x in reversed(w_l):
        if sum < x:
            continue
        coins += [x]
        sum = sum - x

    return coins

def list_former():
    list_of_lists = []
    work_list = biggest_list.copy()
    measure = greedy_coin2(intern_value, work_list)
    while len(work_list) > len(measure):
        list_of_lists.append(measure)
        for elem in measure:
            work_list.remove(elem)
        measure = greedy_coin2(intern_value, work_list)
    return list_of_lists

print(list_former())
print(greedy_coin2(85, test_for_coin_value))
