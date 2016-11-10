#!/usr/bin/env python
import argparse
import datetime
file = open('example.txt', 'r') # change this to correspond to your list

class Book:
  def __init__(self, title, author, owned, start, end, physical, date):
    self.title = title
    self.author = author
    self.owned = owned
    self.start = start
    self.end = end
    self.physical = physical
    self.date = date
  def readTime(self):
    try:
      start = self.start.split('/')
      end = self.end.split('/')
      startDate = datetime.date(int(start[2]), int(start[0]), int(start[1]))
      endDate = datetime.date(int(end[2]), int(end[0]), int(end[1]))
      readingTime = endDate - startDate
      return 'You read this in ' + str(readingTime.days) + ' days.'
    except IndexError:
      return 'Unread or current'
  def returnAllInfo(self):
    return [self.title, self.author, self.owned, self.start, self.end, self.physical, self.date, self.readTime()]
  def returnType(self):
    return self.physical
  def returnOwnedStatus(self):
    return self.owned

def stats():
  totalBooks, totalPhysical, totalEbooks = 0, 0, 0
  totalRead, totalOwned, totalBorrowed = 0, 0, 0
  file.next()
  file.next()
  for line in file:
    line = line.strip('|\n')
    entry = line.split('|')
    currentBook = Book(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
    totalBooks += 1
    if currentBook.returnType() == 'Paperback' or format == 'Hardcover':
      totalPhysical += 1
    elif currentBook.returnType() == 'Ebook':
      totalEbooks += 1
    if currentBook.returnOwnedStatus() == 'x':
      totalOwned += 1
    elif currentBook.returnOwnedStatus() == 'o':
      totalBorrowed += 1
    readStatus = currentBook.returnAllInfo()
    if readStatus[7] != 'Unread or current':
      totalRead += 1
  print 'You have ' + str(totalBooks) + ' books on your list; you have read ' + str(totalRead) + '.'
  print 'You own ' + str(totalOwned) + ' books: ' + str(totalPhysical) \
        + ' physical (paperback or hardcover) and ' + str(totalEbooks) + ' ebooks.'
  print 'You have borrowed ' + str(totalBorrowed) + ' books.'

def search(option, search):
  file.next()
  file.next()
  for line in file:
    line = line.strip('|\n')
    entry = line.split('|')
    title, author, owned, start, end, format, date = entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]
    if option == 't':
      if search in title:
        getInfo(title, author, owned, start, end, format, date)
    elif option == 'y':
      if start and end != '-':
        if search == getYear(start) or search == getYear(end):
          getInfo(title, author, owned, start, end, format, date)
    elif option == 'a':
      search = search.title()
      if search in author:
        getInfo(title, author, owned, start, end, format, date)
    elif option == 'p':
      if search == date:
        getInfo(title, author, owned, start, end, format, date)
    elif option == '--list':
      getInfo(title, author, owned, start, end, format, date)



parser = argparse.ArgumentParser(description='List books based on queries.')
parser.add_argument('-a', help='Search by author')
parser.add_argument('-p', help='Search by publication date')
parser.add_argument('-t', help='Search by title')
parser.add_argument('-y', help='Search by reading year')
parser.add_argument('--stats', action='store_true', help='Show stats about list (no argument)')
parser.add_argument('--add', action='store_true', help='Add book (no argument)')
parser.add_argument('--list', action='store_true', help='List all books')
args = parser.parse_args()
if args.t:
  search('t', args.t)
elif args.y:
  search('y', args.y)
elif args.a:
  search('a', args.a)
elif args.p:
  search('p', args.p)
elif args.stats:
  stats()
elif args.add:
  addBook()
elif args.list:
  search('--list', '')
else:
  print 'Try running again with \'-h\''

file.close()
