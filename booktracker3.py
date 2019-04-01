# coding: utf-8
# import console

from booklib.book import Book
from booklib.booklist import BookList

# from book import Book
# for Pythonista this method is working with __init__.py present in the same dir


def test_case1():
	b1 = Book('Herding cats', 'Hank Reinwater')
	print(b1.__doc__)
	
	unread = BookList()
	unread.title = 'Непрочитанное'
	print(unread.__doc__)
	
	
def test_case2():
	b1 = Book('Herding cats', 'Hank Reinwater')
	b1.pages = 312
	b2 = Book('Deadline', 'Tom DeMarco')
	b3 = Book('Refactoring', 'Martin Fowler')

	unread = BookList()
	unread.title = 'Непрочитанное'

	unread.AddBook(b1)
	unread.AddBook(b2)
	unread.AddBook(b3)
	unread.ViewBooks()

	print('\n')

	reading = BookList()
	reading.title = 'Читаемое'
	reading.AddBook(unread.GetBook('Deadline'))
	reading.ViewBooks()

def test_case2():
	b1 = Book('Herding cats', 'Hank Reinwater')
	b1.pages = 312
	b2 = Book('Deadline', 'Tom DeMarco')
	b3 = Book('Refactoring', 'Martin Fowler')

	unread = BookList()
	unread.title = 'Непрочитанное'

	unread.AddBook(b1)
	unread.AddBook(b2)
	unread.AddBook(b3)
	unread.ViewBooks()

	print('\n')

	reading = BookList()
	reading.title = 'Читаемое'
	reading.AddBook(unread.GetBook('Deadline'))
	reading.ViewBooks()


def test_case3():
	b1 = Book('Herding cats', 'Hank Reinwater')
	b1.pages = 312
	b2 = Book('Deadline', 'Tom DeMarco')
	b3 = Book('Refactoring', 'Martin Fowler')

	unread = BookList()
	unread.title = 'Непрочитанное'

	unread.AddBook(b1)
	unread.AddBook(b2)
	unread.AddBook(b3)
	unread.ViewBooks()

	unread.save_books("unread_books.txt")


if __name__ == "__main__":
	# console.clear()
	# test_case1()
	test_case3()