# coding: utf-8

from booklib.book import Book
from booklib.booklist import BookList
import json
import codecs

Library: BookList
Fname = "library.json"


class BookTracker(object):
	""" Application's main class. Class properties is used instead of global variables. """
	def __init__(self, dbfile):
		self.TrackerDb = {}
		self.ListCount = 0
		self.load_tracker(dbfile)
		
	def load_tracker(self, fname):
		tracker_dict = {}
		
		try:
			with codecs.open(fname, 'rU', 'utf-8') as f:
				# i = 0
				line = f.readline()
				tracker_dict = json.loads(line)
				
			print(tracker_dict)
				# for line in f:
				#		self.add_list(line)
			for key in tracker_dict:
				new_list = self.add_list(tracker_dict[key])
				bookfile = new_list.title+".json"
				print("Bookfile=\"{}\"".format(bookfile))
				new_list.load_books(bookfile)
					# i = i + 1
				
		except OSError as E:
			print(E.strerror)
			print("You are running app for the first time! Book tracker is empty.")

	def add_list(self, title):
		if title not in self.TrackerDb:
			new_list = BookList()
			new_list.title = title
			self.ListCount += 1
			self.TrackerDb[title] = new_list
			# new feature
			return new_list
	
	def get_list(self, title):
		# not so terrible
		if title in self.TrackerDb:
			return self.TrackerDb[title]
		else:
			return self.add_list(title)
		
	def del_list(self, title):
		if title in self.TrackerDb:
			self.TrackerDb.pop(title)

		
	def save_tracker(self, fname):
		i = 0
		tracker_dict = {}
		if self.ListCount != 0:
			with open(fname, "w") as f:
				for key, value in self.TrackerDb.items():
					# save lists
					tracker_dict[i] = value.title
					# f.write(value.title)
					# save list contents
					value.save_books(value.title+'.json')
					i = i + 1
				
				print(json.dumps(tracker_dict, indent=4))
				js = json.dumps(tracker_dict)
				
				f.write(js)
			print("Lists saved: ", i)
			
	def show_tracker(self):
		for title in self.TrackerDb:
			print(self.TrackerDb[title].title)
	
	# optional
	def show_tracker_dbg(self):
		print("Lists count: {}".format(self.ListCount))
		for list_item in self.TrackerDb.items():
				print(list_item)
		pass


def TestCase21():
	# import console
	# console.clear()
	
	tracker = BookTracker(Fname)
	# Tracker.show_tracker()
	# Tracker.add_list('Unread')
	# Tracker.add_list('My library')
	newbook = Book('Steven King','It!')
	unread = tracker.get_list('Unread')
	print(unread)
	unread.AddBook(newbook)
	
	tracker.show_tracker()

	# tracker.del_list(unread.title)
	tracker.save_tracker(Fname)
	
	
if __name__ == "__main__":
	TestCase21()

