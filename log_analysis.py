#!/usr/bin/env python3

"""Log Analysis Project for Full Stack Nanodegree by Udacity"""
import psycopg2


def connect_to_database():
    """Connects to the news database and return a database cursor."""
    try:
        db = psycopg2.connect("dbname=news")
        db_cursor = db.cursor()
    except:
        """Throws exception if it does not connect to the database"""
        print("Failed to connect to the database.")
        return None
    else:
        return db_cursor

def three_most_popular_articles(db_cursor):
    """Query and print out the 3 most popular articles.
    """
    db_cursor.execute("""
            SELECT articles.title,
                   count(*)
            FROM   log,
                   articles
            WHERE  log.path = concat('/article/', articles.slug)
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """)
    articles = db_cursor.fetchall()

    print(' ')
    print('The three most popular articles of all time:')

    for article in articles:
        print('"{title}" -- {count} views'
              .format(title=article[0], count=article[1]))
    return

def most_popular_authors(db_cursor):
    """Query and print out the most popular authors.
    counts all the authors who's articles are most popular
    """
    db_cursor.execute("""
            SELECT authors.name, count(*)
            FROM log, articles, authors
            WHERE  log.path = concat('/article/', articles.slug)
            AND  articles.author = authors.id
            GROUP BY authors.name
            ORDER BY count(*) DESC;
            """)

    authors = db_cursor.fetchall()
    print(' ')
    print('The most popular authors of all time:')

    for author in authors:
        print('{author_name} -- {count} views'
              .format(author_name=author[0], count=author[1]))
    return

        

if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        three_most_popular_articles(db_connection)
        most_popular_authors(db_connection)
        db_connection.close()
