# coding: utf-8

""" Модуль для работы с книгами """
import json


class Book(object):
	""" Класс представления для моих книг """
	def __init__(self, name, author):
		self.author = author
		self.name = name
		self.pages = 0
		self.progress = None
		# self.bookmarks = {}
		
	def view_details(self):
		print("Книга \"%s\" автора %s"%(self.name, self.author))
		
	def view_progress(self):
		if self.progress:
			print("Прочитано %d страниц"%(self.progress))
		else:
			print('Даже не приступал')
		
	def set_progress(self, newProgress):
		if newProgress <= self.pages:
			if newProgress >= self.progress:
				#delta = newProgress - self.progress
				self.progress = newProgress
			else:
				print('Регресс в чтении книг невозможен')
		else:
			print('В книге же меньше страниц!')

	def get_pages(self):
		return self.pages

	def set_pages(self, pages):
		self.pages = pages

	def serialize(self):
		# return json.dumps(self.__dict__, sort_keys=True, indent=4)
		return json.dumps(self.__dict__, sort_keys=True)

	def deserialize(self, dbstr):
		self.__dict__ = json.loads(dbstr)

