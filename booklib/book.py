# coding: utf-8

""" Модуль для работы с книгами """

class Book(object):
	""" Класс представления моих книг """
	def __init__(self, name, author):
		self.author = author
		self.name = name
		self.pages = 0
		self.progress = None
		# self.bookmarks = {}
		
	def ViewDetails(self):
		print("Книга \"%s\" автора %s"%(self.name,self.author))
		
	def ViewProgress(self):
		if self.progress:
			print("Прочитано %d страниц"%(self.progress))
		else:
			print('Даже не приступал')
		
	def SetProgress(self, newProgress):
		if newProgress <= self.pages:
			if newProgress >= self.progress:
				#delta = newProgress - self.progress
				self.progress = newProgress
			else:
				print('Регресс в чтении книг невозможен')
		else:
			print('В книге же меньше страниц!')
