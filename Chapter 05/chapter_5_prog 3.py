""" Books Example"""
import sql

class Books:
    """ Books Class"""
    def __init__(self, dbname):
        """ Initialize books class"""
        self.dbname = dbname

    def create_book(self):
        """ Create a new book record """
        title = input("Enter the Title of the Book: ")
        author = input("Enter the Author name of the Book: ")
        publisher = input("Enter the Publisher of the Book: ")
        price = float(input("Enter the Price id of the Book: "))
        copies = int(input("Enter the Copies of the Book: "))

        query = f'''INSERT INTO BOOKS(title, author, publisher, price, copies) 
        VALUES('{title}', '{author}', '{publisher}', {price}, {copies})'''

        sql.perform_db_actions(self.dbname, query)
        print("Successfully added book record to the database")

    def display_all(self):
        """ Display all the books in the database """
        query = '''SELECT * FROM BOOKS'''
        rows = sql.perform_db_actions(self.dbname, query)
        print("Books available in the Library are:")
        for book in rows:
            print(book)

    def display_specific(self):
        """ Display a specific book record """
        book_id = int(input("Enter the ID of the Book: "))
        query = f'''SELECT * FROM BOOKS WHERE bookid = {book_id}'''
        rows = sql.perform_db_actions(self.dbname, query)
        print("Details are:")
        for book in rows:
            print(book)

    def modify_book(self):
        """Modify the details of a specific book record"""
        bid = int(input("Enter the ID of the book record to be updated: "))
        query = f"SELECT title, author, publisher, price, copies FROM BOOKS WHERE bookid = {bid}"
        rows = sql.perform_db_actions(self.dbname, query)

        if rows:
            cols = ['title', 'author', 'publisher', 'price', 'copies']
            update_query = "UPDATE BOOKS SET"

            if len(rows[0]) > 1:
                for col, value in zip(cols, rows[0]):
                    print(f"Current {col} is {value}")
                    ch = input("Enter y to modify: ")
                    if ch.lower() == 'y':
                        if col in ['title', 'author', 'publisher']:  # string values
                            inp = input(f"Enter the new {col}: ")
                            update_query += f" {col} = '{inp}',"
                        elif col in ['price', 'copies']:  # numeric values
                            inp = int(input(f"Enter the new {col}: "))
                            update_query += f" {col} = {inp},"

                if len(update_query) > 16:
                    update_query = update_query[:-1] + f" WHERE bookid = {bid}"
                    rows = sql.perform_db_actions(self.dbname, update_query)
                    print("Data has been updated")
                else:
                    print("Nothing to update!")
        else:
            print("No such data available!")


    def delete_book(self):
        """ Delete a specific book record"""
        book_id = int(input("Enter the ID of the Book record to be deleted: "))
        query = f'''SELECT bookid FROM BOOKS WHERE bookid = {book_id}'''
        rows = sql.perform_db_actions(self.dbname, query)
        if len(rows) == 0:
            print("No such data available!")
        else :
            query = f'''DELETE FROM BOOKS WHERE bookid = {book_id}'''
            rows = sql.perform_db_actions(self.dbname, query)
            print("Data deleted")
