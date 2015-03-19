from __future__ import print_function

__author__ = 'Varun Joshi'

import os
import re
import mysql.connector

from mysql.connector import errorcode

#DB_NAME = 'swm_dataset1'
DB_NAME = 'test_dataset'

TABLES = {}
TABLES['3author'] = (
    "CREATE TABLE `author` ("
    "  `author_key` int NOT NULL AUTO_INCREMENT,"
    "  `author_name` varchar(100) ,"
    "  PRIMARY KEY (`author_key`)"
    ") ENGINE=InnoDB")
TABLES['4journal'] = (
    "CREATE TABLE `journal` ("
    "  `journal_key` int NOT NULL AUTO_INCREMENT,"
    "  `journal_name` varchar(1000) ,"
    "  PRIMARY KEY (`journal_key`)"
    ") ENGINE=InnoDB")
TABLES['2paper'] = (
    "CREATE TABLE `paper` ("
    "  `paper_key` int NOT NULL AUTO_INCREMENT,"
    "  `paper_index` int NOT NULL ,"
    "  `title` varchar(1000) ,"
    "  PRIMARY KEY (`paper_key`)"
    ") ENGINE=InnoDB")
TABLES['1domain_area'] = (
    "CREATE TABLE `domain_area` ("
    "  `domain_key` int NOT NULL AUTO_INCREMENT,"
    "  `domain_name` varchar(50) ,"
    "  PRIMARY KEY (`domain_key`)"
    ") ENGINE=InnoDB")
TABLES['6reference'] = (
    "CREATE TABLE `reference` ("
    "  `paper_key` int NOT NULL,"
    "  `ref_index` int NOT NULL ,"
    "  PRIMARY KEY (`paper_key`,`ref_index`)"
    ") ENGINE=InnoDB")
TABLES['7paper_details'] = (
    "CREATE TABLE `paper_details` ("
    "  `paper_key` int NOT NULL,"
    "  `journal_key` int NOT NULL ,"
    "  `year_val` int NOT NULL ,"
    "  `domain_key` int NOT NULL ,"
    "  `citation` int NOT NULL ,"
    "  PRIMARY KEY (`paper_key`),"
    " FOREIGN KEY (paper_key) REFERENCES paper(paper_key),"
    " FOREIGN KEY (journal_key) REFERENCES journal(journal_key) ,"
    " FOREIGN KEY (domain_key) REFERENCES domain_area(domain_key)"
    ") ENGINE=InnoDB")
TABLES['5paper_author'] = (
    "CREATE TABLE `paper_author` ("
    "  `paper_key` int NOT NULL,"
    "  `author_key` int NOT NULL ,"
    "  PRIMARY KEY (`paper_key`,`author_key`),"
    " FOREIGN KEY (paper_key) REFERENCES paper(paper_key),"
    " FOREIGN KEY (author_key) REFERENCES author(author_key)"
    ") ENGINE=InnoDB")


#  password='Dellxcd35$'

cnx = mysql.connector.connect(user='root', password='root')

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

cnx.commit()

cursor.close()
cnx.close()