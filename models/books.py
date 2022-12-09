from models.book import *

book1 = Book("Norse Myths", "Kevin Crossley-Holland", "Mythology", False)
book2 = Book("Judge Dredd: The Complete Case Files 05", "John Wagner & Alan Grant", "Graphic Novel", False)
book3 = Book("Pens Are My Friends", "Jon Burgerman", "Art & Design", True)

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book_at_index(index):
    books.pop(index)