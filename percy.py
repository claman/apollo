#!/usr/local/bin/python2.7
import argparse
import datetime
import yaml
file = open('example.txt', 'r') # change this to correspond to your list

def getYear(date):
  slashDate = date.split('/')
  year = slashDate[2]
  return year
def readTime(start, end):
  try:
    start = start.split('/')
    end = end.split('/')
    startDate = datetime.date(int(start[2]), int(start[0]), int(start[1]))
    endDate = datetime.date(int(end[2]), int(end[0]), int(end[1]))
    readingTime = endDate - startDate
    return 'You read this in ' + str(readingTime.days) + ' days.'
  except IndexError:
    if end == 'pending':
      return 'You are currently reading this.'
    else:
      return 'You haven\'t read this yet.'
def getInfo(title, author, owned, start, end, format, date):
  print title + ' by ' + author
  print 'Owned: ' + owned
  print 'Started: ' + start
  print 'Finished: ' + end
  print 'Format: ' + format
  print 'First Published: ' + date
  print readTime(start, end)
  print
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
def stats():
  totalBooks, totalPhysical, totalEbooks = 0, 0, 0
  totalRead, totalOwned, totalBorrowed = 0, 0, 0
  file.next()
  file.next()
  for line in file:
    line = line.strip('|\n')
    entry = line.split('|')
    title, author, owned, start, end, format, date = entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]
    totalBooks += 1
    if format == 'Paperback' or format == 'Hardcover':
      totalPhysical += 1
    elif format == 'Ebook':
      totalEbooks += 1
    if owned == 'x':
      totalOwned += 1
    elif owned == 'o':
      totalBorrowed += 1
    if start != '-' and end != '-':
      totalRead += 1
  print 'You have ' + str(totalBooks) + ' books on your list; you have read ' + str(totalRead) + '.'
  print 'You own ' + str(totalOwned) + ' books: ' + str(totalPhysical) \
        + ' physical (paperback or hardcover) and ' + str(totalEbooks) + ' ebooks.'
  print 'You have borrowed ' + str(totalBorrowed) + ' books.'
def addBook():
  append = open('example.txt', 'a') # change this to correspond to your list
  title = raw_input('Title: ')
  author = raw_input('Author: ')
  owned = raw_input('Owned (x/o): ')
  start = raw_input('Date Started (ie 2/7/2014): ')
  end = raw_input('Date Finished (ie 2/10/2014): ')
  b_format = raw_input('Format: ')
  year = raw_input('Year of Publication: ')
  append.write('\n|'+str(title)+'|'+str(author)+'|'+str(owned)+'|'+str(start)+'|'+str(end)+'|'+str(b_format)+'|'+str(year)+'|')
  print 'Added '+str(title)+' by '+str(author)
  append.close()

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
