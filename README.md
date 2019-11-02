## Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree

#### DESCRIPTION
This is the first project in the Full Stack Web Developer Nanodegree, and it goes like this:

>I'm hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. I'm asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

>my task is to create a reporting tool that runs from the command line, and prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

>The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, my code will answer the following three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#### RUNNING THE PROGRAM
1. To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project is developed on, running on your computer. You can download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.
Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.

2. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. Put the file inside the Vagrant folder. 

3. Load the database using `psql -d news -f newsdata.sql`. 
	Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

4. Connect to the database using `psql -d news`.

5. Create the Views given below. Then exit `psql` by writing `\q`.

6. Now execute the Python file - `python logs-analysis-report.py`.

#### CREATE THE FOLLOWING VIEWS:

##### Views for Question 1
```sql
CREATE VIEW popular_articles AS
select title, count(path) as num
from articles, log
where articles.slug = replace(log.path, '/article/', '')
group by title;
```
##### Views for Question 2
```sql
CREATE VIEW popular_authors AS
select authors.name as name, sum(popular_articles.num) as num
from articles, authors, popular_articles
where articles.author = authors.id and
articles.title = popular_articles.title
group by name;
```
