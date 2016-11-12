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
  def returnReadingYears(self):
    yearS = self.start.split('/')
    yearE = self.end.split('/')
    if len(yearS) and len(yearE) == 3:
      return [yearS[2], yearE[2]]
    else:
      return []
  def returnAllInfo(self):
    return [self.title, self.author, self.owned, self.start, self.end, self.physical, self.date, self.readTime()]
  def returnFormatted(self):
    print self.title + ' by ' + self.author
    print 'Owned: ' + self.owned
    print 'Started: ' + self.start
    print 'Finished: ' + self.end
    print 'Format: ' + self.physical
    print 'First Published: ' + self.date
    print self.readTime()
    print

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
    if currentBook.physical == 'Paperback' or format == 'Hardcover':
      totalPhysical += 1
    elif currentBook.physical == 'Ebook':
      totalEbooks += 1
    if currentBook.owned == 'x':
      totalOwned += 1
    elif currentBook.owned == 'o':
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
    currentBook = Book(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
    if option == 't':
      if search in currentBook.title:
        currentBook.returnFormatted()
    elif option == 'y':
      if currentBook.start and currentBook.end != '-':
        if search in currentBook.returnReadingYears():
          currentBook.returnFormatted()
    elif option == 'a':
      if search in currentBook.author:
        currentBook.returnFormatted()
    elif option == 'p':
      if search == currentBook.date:
        currentBook.returnFormatted()
    elif option == '--list':
      currentBook.returnFormatted()

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
