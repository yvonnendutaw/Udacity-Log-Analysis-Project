# Log Analysis Project
The Log Analysis project is part of the  Full Stack Web Developer Nanodegree program at Udacity.

## What is it for?
This project will be used to create a report on the most popular three articles of all time from the data in a [database file](newsdata.zip). This will be done using SQL queries to answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites
To run this program you will need to have:
* Python 2.7.5
* psycopg2 2.7.6.1
* PostgreSQL 9.5.14

It is advisable to run the project in a Vagrant environment so that it does not interfere with your host machine and because it comes with all the dependencies required.
* For this you will need [Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on
your system.

## Run the Project
1. Clone this repository to your preffered folder, or download the zip file.

2. Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows) and navigate to the project
directory.

3. Bring up the VM with the following command:

```bash
vagrant up
```

4. You can then log into the VM with the following command:

```bash
vagrant ssh
```

5. Once inside the VM, navigate to the tournament directory with this command:

```bash
cd /vagrant
```

6. First, unzip the zip file with the command:

```bash
unzip newsdata.zip
```

7. Then run the following command to load the logs into the database:

```bash
psql -d news -f newsdata.sql
```
8. The logs reporting tool is executed with the following command:

```bash
python log_analysis.py
```

### For question three you will need to create the following view in psql:


```bash
CREATE VIEW total_views AS SELECT date(time), count(*)
As views FROM Log
GROUP BY date(time)
ORDER BY date(time);
```
```bash
CREATE VIEW error_views AS SELECT date(time), count(*) 
As errors FROM Log WHERE Status = '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);
```
```bash

CREATE VIEW error_rate AS
SELECT total_views.date, (100.0*error_views.errors/total_views.views) AS percentage
FROM total_views, error_views
WHERE total_views.date = error_views.date
ORDER BY total_views.date;
```
9. If you wish to shut down the VM you can do so with the following command:
```bash
vagarant halt
```
