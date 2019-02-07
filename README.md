# Logs Analysis Project

## Project Overview

This is the first project in Udacity's Full Stack Nanodegree program.
In this project, we will use Python3 and PostgreSQL to develop a reporting tool
that connects to a database and prints out reports in plain-text format. These
reports will answer the following questions:

1. **What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2. **Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. **On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Installation Requirements:
1. Install [Virtual Box](https://www.virtualbox.org/).
2. Install [Vagrant](https://www.vagrantup.com/downloads.html).
3. Download the [VM Configuration](https://github.com/udacity/fullstack-nanodegree-vm).
4. Download the [news](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) zip file. Extract its contents and store it in the **vagrant folder** that was downloaded in step 3.

## Starting the Virtual Machine:
1. From your terminal, inside the **/vagrant** subdirectory, run the command `vagrant up`.
2. Once it is finished, run `vagrant ssh` to connect to the virtual machine.

## Loading the file and using PostgreSQL
1. Import file by typing `psql -d news -f newsdata.sql` into your terminal while connected to the virtual machine.
2. Create a file in your favorite text editor to store your queries and python code. I named the file **logsanalysisdb.py** stored inside the vagrant folder.
3. If you exit the terminal, you will need to cd into the **/vagrant** directory again and run `vagrant ssh` to reconnect, and use `psql news` to run queries. If you shutdown the computer, you will need to run `vagrant up` again before
3. Run your python code in the terminal by typing `python3 logsanalysisdb.py` while in the **/vagrant** subdirectory.
