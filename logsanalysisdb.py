#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


# connects to database and runs query
def get_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# returns top 3 articles sorted by page views
query1 = """
SELECT articles.title, COUNT(*) as views
FROM articles, log
WHERE log.path = (concat('/article/', articles.slug))
GROUP BY articles.title
ORDER BY views desc
LIMIT 3;
"""


# returns authors sorted by most page views
query2 = """
SELECT authors.name as author, COUNT(*) as views
FROM authors, articles, log
WHERE log.path = (concat('/article/', articles.slug))
AND articles.author = authors.id
GROUP BY authors.name
ORDER BY views desc;
"""

# returns days where more than 1% of HTTP requests led to an error
query3 = """
SELECT (to_char(time, 'Month DD, YYYY')) as date,
ROUND(
SUM(CASE WHEN log.status = '404 NOT FOUND' THEN 1 ELSE 0 END)::decimal /
(COUNT(log.status))*100, 1) as percent
FROM log
GROUP BY date
HAVING round(
sum(case when log.status = '404 NOT FOUND' THEN 1 ELSE 0 END)::decimal /
(count(log.status))*100, 1) > 1.0;
"""

# results for each query
result1 = get_query(query1)
result2 = get_query(query2)
result3 = get_query(query3)

# presenting query1 with proper display
print("Top 3 most popular articles:" + "\n")
for i in result1:
    print('"{}"'.format(i[0]) + " - " + str(i[1]) + " views")
print("\n")

# presenting query2 with proper display
print("Most popular article authors of all time:" + "\n")
for i in result2:
    print(i[0] + " - " + str(i[1]) + " views")
print("\n")

# presenting query3 with proper display
print("Days where more than 1% of HTTP requests led to an error:" + "\n")
for i in result3:
    print(" ".join(i[0].split()) + " - " + str(i[1]) + "% errors")
