import percy
import unittest

class bookEntry(unittest.TestCase):
  title = "Harry Potter and the Sorcerer's Stone"
  author = "J.K. Rowling"
  owned = "o"
  start = "3/4/2010"
  end = "3/23/2010"
  physical = "Hardcover"
  date = "1997"

  def testBookCreation(self):
    testBook = percy.Book(self.title,self.author,self.owned,self.start,self.end,self.physical,self.date)
    self.assertEqual(self.title,testBook.title)
    self.assertEqual(self.author,testBook.author)
    self.assertEqual(self.owned,testBook.owned)
    self.assertEqual(self.start,testBook.start)
    self.assertEqual(self.end,testBook.end)
    self.assertEqual(self.physical,testBook.physical)
    self.assertEqual(self.date,testBook.date)

if __name__ == "__main__":
  unittest.main()
