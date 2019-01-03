#!/usr/bin/python3
#-*- coding: utf-8 -*-
#Project - Log Analysis

import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

#The three most viewed articles of all time.
top_three = """ select articles.title, count(*) as views from articles join log on
log.path = ('/article/' || articles.slug)
group by title order by views desc limit 3;"""
c.execute(top_three)
result_1 = c.fetchall()
print("1 - What are the three most popular articles of all time?")
for result in result_1:
    print(f"{result[0]} - {result[1]} views")

#The authors of most popular articles of all time.
famous_authors = """select authors.name, count(*) as views from articles
join authors on articles.author = authors.id
join log on log.path like concat('%', articles.slug, '%') where
log.status = '200 OK' group by authors.name order by views desc;"""
c.execute(famous_authors)
result_2 = c.fetchall()
print("2 - Who are the most famous article authors of all time?")
for result in result_2:
    print(f"{result[0]} - {result[1]} views")

#Shows which days have more than 1 percent of the requests resulted in errors.
error_percent = """select to_char(time::date, 'Mon DD, YYYY'),
(count(case when status != '200 OK' then 1 end)*100)::float/
count(*) from log group by time::date having
(count(case when status != '200 OK' then 1 end)*100)::float/ count(*) > 1;"""
c.execute(error_percent)
result_3 = c.fetchall()
print("3 - On which days did more than 1% of requests lead to errors?")
for result in result_3:
    print(f"{result[0]} {result[1]:.2f} % errors")

db.close()

