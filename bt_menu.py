def init_app(lib):
	# Library = BookList()
	try:
		lib.load_books(Fname)
	except OSError as E:
		print("You are running app for the first time! Library is empty")


def print_main_menu():
	print("1. Show library")
	print("2. My book lists")
	print("3. Add new book")
	print("4. Save library")
	print("5. Exit")


def print_new_book():
	print("Enter book details: ")
	author = input("Author: ")
	title = input("Title: ")
	pages = input("Pages: ")

	new_book = Book(author=author, name=title)

	if pages.isdigit():
		new_book.set_pages(int(pages))
		
	return new_book

def print_my_lists():
	print("1. View lists")
	print("2. Add new list")
	print("3. Back")
	pass
	
def handle_my_lists(lib):
	while True:
		print_my_lists()
		sp = input(">")
		if sp.isdigit():
			p = int(sp)
			if p is 1:
				pass
			elif p is 2:
				pass
			elif p is 3:
				return 
		
def handle_main_menu(lib):
	while True:
		print_main_menu()

		sp = input(">")
		if sp.isdigit():
			p = int(sp)
			if p is 1:
				lib.ViewBooks()
			elif p is 2:
				handle_my_lists(lib)
			elif p is 3:
				handle_new_book(lib)
			elif p is 4:
				lib.save_books(Fname)
			elif p is 5:
				print("See you around!")
				return


def handle_new_book(lib):
	book = print_new_book()
	lib.AddBook(book)


def main2():
	Library = BookList()
	
	init_app(Library)
	handle_main_menu(Library)
