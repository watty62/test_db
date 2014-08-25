#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    con = lite.connect('test.db')

    cur = con.cursor()  

    cur.executescript("""
        DROP TABLE IF EXISTS data;
        CREATE TABLE data (Id INT, Name TEXT, Price INT);
        INSERT INTO data VALUES(1,'Audi',52642);
        INSERT INTO data VALUES(2,'Mercedes',57127);
        INSERT INTO data VALUES(3,'Skoda',9000);
        INSERT INTO data VALUES(4,'Volvo',29000);
        INSERT INTO data VALUES(5,'Bentley',350000);
        INSERT INTO data VALUES(6,'Citroen',21000);
        INSERT INTO data VALUES(7,'Hummer',41400);
        INSERT INTO data VALUES(8,'Volkswagen',21600);
        """)

    con.commit()
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 
        
con = lite.connect('test.db')
with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM data")

    rows = cur.fetchall()

    for row in rows:
        print row
if con:
    con.close()
