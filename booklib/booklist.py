# coding: utf-8
""" Модуль для работы со списками книг

		Можно менять порядок книг
"""

from booklib.book import Book
import codecs
import json


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
				# self.MoveUp(self.order[index])
				
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
			print('Book #%d:' % i)
			self.books[bookname].view_details()

	def toJSON(self):
		# return json.dumps(self.__dict__, sort_keys=True, indent=4)
		# return json.dumps(self.__dict__, sort_keys=True)
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

	def fromJSON(self, dbstr):
		try:
			self.__dict__ = json.loads(dbstr)
		except json.JSONDecodeError as E:
			print("%s on %d".formate(E.msg, E.lineno))
		
	def save_books(self, fname):
		# i = 0

		if self.count != 0:
			with open(fname, "w") as f:
				for i, bookname in enumerate(self.order):
					book = self.GetBook(bookname)
					f.write(book.serialize())
					f.write("\n")
					# i = i + 1
			print("Books saved: ", i+1)

	def load_books(self, fname):
		i = 0
		try:
			with codecs.open(fname, 'rU', 'utf-8') as f:
				for line in f:
					# ci_db.append(json.loads(line))
					book = Book('', '')
					book.deserialize(line)
					# ci.show()
					self.AddBook(book)
					i = i + 1
			print("Books loaded: ", i)
		except OSError as E:
			print("File not found!")

