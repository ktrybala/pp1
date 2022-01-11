class Ebook:

	'''Class creates an ebook object and defines its attributes'''

	def __init__(self, title, author, page_numbers):
		self.title = title
		self.author = author
		self.page_numbers = page_numbers
		self.current_page_no = 0
		self.status = False

	def book_status(self):
		print(f"Title: {self.title}, Author: {self.author}, Page number: {self.page_numbers}, Current page: {self.current_page_no}")

	def open_book(self):
		if self.status == False:
			self.status = True
			print("The Book is opened.")
		elif self.status == True:
			print("The Book is already opened.")

	def close_book(self):
		if self.status == True:
			self.status = False
			print("The Book is closed.")
		elif self.status == True:
			print("The Book is already closed.")

	def read_page(self):
		if self.status == True:
			if self.current_page_no < self.page_numbers:
				self.current_page_no += 1
			else:
				print("You're on final page.")
		else:
			print("The Book is closed. You cannot read it.")



