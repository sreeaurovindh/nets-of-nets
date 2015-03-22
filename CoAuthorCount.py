from __future__ import print_function

__author__ = 'Abhishek C.V'


import os
import re
import mysql.connector

from mysql.connector import errorcode

DB_NAME = 'swm_dataset1'
#DB_NAME = 'test_dataset1'
TABLES = {}
TABLES['coauthor'] = (
    "CREATE TABLE `coauthor` ("
    "  `domain_key` int NOT NULL,"
    "  `author_key1` int NOT NULL ,"
    "  `author_key2` int NOT NULL ,"
    "  `coauthor_count` int NOT NULL,"
    "  PRIMARY KEY (`domain_key`,`author_key1`,`author_key2`),"
    " FOREIGN KEY (domain_key) REFERENCES domain_area(domain_key),"
    " FOREIGN KEY (author_key1) REFERENCES author(author_key),"
    " FOREIGN KEY (author_key2) REFERENCES author(author_key)"
    ") ENGINE=InnoDB")



# password='Dellxcd35$'

cnx = mysql.connector.connect(user='root', password='abhishek')

print(cnx)

cursor = cnx.cursor()
cursor1 = cnx.cursor()

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

for i in range(2, 12):
    #print("domain = "+str(i))
    paper_query="Select paper_key from swm_dataset1.paper_details where domain_key="+str(i) + " ;"
    #print(paper_query)
    cursor.execute(paper_query)
    data_paper = cursor.fetchall()
    paper_arr = []
    for data in data_paper:
        paper_arr.append(data[0])
    #print(len(paper_arr))

    for papers in paper_arr:
        #print(papers)
        author_query = "Select author_key from swm_dataset1.paper_author where paper_key="+str(papers) + ";"
        #print(author_query)
        cursor.execute(author_query)
        data_author = cursor.fetchall()
        print(data_author)
        author_arr = []
        for data1 in data_author:
            author_arr.append(data1[0])
        #print(len(author_arr))
        if len(author_arr) != 1:
            for j in range(len(author_arr)):
                for k in range(j+1, len(author_arr)):
                    print(str(author_arr[j])+"   "+str(author_arr[k]))
                    cmd_coa = "Select coauthor_count from swm_dataset1.coauthor where domain_key ="+str(i) +" AND author_key1="+str(author_arr[j]) +" AND author_key2="+str(author_arr[k]) +" ;"
                    print(cmd_coa)
                    cursor.execute(cmd_coa)
                    coauthor_count = cursor.fetchone()

                    if coauthor_count:
                        print("already exists and update ")
                        temp = coauthor_count[0]+1
                        update_coa_count = "UPDATE swm_dataset1.coauthor SET coauthor_count="+str(temp)+" WHERE domain_key="+str(i) +" AND author_key1="+str(author_arr[j]) +" AND author_key2="+str(author_arr[k]) +" ;"
                        print(update_coa_count)
                        cursor.execute(update_coa_count)
                        refer_id = cursor.lastrowid
                        print(refer_id)
                        cnx.commit()
                    else:
                        ins_coauthor="INSERT INTO swm_dataset1.coauthor (domain_key,author_key1,author_key2,coauthor_count) VALUES ("+str(i) +","+str(author_arr[j]) +","+str(author_arr[k]) +",1);"
                        cursor.execute(ins_coauthor)
                        refer_id = cursor.lastrowid
                        print(refer_id)
                        cnx.commit()
cursor.close()
cnx.close()