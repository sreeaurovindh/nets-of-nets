from __future__ import print_function

__author__ = 'Varun Joshi'

import os
import re
import mysql.connector

from mysql.connector import errorcode

DB_NAME = 'swm_dataset1'
#DB_NAME = 'test_dataset1'
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


# password='Dellxcd35$'

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

# cursor.close()
# cnx.close()

domain = {"Theoretical_computer_science"}
 #         "Software_engineering"

#"Artificial_intelligence", "Compter_graphics_Multimedia", "Computer_networks", "Database_Data mining_Information_retrieval"
#"High-Performance_Computing" "Information_security" "Human_computer_interaction_Ubiquitous_computing"
#"Interdisciplinary_Studies"
#,

# domain = {"Artificial_intelligence", "Compter_graphics_Multimedia", "Computer_networks", "Database_Data mining_Information_retrieval"}
#domain[0] = "Artificial_intelligence"
#domain[1] = "Compter_graphics_Multimedia"
#domain[2] = "Computer_networks"
#domain[3] = "Database_Data mining_Information_retrieval"
#domain[4] = "High-Performance_Computing"
#domain[5] = "Human_computer_interaction_Ubiquitous_computing"

# , 6: "Information_security",
#           7: "Interdisciplinary_Studies", 8: "Software_engineering", 9: "Theoretical_computer_science"}

add_author = "INSERT INTO swm_dataset1.author (author_name) VALUES ("
add_journal = "INSERT INTO swm_dataset1.journal (journal_name) VALUES ("
add_paper = "INSERT INTO swm_dataset1.paper (paper_index,title) VALUES ("
add_domain_area = "INSERT INTO swm_dataset1.domain_area (domain_name) VALUES ("
add_reference = "INSERT INTO swm_dataset1.reference (paper_key,ref_index) VALUES ("
add_paper_author = "INSERT INTO swm_dataset1.paper_author (paper_key,author_key) VALUES ("
add_paper_details = "INSERT INTO swm_dataset1.paper_details (paper_key,journal_key,year_val,domain_key,citation) VALUES ("

for filename in domain:
    cmdD = add_domain_area + "'" + filename + "');"
    cursor.execute(cmdD)
    domain_key = cursor.lastrowid
    cnx.commit()
    #domain_key = 8
    # cmdD = "SELECT * from swm_dataset1.domain_area where domain_name=" + "'" + filename + "';"
    # cursor.execute(cmdD)
    # data = cursor.fetchone()
    # if data:
    #     domain_key = data[0]

    print(filename)
    #
    open_file = "C:\\Personal\\Academics\\Spring2015\\SWM\\Project\\DBLP\\DBLP_Citation_2014_May\\domains\\" + filename + ".txt"
    with open(open_file, encoding="utf8") as fp:
        for line in fp:
            if (line.find("#*")) == 0:
                #line.rstrip(os.linesep),
                title = line.replace('#*', '', 1)
                title = title.replace('\n', '', 1)
                title = title.replace("'", '', 1)
                for char in title:
                    if char in ".'\"`":
                        title = title.replace(char, '')
                        #title = str.split(line, '#*'),
                        #print(title)
            if (line.find("#@")) == 0:
                name = line.replace('#@', '', 1)
                name = name.replace('\n', '', 1)
                name = name.replace("'", '', 1)
                for char in name:
                    if char in ".'\"`":
                        name = name.replace(char, '')
                authors = name.split(',')
                #print(authors[0])
            if (line.find("#t")) == 0:
                year = line.replace('#t', '', 1)
                year = year.replace('\n', '', 1)
                year_val = int(year)
                #print(year_val)
            if (line.find("#c")) == 0:
                venue = line.replace('#c', '', 1)
                venue = venue.replace('\n', '', 1)
                for char in venue:
                    if char in ".'\"`":
                        venue = venue.replace(char, '')
                        #print(venue)
            if (line.find("#index")) == 0:
                index1 = line.replace('#index', '', 1)
                index1 = index1.replace('\n', '', 1)
                paper_index = int(index1)

                #Journal Table Population
                cmdJ = "SELECT * from swm_dataset1.journal where journal_name=" + "'" + venue + "';"
                cursor.execute(cmdJ)

                # Fetch a single row using fetchone() method.
                data = cursor.fetchone()
                #print(data[0])
                if data:
                    journal_key = data[0]
                    #print("journal alreday exists")
                else:
                    #print(venue)
                    cmd = add_journal + "'" + venue + "');"
                    #print(cmd)
                    # Insert new employee
                    cursor.execute(cmd)
                    journal_key = cursor.lastrowid
                    #print(journal_key)
                    cnx.commit()

                #Paper Table Population
                print(paper_index)
                cmdJ = "SELECT * from swm_dataset1.paper where paper_index=" + str(paper_index)+ " AND title=" + "'" + title + "';"
                cursor.execute(cmdJ)

                # Fetch a single row using fetchone() method.
                data = cursor.fetchone()
                #print(data[0])
                if data:
                    paper_key = data[0]
                    #print("journal alreday exists")
                else:
                    cmdP = add_paper + str(paper_index) + ",'" + title + "');"
                    #print(cmdP)
                    # Insert new employee
                    cursor.execute(cmdP)
                    paper_key = cursor.lastrowid
                    print(paper_index)
                    cnx.commit()



                #Author and Paper_Author Tables Population
                for check in authors:
                    cmdCA = "SELECT * from swm_dataset1.author where author_name=" + "'" + check + "';"
                    cursor.execute(cmdCA)
                    #print(cmdCA)
                    # Fetch a single row using fetchone() method.

                    data = cursor.fetchone()
                    #print("Author")
                    #print(data)
                    if data:
                        author_key = data[0]
                        #print("A already exists")
                    else:
                        #print(check)
                        cmdA = add_author + "'" + check + "');"
                        #print(cmdA)
                        # Insert new employee
                        cursor.execute(cmdA)
                        author_key = cursor.lastrowid
                        #print(author_key)
                        cnx.commit()
                    cmdC = "SELECT * from swm_dataset1.paper_author WHERE paper_key=" + str(paper_key) + " AND author_key=" + str(author_key) + ";"
                    cursor.execute(cmdC)
                    data = cursor.fetchone()
                    if data:
                        a=1
                    else:
                        cmdPA = add_paper_author + str(paper_key) + "," + str(author_key) + ");"
                        #print(cmdPA)
                        cursor.execute(cmdPA)
                        cnx.commit()

                #Reference Table Population
                for line1 in fp:
                    if line1.find("#!") == 0:
                        break
                    else:
                        if (line1.find("#%")) == 0:
                            refer = line1.replace('#%', '', 1)
                            refer = refer.replace('\n', '', 1)
                            for char in refer:
                                if char in " .'\"`":
                                    refer = refer.replace(char, '')
                            if refer != '':
                                refer_key = int(refer)
                                cmdC = "SELECT * from swm_dataset1.paper_author WHERE paper_key=" + str(paper_key) + " AND author_key=" + str(author_key) + ";"
                                cursor.execute(cmdC)
                                data = cursor.fetchone()
                                if data:
                                    a=1
                                else:
                                    cmdR = add_reference + str(paper_key) + "," + str(refer_key) + ");"
                                    #print(cmdR)
                                    # Insert new employee
                                    cursor.execute(cmdR)
                                    refer_id = cursor.lastrowid
                                    #print(refer_id)
                                    cnx.commit()
                cmdC = "SELECT * from swm_dataset1.paper_details WHERE paper_key=" + str(paper_key) + ";"
                cursor.execute(cmdC)
                data = cursor.fetchone()
                if data:
                    a=1
                else:
                    cmdPD = add_paper_details + str(paper_key) + "," + str(journal_key) + "," + str(year_val) + "," + str(domain_key) + ",0);"
                    #print(cmdPD)
                    cursor.execute(cmdPD)
                    PD_id = cursor.lastrowid
                    #print(PD_id)
                    cnx.commit()

                # Make sure data is committed to the database

cursor.close()
cnx.close()


