# coding: utf-8
# import console

from booklib.book import Book
from booklib.booklist import BookList
Library: BookList
Fname = "library.json"


def init_app():
	Library = BookList()
	try:
		Library.load_books(Fname)
	except OSError as E:
		print("You are running app for the first time! Library is empty")


def print_main_menu():
	print("1. Show library")
	print("2. Add new book")
	print("3. Save library")
	print("4. Exit")


def print_new_book():
	print("Enter book details: ")
	author = input("Author: ")
	title = input("Title: ")
	pages = input("Pages: ")

	new_book = Book(author=author, name=title)

	if pages.isdigit():
		new_book.set_pages(int(pages))
		Library.AddBook(new_book)
	return


def handle_main_menu():
	while True:
		print_main_menu()

		sp = input(">")
		if sp.isdigit():
			p = int(sp)
			if p is 1:
				Library.ViewBooks()
			elif p is 2:
				handle_new_book()
			elif p is 3:
				Library.save_books()
			elif p is 4:
				return


def handle_new_book():
	print_new_book()


def main():
	init_app()
	handle_main_menu()


if __name__ == "__main__":
	main()

