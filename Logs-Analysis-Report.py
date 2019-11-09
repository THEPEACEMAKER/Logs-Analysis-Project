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
popularAuthors = """select name, num
                     from popular_authors
                     order by num desc"""
errorsDay = """select day, percentage
                from errors_percentage
                where percentage > 1
                order by percentage desc"""


# dealing with the results
def print_results(q_results, type):
    print(" ")
    if type == "views":
        for i in q_results:
                print("\t" + str(i[0]) + " - " + str(i[1]) + " views")
        print("\n")
    elif type == "errors":
        for i in q_results:
                print("\t" + str(i[0]) + " - " + str(i[1]) + " % " + "errors")
        print("\n")

# executing
print("The most popular three articles of all time")
print_results(queryDB(popularAritcles), "views")
print("the most popular article authors of all time")
print_results(queryDB(popularAuthors), "views")
print("The dayes on which more than 1% of requests led to errors")
print_results(queryDB(errorsDay), "errors")
