from ebook import Ebook

x = 0
book1 = Ebook("Harry Potter", "J.K.Rowling", 256)

book1.open_book()
book1.book_status()
while x != 6:
	book1.read_page()
	x += 1
book1.book_status()
book1.close_book()
book1.read_page()


