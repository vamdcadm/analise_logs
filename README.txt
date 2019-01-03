# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________
## About
This is the third project for the Udacity Back end Nanodegree. 
## Prerequisites
* Python 3 [open the terminal and type sudo apt-get install python3.5 to install python]
* Vagrant [download https://www.vagrantup.com/]
* VirtualBox 3 [download https://www.virtualbox.org/wiki/Downloads]
* DB [ download https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]

You will need to unpack the newsdata.zip. The file inside is called newsdata.sql. Place this file in the vagrant directory that is shared with the virtual machine.

To create the reporting tool, you need to load these files from the site into your local database. 

To load the data, use the psql -d news -f newsdata.sql command.
Here's what this command does:

    *psql - the PostgreSQL command-line program
    *-d news - connects to the database called news that was created for you
    *-f newsdata.sql - executes the SQL statements in the newsdata.sql file

Executing this command will connect you to your installed database server and execute the SQL commands on the downloaded file, creating tables and populating them with data.

To Run

Launch Vagrant VM by running vagrant up and vagrant ssh

To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.

To execute the program, run python3 report.py from the command line and after some seconds the report.txt will be update.


