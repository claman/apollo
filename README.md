# Percival (Percry for short)

Percival is a quick and dirty little script I've hacked together to search through a Markdown list of books.

Given a markdown table formatted thusly:

|Title|Author|Owned|Date Begun|Date Finished|Medium|First Published|
|:----|:-----|:----|:---------|:------------|:-----|:--------------|
|V.|Thomas Pynchon|x|8/21/2014|9/3/2014|Paperback|1963|
|The Mirror Empire|Kameron Hurley|x|9/3/2014|9/5/2014|Paperback|2014|
|The Name of the Wind|Patrick Rothfuss|x|9/5/2014|9/8/2014|Paperback|2007|

You can search by author, publication date, title, and the year in which you read the book:

  - -h, --help  show this help message and exit
  - -a AUTHOR, --author AUTHOR  Search by author
  - -p PUBLISHED, --published PUBLISHED  Search by publication date
  - -t TITLE, --title TITLE  Search by title
  - -y YEAR, --year YEAR  Search by reading year