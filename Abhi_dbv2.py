# from bs4 import BeautifulSoup
# import re
#
# import requests
# #import dblp
#
# count = 0
# temp1 =10
# for j in[0, 50]:
# temp1=temp1+j,
#     url = "http://citeseerx.ist.psu.edu/viewdoc/versions?doi=10.1.1.129.16" + temp1,
#     r = requests.get(url),
#     data = r.text,
#     soup = BeautifulSoup(data),
#     td = soup.find_all('td'),
#     t = len(td),
#     #print(t)
#     for i in range(0, t):
#         if td[i].__contains__("AUTHOR NAME"):
#             count=count+1

from __future__ import print_function
import os
import re
import mysql.connector

from mysql.connector import errorcode

DB_NAME = 'test1'

TABLES = {}
TABLES['test'] = (
    "CREATE TABLE `test` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(100) NOT NULL,"
    "  `name1` varchar(100) NOT NULL,"
    "  `year1` varchar(5) NOT NULL,"
    "  `venue` varchar(100) NOT NULL,"
    "  `index1` varchar(50) NOT NULL,"
    "  `citation1` varchar(50),"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

# TABLES['departments'] = (
#     "CREATE TABLE `departments` ("
#     "  `dept_no` char(4) NOT NULL,"
#     "  `dept_name` varchar(40) NOT NULL,"
#     "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
#     ") ENGINE=InnoDB")
#
# TABLES['salaries'] = (
#     "CREATE TABLE `salaries` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `salary` int(11) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
#
# TABLES['dept_emp'] = (
#     "CREATE TABLE `dept_emp` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `dept_no` char(4) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
#
# TABLES['dept_manager'] = (
#     "  CREATE TABLE `dept_manager` ("
#     "  `dept_no` char(4) NOT NULL,"
#     "  `emp_no` int(11) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`),"
#     "  KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
#
# TABLES['titles'] = (
#     "CREATE TABLE `titles` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `title` varchar(50) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date DEFAULT NULL,"
#     "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
#
#
cnx = mysql.connector.connect(user='root', password='')

print(cnx)

cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# cursor.close()
# cnx.close()

add_paper = "INSERT INTO test1.test (title, name1, year1, venue, index1, citation1) VALUES ("
open_file = "C:\\Users\\Darshan\\Desktop\\ASU\\DBLP_Citation_2014_May\\DBLP_Citation_2014_May\\publications.txt"
with open(open_file) as fp:
    for line in fp:
        if (line.find("#*")) == 0:
            #line.rstrip(os.linesep),
            title = line.replace('#*','',1)
            title = title.replace('\n','',1)
            title = title.replace("'",'',1)
            #title = str.split(line, '#*'),
            #print(title)
        if (line.find("#@")) == 0:
            name = line.replace('#@','',1)
            name = name.replace('\n','',1)
            name = name.replace("'",'',1)
            #print(name)
        if (line.find("#t")) == 0:
            year = line.replace('#t','',1)
            year = year.replace('\n','',1)
            #print(year)
        if (line.find("#c")) == 0:
            venue = line.replace('#c','',1)
            venue = venue.replace('\n','',1)
            #print(venue)
        if (line.find("#index")) == 0:
            index1 = line.replace('#index','',1)
            index1 = index1.replace('\n','',1)
            #print(index1)
            for line1 in fp:
                if line1.find("#!") == 0:
                    break
                else:
                    if (line1.find("#%")) == 0:
                        citation = line1.replace('#%','',1)
                        citation = citation.replace('\n','',1)
                        # print(title)
                        # print(name)
                        # print(year)
                        # print(venue)
                        # print(index1)
                        # print(citation)
                        cmd = add_paper+"'"+title+"', "+"'"+name+"', "+"'"+year+"', "+"'"+venue+"', "+"'"+index1+"', "+"'"+citation+"');"
                        print(cmd)
                        # Insert new employee
                        cursor.execute(cmd)
                        id = cursor.lastrowid
                        print(id)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()








