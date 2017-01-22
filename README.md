## Apollo

Percival is a little script I've hacked together to search through a Markdown list of books (and soon: movies).

#### Reading List

Given a book list in Markdown table form:

    |Title|Author|Owned|Date Begun|Date Finished|Medium|First Published|
    |:----|:-----|:----|:---------|:------------|:-----|:--------------|
    |The Long Dark Teatime of the Soul|Douglas Adams|-|-|-|-|-|
    |V.|Thomas Pynchon|x|8/21/2014|9/3/2014|Paperback|1963|
    |The Mirror Empire|Kameron Hurley|x|9/3/2014|9/5/2014|Ebook|2014|
    |The Name of the Wind|Patrick Rothfuss|o|9/5/2014|9/8/2014|Hardcover|2007|
    |Arundel|Kenneth Roberts|x|8/18/2015|pending|Paperback|1929| 

You can search by author, publication date, title, and the year in which you read the book:

  - -h, (show this help message and exit)
  - -a AUTHOR, (Search by author)
  - -p PUBLISHED, (Search by publication date)
  - -t TITLE, (Search by title)
  - -y YEAR, (Search by reading year)
  - --stats (Get stats)
  - --list (List all books)

#### Movie Watch List

Coming soon.
