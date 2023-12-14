# pip install psycopg2 если библиотека не установлена
import psycopg2
connection = psycopg2.connect(    # connection - это объект, который отвечает за соединение с БД
    database="startml",
    user="robot-startml-ro",
    password="pheiph0hahj1Vaif",
    host="postgres.lab.karpov.courses",
    port=6432
)
cursor = connection.cursor()


import pandas as pd

conn_uri = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"
df = pd.read_sql(
    """SELECT * FROM "feed_action" LIMIT 10 """,
    conn_uri
)

df.head()

# task 1
df = pd.read_sql(
    """SELECT * FROM "user" """,
    conn_uri
)


# task 2
df = pd.read_sql(
    """SELECT distinct p.topic FROM "post" as p """,
    conn_uri
)


# task 3
df = pd.read_sql(
    """SELECT * FROM "user" as u
        WHERE u.age > 30 AND u.os = 'iOS'

    """,
    conn_uri
)


# task 4
df = pd.read_sql(
    """SELECT * FROM "user" as u
        WHERE u.country != 'Russia' AND ((u.exp_group NOT IN (0, 3)) OR u.city = 'Minsk')

    """,
    conn_uri
)

# task 5
df = pd.read_sql(
    """SELECT country, AVG(age) FROM "user" as u
        GROUP BY country

    """,
    conn_uri
)
round(df.iloc[2]['avg'], 2)
round(df[df['country'] == 'Cyprus']['avg'], 2)

# task 6
df = pd.read_sql(
    """SELECT exp_group, os, COUNT(id) as "total_users", MAX(age) as "max_age", MIN(age) as "min_age" FROM "user"
        GROUP BY exp_group, os

    """,
    conn_uri
)
df.to_csv("step_6.csv", index = False)

# task 7
df = pd.read_sql(
    """SELECT topic, text FROM "post"
        GROUP BY topic, text
        HAVING LENGTH(text) > 25000
    """,
    conn_uri
)

# task 8
df = pd.read_sql(
    """SELECT country, COUNT(country) FROM "user"
        GROUP BY country
        HAVING COUNT(country) > 1000
        ORDER BY COUNT(country)
    """,
    conn_uri
)

# task 9
"""SELECT country, exp_group, COUNT(id)
FROM "user"
GROUP BY country, exp_group;
"""

# task 10
df = pd.read_sql(
    """SELECT exp_group, AVG(age), count(id) FROM "user"
        WHERE city = 'Moscow'
        GROUP BY exp_group
        HAVING AVG(age) > 27.2
    """,
    conn_uri
)

# task 11
df = pd.read_sql(
    """SELECT topic, count(id) FROM "post"
        GROUP BY topic
        ORDER BY count(id) DESC
    """,
    conn_uri
)

# task 12
df = pd.read_sql(
    """SELECT * FROM "user" as u
        WHERE u.city = 'Voronezh'
        ORDER BY age DESC, exp_group
    """,
    conn_uri
)

# task 13
df = pd.read_sql(
    """SELECT f.post_id, f.time, u.age, u.os FROM "user" as u
        JOIN "feed_action" f ON u.id = f.user_id
        WHERE u.city = 'Omsk'AND f.action = 'like'
        ORDER BY f.time DESC
        LIMIT 100
    """,
    conn_uri
)
df.to_csv("step_15.csv", index = False)

# task 14
df = pd.read_sql(
    """SELECT u.city, COUNT(u.city) FROM "user" as u
        JOIN "feed_action" f ON u.id = f.user_id
        JOIN "post" p ON f.post_id = p.id
        WHERE DATE(f.time) = '2021-12-01' AND f.action = 'view' and u.age = 36 and p.topic = 'covid'
        GROUP BY city
        ORDER BY COUNT(u.city)
    """,
    conn_uri
)

# task 15
df = pd.read_sql(
    """SELECT post_id, COUNT(post_id) as "Likes", MAX(DATE(time)) as "Latest like" FROM "feed_action" as f
        WHERE action = 'like'
        GROUP BY post_id
        ORDER BY count(post_id) DESC
    """,
    conn_uri
)
