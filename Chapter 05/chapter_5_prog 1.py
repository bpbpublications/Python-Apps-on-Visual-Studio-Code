#Presented below is the complete code for perform_db_actions():
from datetime import datetime
import pymysql


def perform_db_actions(db_name, query):
    '''This function will be called for any kinds of 
    database interaction from all other files as well. 
    @db_name: the name of the database
    @query: the query to be executed
    @values: the values for dynamic query in tuple format
    returns: Select query will return the recordset, other queries will return none
    '''
    connect = pymysql.connect(host="localhost",
                              user="root",
                              password="learnSQL",
                              database=db_name)
    cursorobj = connect.cursor()
    data = []
    data = cursorobj.execute(query)
    data = cursorobj.fetchall()
    connect.commit()
    cursorobj.close()
    return data

def create_db(db_name):
    '''One time create database queries'''
    # Table 1 Students getting created
    t1 = '''Create table STUDENTS(
    MEMID INTEGER   PRIMARY KEY  AUTO_INCREMENT,
    NAME VARCHAR(30),
    EMAIL VARCHAR(15),
    PHONE VARCHAR(12),
    JOIN_DATE DATE DEFAULT (CURRENT_DATE))'''
    # call DB action
    perform_db_actions(db_name, t1)
    t2 = '''Create table BOOKS(
    BOOKID INTEGER   PRIMARY KEY AUTO_INCREMENT,
    TITLE VARCHAR(30),
    AUTHOR VARCHAR(15),
    PUBLISHER VARCHAR(15),
    PRICE REAL,
    COPIES SMALLINT)'''
    perform_db_actions(db_name, t2)

    t3 = '''Create table TRANSACTIONS(
    TID INTEGER   PRIMARY KEY AUTO_INCREMENT,
    BOOKID INTEGER REFERENCES BOOKS(BOOKID),
    MEMID INTEGER REFERENCES STUDENTS(MEMID),
    ISSUE_DATE DATE,
    RETURN_DATE DATE)'''
    perform_db_actions(db_name, t3)

    add_students = ['''INSERT INTO STUDENTS(NAME,EMAIL,PHONE) VALUES('Sachin','sachin@em.com','346377')''',
                    '''INSERT INTO STUDENTS(NAME,EMAIL,PHONE) VALUES('Virat','virat@em.com','544343466')''',
                    '''INSERT INTO STUDENTS(NAME,EMAIL,PHONE) VALUES('Dhoni','dhoni@ema.com','5645654')''',
                    '''INSERT INTO STUDENTS(NAME,EMAIL,PHONE) VALUES('Kapil','kapil@ema.com','4576457')''']
    for q in add_students:
        perform_db_actions(db_name, q)
    add_books = ['''INSERT INTO BOOKS(TITLE,AUTHOR,COPIES) VALUES('Practice Python','Swapnil Saurav',3)''',
                 '''INSERT INTO BOOKS(TITLE,AUTHOR,COPIES) VALUES('Practice SQL','Swapnil Saurav',3)''',
                 '''INSERT INTO BOOKS(TITLE,AUTHOR,COPIES) VALUES('Practice Data Visualization','Swapnil Saurav',3)''',
                 '''INSERT INTO BOOKS(TITLE,AUTHOR,COPIES) VALUES('Practice Machine Learning','Swapnil Saurav',3)''']

    for q in add_books:
        perform_db_actions(db_name, q)

    print("Your data has been created successfully!")

if __name__ == "__main__":
    create_db("libraryms")  #Onetime