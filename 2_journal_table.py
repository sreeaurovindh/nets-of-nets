from __future__ import print_function
import os
import re
import mysql.connector

from mysql.connector import errorcode

DB_NAME = 'verified_papers'

TABLES = {}
TABLES['journal'] = (
    "CREATE TABLE `journal` ("
    "  `venue_id` int NOT NULL AUTO_INCREMENT,"
    "  `venue_name` varchar(1000) ,"
    "  PRIMARY KEY (`venue_id`)"
    ") ENGINE=InnoDB")
password='Dellxcd35$'

cnx = mysql.connector.connect(user='root', password=password)

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

add_journal = "INSERT INTO verified_papers.journal (venue_name) VALUES ("
open_file = "C:\\Users\\Darshan\\Desktop\\ASU\\DBLP_Citation_2014_May\\DBLP_Citation_2014_May\\publications.txt"
with open(open_file, encoding="utf8") as fp:
    for line in fp:
        if (line.find("#*")) == 0:
            #line.rstrip(os.linesep),
            title = line.replace('#*','',1)
            title = title.replace('\n','',1)
            title = title.replace("'",'',1)
            for char in title:
                if char in " .'\"`":
                    title=title.replace(char,'')
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
            for char in venue:
                if char in " .'\"`":
                    venue=venue.replace(char,'')
            print(venue)
        if (line.find("#index")) == 0:
            index1 = line.replace('#index','',1)
            index1 = index1.replace('\n','',1)
            print(index1)
            cmd1="SELECT * from verified_papers.journal where venue_name="+"'"+venue+"';"
            cursor.execute(cmd1)

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            #print(data[0])
            if data:
                print("venue alreday exists")
            else:
                #print(venue)
                cmd = add_journal+"'"+venue+"');"
                print(cmd)
                # Insert new employee
                cursor.execute(cmd)
                id = cursor.lastrowid
                print(id)


# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()


