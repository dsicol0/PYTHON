# AGGREGATION -->   REPRESENTS A RELATIONSHIP WHERE ONE OBJECT (THE WHOLE)
#                   CONTAINS REFERENCES TO ONE OR MORE 
#                   INDEPENDENT OBJECTS (THE PARTS)

# THE WHOLE 
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

# INDEPENDENT PARTS
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Biblioteca Comunale Acquaviva")

book1 = Book("Il Signore degli Anelli", "J. R. R. Tolkien")
book2 = Book("Il Ritratto di Dorian Grey", "Oscar Wilde")
book3 = Book("Il sosia", "Fedor Dostoievskij")

# library will contain books (add books to Library)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(f"Welcome to {library.name}")

for book in library.list_books():
    print(book)