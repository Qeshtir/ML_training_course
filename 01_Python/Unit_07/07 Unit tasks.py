# task 1
class Triangle:
    n_dots = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

tr_1 = Triangle(1, 2, 3)
tr_2 = Triangle(3, 4, 5)

# task 2
class Triangle:
    n_dots = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c) * 0.5
        if (a < b + c):
            if (b < a + c):
                if (c < b + a):
                    pass
                else:
                    raise ValueError("triangle inequality does not hold")
            else:
                raise ValueError("triangle inequality does not hold")
        else:
            raise ValueError("triangle inequality does not hold")
    def area(self):

        return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5

tr_1 = Triangle(3, 4, 5)
tr_2 = Triangle(1, 2, 3)
square_1 = tr_1.area()
square_2 = tr_2.area()

# task 3
class Rectangle (Triangle):
    n_dots = 4
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

# task 4

class BaseFigure:
    n_dots = None
    def area(self):
        raise NotImplementedError
    def validate(self):
        raise NotImplementedError
    def __init__(self):
        self.validate()

# task 5
class Triangle(BaseFigure):
    n_dots = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c) * 0.5
        super().__init__()
    def area(self):
        return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5
    def validate(self):
        if (self.a < self.b + self.c):
            if (self.b < self.a + self.c):
                if (self.c < self.b + self.a):
                    return self.a, self.b, self.c
                else:
                    raise ValueError("triangle inequality does not hold")
            else:
                raise ValueError("triangle inequality does not hold")
        else:
            raise ValueError("triangle inequality does not hold")

class Rectangle (BaseFigure):
    n_dots = 4
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()
    def area(self):
        return self.a * self.b
    def validate(self):
        return self.a, self.b

# task 6
class Circle (BaseFigure):
    n_dots = float('inf')
    def __init__(self, r):
        self.r = r
        super().__init__()
    def area(self):
        return 3.14 * (self.r ** 2)
    def validate(self):
        pass

# task 7
class Vector:
    def __init__(self, a):
        self.coords = a
    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
        else:
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] + other.coords[i])
            return Vector(result)

# Будет работать
Vector([1, 2, 3]) + Vector([2, 3, 4]) # даст Vector([3, 5, 7])

# НЕ будет работать
Vector([1, 2]) + Vector([1, 2, 3])  # нельзя складывать векторы разной длины
# Должно возвращать ошибку (сообщение тоже!)
# ValueError: left and right lengths differ: 2 != 3

# task 8
class Vector:
    def __init__(self, a):
        self.coords = a
    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
        else:
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] + other.coords[i])
            return Vector(result)
    def __str__(self):
        return f'{self.coords}'

# task 9
class Vector:
    def __init__(self, a):
        self.coords = a
    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
        else:
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] + other.coords[i])
            return Vector(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] * other)
            return Vector(result)
        elif isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
            else:
                result = []
                for i in range(len(self.coords)):
                    result.append(self.coords[i] * other.coords[i])
                return sum(result)

    def __str__(self):
        return f'{self.coords}'

# task 10
class Vector:
    def __init__(self, a):
        self.coords = a
    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
        else:
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] + other.coords[i])
            return Vector(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] * other)
            return Vector(result)
        else:
            if len(self.coords) != len(other.coords):
                raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
            else:
                result = []
                for i in range(len(self.coords)):
                    result.append(self.coords[i] * other.coords[i])
                return Vector(sum(result))

    def __abs__(self):
        if isinstance(self, Vector):
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] ** 2)
            return sum(result) ** 0.5

    def __eq__(self, other):
        if isinstance(self, Vector):
            if isinstance(other, Vector):
                return self.coords == other.coords
            else:
                pass
        else:
            pass
    def __str__(self):
        return f'{self.coords}'

# task 11
class ParsesCookies:

    def cookies(self):
        return self.request['cookies']
    def is_authed(self):
        return 'auth_key' in self.request['cookies']

class ParsesBody:

    def body(self):
        return self.request['body']
class ParsesHeaders:

    def headers(self):
        return self.request['headers']
    def need_json(self):
        return self.request['headers'].get('content-type') == 'application/json'

"""
# Для проверки вставь инит

class ParsesCookies:
    def __init__(self, a):
        self.request = a
    def cookies(self):
        return self.request['cookies']
    def is_authed(self):
        return 'auth_key' in self.request['cookies']

class ParsesBody:
    def __init__(self, a):
        self.request = a
    def body(self):
        return self.request['body']
class ParsesHeaders:
    def __init__(self, a):
        self.request = a
    def headers(self):
        return self.request['headers']
    def need_json(self):
        return self.request['headers'].get('content-type') == 'application/json'


# будет приходить запрос в виде словаря
request = {
  "cookies": {'key_1': 'value_1', 'auth_key': 'auth_key'},
  "body": "a long time ago, in a Galaxy far, far away",
  "headers": {"content-type": "application/json", "Accept": "application/json"}
}

# и этот словарь будет передаваться в конструктор класса
#handler = Handler(request)
"""

# task 12
import json


class JsonHandler(ParsesBody, ParsesHeaders):
    def __init__(self, request):
        self.request = request

    def process(self):
        if self.need_json() == False:
            return None
        else:
            try:
                json.loads(self.body())
                return len(json.loads(self.body()))
            except:
                return None
# Пример использования
r = {'body': '{"a": 123, "b": 1234}',
     'headers': {'content-type': 'application/json'}
    }
print(JsonHandler(r).process())


# task 13
class SecureTextHandler(ParsesBody, ParsesCookies):
    def __init__(self, request):
        self.request = request
    def process(self):
        if self.is_authed() == False:
            return None
        else:
            return len(self.body())
# Примеры
r = {'cookies': {'auth_key': '123'},
     'body': 'hello'
    }
print(SecureTextHandler(r).process())
# 5
r = {'cookies': {},
     'body': 'hello'
    }
print(SecureTextHandler(r).process())
# None

