import datetime
from typing import List

import psycopg2
from fastapi import FastAPI, HTTPException
from loguru import logger
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel  # для наследования класса-валидатора. Если нет значения по умолчанию - поле обязательно

app = FastAPI()


class BookingGet(BaseModel):
    id: int
    facility_id: int
    member_id: int
    start_time: datetime.datetime
    slots: int

    class Config:  # передача настроек при создании класса (подробнее в доке)
        orm_mode = True


class SimpleUser(BaseModel):
    name: str
    surname: str
    age: int


@app.get("/", summary="Just say hello")
def say_hello():
    """Say hello to a user.

    :return:
    """
    return "hello"


@app.get("/sum")
def sum_two(a: int, b: int) -> int:
    return a + b


@app.get("/print/{number}/{number_2}")
def print_num(number: int, number_2: int):
    return number * 2 + number_2


@app.post("/user")
def print(name: str):
    return {"message": f"hello, {name}"}


@app.get("/booking/all", response_model=List[BookingGet])  # класс-валидатор. Список объектов для множественного вывода
def all_bookings():
    conn = psycopg2.connect(
        "postgresql://postgres:password@localhost:5432/exercises",
        cursor_factory=RealDictCursor,  # курсор будет возвращаться словарём, а не списком
    )
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT bookid AS id,
          facid AS facility_id,
          memid AS member_id,
          starttime AS start_time,
          slots
        FROM cd.bookings
        """
    )
    result = cursor.fetchall()
    logger.info(result)
    return result


@app.post("/user/validate")
def validate_user(user: SimpleUser):
    logger.info(user.dict())
    return "ok"


@app.get("/error")
def show_error(a: int):
    if a == 5:
        raise HTTPException(304)
    return "ok"
