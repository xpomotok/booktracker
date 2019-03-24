# coding: utf-8
""" Модуль для работы со списками книг 

		Можно менять порядок книг
"""

class BookList(object):
	""" Класс для хранения упорядочиваемого списка книг """
	def __init__(self):
		self.title = 'Simple'
		self.count = 0
		self.books = {}
		self.order = list()
		
	def __getitem__(self, key):
		return self.books[key]
							
	def AddBook(self, book):
		if book.name not in self.books:
			self.count += 1
			self.books[book.name] = book
			# self.order.append(book.name)
			self.order += [book.name]
			
	def GetBook(self, bookname):
		if bookname in self.books:
			return self.books[bookname]
			
	def RemoveBook(self, bookname):
		if bookname in self.books:
				index = self.order.index(bookname)
				del self.books[bookname]
				del self.order[index]
				self.count -= 1
				#self.MoveUp(self.order[index])
				
	def MoveUp(self, bookname):
		index = self.order.index(bookname)
		if index > 0:
			index2 = index - 1
			self.order[index] = self.order[index2]
			self.order[index2] = bookname
	
	def MoveDown(self, bookname):
		index = self.order.index(bookname)
		if index < self.count:
			index2 = index + 1
			self.order[index] = self.order[index2]
			self.order[index2] = bookname
			
	def ViewBooks(self):
		print(self.title)
		for i, bookname in enumerate(self.order):
			print('Книга #%d:'%i)
			self.books[bookname].ViewDetails()