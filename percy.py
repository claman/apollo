#!/usr/bin/python
import argparse
file = open('your filename here', 'r') # change this to correspond to your list

def getYear(date):
  slashDate = date.split('/')
  year = slashDate[2]
  return year
def info(title, author, owned, start, end, format, date):
  print title + ' by ' + author
  print 'Owned: ' + owned
  print 'Started: ' + start
  print 'Finished: ' + end
  print 'Format: ' + format
  print 'First Published: ' + date
  print
def search(option, search):
  for line in file:
    line = line.strip('|\n')
    entry = line.split('|')
    title, author, owned, start, end, format, date = entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]
    if option == 't':
      if search in title:
	info(title, author, owned, start, end, format, date)
    elif option == 'y':
      if title != 'Title' and title != ':----' and title != '~':
	if start and end != '-':
          if search == getYear(start) or search == getYear(end):
            info(title, author, owned, start, end, format, date)
    elif option == 'a':
      search = search.title()
      if search in author:
	info(title, author, owned, start, end, format, date)
    elif option == 'p':
      if search == date:
	info(title, author, owned, start, end, format, date)
def stats():
  totalBooks = 0
  totalPhysical = 0
  totalEbooks = 0
  for line in file:
    line = line.strip('|\n')
    entry = line.split('|')
    title, author, owned, start, end, format, date = entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]
    if title != 'Title' and title != ':----' and title != '~':
      totalBooks += 1
    if format == 'Paperback' or format == 'Hardcover':
      totalPhysical += 1
    elif format == 'Ebook':
      totalEbooks += 1
  print 'You have ' + str(totalBooks) + ' books on your list.'
  print str(totalPhysical) + ' of them are physical (paperback or hardcover).'
  print str(totalEbooks) + ' of them are ebooks.'

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--author', help='Search by author')
parser.add_argument('-p', '--published', help='Search by publication date')
parser.add_argument('-t', '--title', help='Search by title')
parser.add_argument('-y', '--year', help='Search by reading year')
parser.add_argument('--stats', action='store_true')
args = parser.parse_args()
if args.title:
  search('t', args.title)
elif args.year:
  search('y', args.year)
elif args.author:
  search('a', args.author)
elif args.published:
  search('p', args.published)
elif args.stats:
  stats()
else:
  print 'Try running again with \'-h\' or \'--help\''

file.close()
