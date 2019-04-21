#!/usr/bin/env python3

"""Log Analysis Project for Full Stack Nanodegree by Udacity"""
import psycopg2


def connect_to_database():
    """Connects to the news database and return a database cursor."""
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
    except:
        """Throws exception if it does not connect to the database"""
        print("Failed to connect to the database.")
        return None
    else:
        return c

def three_most_popular_articles(c):
    """Query and print out the 3 most popular articles.
    """
    query1 = """
            SELECT articles.title,
                   count(*)
            FROM   log,
                   articles
            WHERE  log.path = concat('/article/', articles.slug)
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """
    c.execute(query1)
    articles = c.fetchall()

    print(' ')
    print('1. The three most popular articles of all time:')

    for article in articles:
        print('"{title}" -- {count} views'
              .format(title=article[0], count=article[1]))
    return

def most_popular_authors(c):
    """Query and print out the most popular authors.
    counts all the authors who's articles are most popular
    """
    query2 = """
            SELECT authors.name, count(*)
            FROM log, articles, authors
            WHERE  log.path = concat('/article/', articles.slug)
            AND  articles.author = authors.id
            GROUP BY authors.name
            ORDER BY count(*) DESC;
            """
    c.execute(query2)       
    authors = c.fetchall()
    print(' ')
    print('2. The most popular authors of all time:')

    for author in authors:
        print('{author_name} -- {count} views'
              .format(author_name=author[0], count=author[1]))
    return

def days_greater_than_1pc_errors(c):
    """Query and print out days where the error rate is greater than 1%.
    Args:
        c: psycopg2 PostgreSQL database cursor object.
    """
    query3 = """
     SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
    """
    
    c.execute(query3)
    results = c.fetchall()

    print(' ')
    print('3. Days with greater than 1% errors:')

    for result in results:
        print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
            date=result[0],
            error_rate=result[1]))

    return
        

if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        three_most_popular_articles(db_connection)
        most_popular_authors(db_connection)
        days_greater_than_1pc_errors(db_connection)
        db_connection.close()


