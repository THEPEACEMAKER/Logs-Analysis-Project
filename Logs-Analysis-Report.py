#!/usr/bin/env python
# Logs Analysis Project

# Import postgresql library
import psycopg2

# connecting and executing the queries in the database
DBNAME = "news"


def queryDB(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

# the sql queries
popularAritcles = """select title, num
                     from popular_articles
                     order by num desc
                     limit 3"""
