import datetime as dt
""" Students Example"""
import sql


class Students:
    """Class for Students Example"""
    def __init__(self, dbname):
        """ Initialize the class """
        self.dbname = dbname

    def create_student(self):
        """ Create a new student record """
        name = input("Enter the name of the student: ")
        email = input("Enter the email id of the student: ")
        phone = input("Enter the phone of the student: ")
        query = f'''INSERT INTO STUDENTS(NAME, EMAIL, PHONE)
        VALUES('{name}', '{email}', '{phone}')'''
        sql.perform_db_actions(self.dbname, query)
        print("Successfully added Student record to the database")

    def display_all(self):
        """ Display all the student records in the database"""
        query = '''SELECT * FROM STUDENTS'''
        rows = sql.perform_db_actions(self.dbname, query)
        print("Students in the database:")
        for student in rows:
            print(student)

    def display_specific(self):
        """ Display the details of a specific student record """
        memid = int(input("Enter the Membership ID of the the student: "))
        query = f'''SELECT * FROM STUDENTS WHERE memid = {memid}'''
        rows = sql.perform_db_actions(self.dbname, query)
        print("Details are:")
        for student in rows:
            print(student)

    def modify_student(self):
        """Modify the details of a specific student record"""
        memid = int(input("Enter the Membership ID of the student record to be updated: "))
        query = f"SELECT name, email, phone FROM STUDENTS WHERE memid = {memid}"
        rows = sql.perform_db_actions(self.dbname, query)

        if rows:
            cols = ["Name", "Email", "Phone"]
            update_query = "UPDATE STUDENTS SET"

            if len(rows[0]) > 1:
                for i, col in enumerate(cols):
                    print(f"Current {col} is {rows[0][i]}")
                    ch = input("Enter y to modify: ")
                    if ch.lower() == 'y':
                        inp = input(f"Enter the new {col}: ")
                        update_query += f" {col} = '{inp}',"

                if len(update_query) > 17:
                    update_query = update_query[:-1] + f" WHERE memid = {memid}"
                    rows = sql.perform_db_actions(self.dbname, update_query)
                    print("Data has been updated")
                else:
                    print("Nothing to update!")
        else:
            print("No such data available!")

    def delete_student(self):
        """ Delete a specific student record """
        memid = int(
            input("Enter the Membership ID of the student record to be deleted: "))
        query = f'''SELECT memid FROM STUDENTS where memid = {memid}'''
        rows = sql.perform_db_actions(self.dbname, query)
        if len(rows) == 0:
            print("No such data available!")
        else:
            query = f'''DELETE FROM STUDENTS WHERE memid = {memid}'''
            sql.perform_db_actions(self.dbname, query)
            print("Deleted student record")
