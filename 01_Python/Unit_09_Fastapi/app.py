import datetime
from typing import List

import psycopg2
from fastapi import FastAPI, HTTPException, Depends
from loguru import logger
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date

class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:  # передача настроек при создании класса (подробнее в доке)
        orm_mode = True

"""
@app_fc_2.get("/")
def say_hello():
    return "hello, world"
"""
"""@app_fc_2.get("/")
def sum_two(a: int, b: int) -> int:
    return a + b"""


"""@app_fc_2.get("/sum_date")
def sum_date(current_date: datetime.date, offset: int):
    return current_date + datetime.timedelta(days=offset)"""


"""@app_fc_2.get("/user/validate")
def sum_date(current_date: datetime.date, offset: int):
    return current_date + datetime.timedelta(days=offset)"""

"""@app_fc_2.post("/user/validate")
def validate_user(json_file: User):
    logger.info(json_file.dict())
    return f"Will add user: {json_file.name} {json_file.surname} with age {json_file.age}"
"""

def get_db():
    conn = psycopg2.connect(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml",
        cursor_factory=RealDictCursor,
    )
    return conn


@app.get("/user/{id}")
def user_search(id: int, db = Depends((get_db))):
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT gender,
          age,
          city
        FROM "user" as u
        WHERE u.id = %(id)s
        """, {'id': id}
    )
    result = cursor.fetchone()
    if not result:
        raise HTTPException(404, "user not found")
    logger.info(result)
    return result

@app.get("/post/{id}", response_model=PostResponse)
def post_search(id: int, db = Depends((get_db))) -> PostResponse:
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT *
        FROM "post" as p
        WHERE p.id = %(id)s
        """, {'id': id}
    )
    result = cursor.fetchone()
    if not result:
        raise HTTPException(404, "user not found")
    logger.info(result)
    return PostResponse(**result)



