# coding: utf-8
import console

from booklib.book import Book
from booklib.booklist import BookList

# from book import Book
# for Pythonista this method is working with __init__.py present in the same dir

def TestCase1():
	b1 = Book('Herding cats', 'Hank Reinwater')
	print(b1.__doc__)
	
	Unread = BookList()
	Unread.title = 'Непрочитанное'
	print(Unread.__doc__)
	
	
def TestCase2():
	b1 = Book('Herding cats', 'Hank Reinwater')
	b1.pages = 312
	b2 = Book('Deadline', 'Tom DeMarco')
	b3 = Book('Refactoring', 'Martin Fowler')


	Unread = BookList()
	Unread.title = 'Непрочитанное'

	Unread.AddBook(b1)
	Unread.AddBook(b2)
	Unread.AddBook(b3)
	Unread.ViewBooks()

	print('\n')

	Reading = BookList()
	Reading.title = 'Читаемое'
	Reading.AddBook(Unread.GetBook('Deadline'))
	Reading.ViewBooks()

console.clear()
TestCase1()