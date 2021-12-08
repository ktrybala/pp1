class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    
    def print_info(self):
        print(b1.name)
        print(b1.author)
        print(b1.year)

b1 = Book("Harry Potter", "J.K.Rowling", 1997)

b1.print_info()