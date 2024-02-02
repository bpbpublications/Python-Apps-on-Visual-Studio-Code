class Book:
    """Represents a Book class example"""
    #declaring a class variable:
    book_count = 0
    #Now initialize the variable using the init
    def __init__(self,title): #self keyword represents instance (object) of the class
        ''' Initialize the data'''
        self.title = title
        print("Initializing the title of the book: ", self.title)
        #When a book is created, it should increase the total book count by 1
        Book.book_count +=1  #Since its a class variable, Class name.variable is used

    def remove(self):
        '''Removing book from the list'''
        print("{} is being removed from the list!".format(self.title))
        Book.book_count -= 1
        if Book.book_count <= 0:
            print("It was the last book in the shelf. You don’t have any more book!")
        else:
            print("There are still {} books in the shelf!".format(Book.book_count))

    def say_hi(self):
        """Hello from the book class"""
        print("Hello from Class Book, I am being called by ",self.title)

    @classmethod
    def how_many(cls):
        """Prints current number of books available"""
        print("Currently there are {} books in the shelf.".format(cls.book_count))

####  Below code is used to create object of the class Book
#Creating objects and initializing the title using __init__
#Automatically called while creating objects
book1 = Book("The A to Z of Retail Management")
book2 = Book("Learn and Practice Python Programming")
book3 = Book("Boost your career")
#calling class variable using classname
print("Total number of books available in the shelf: ",Book.book_count)
#Calling functions
book1.say_hi()
book2.remove()
#calling class variable using object
print("Total number of books available in the shelf: ",book3.book_count)