class Book:
  def __init__ (self, title, author, year):
    self.title = title
    self.author = author
    self.year = year
print(f'Creating book: {self.title}')

def __del__(self):
        # Destructor: runs automatically when a Book object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation: for user-friendly display
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official representation: for recreating the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
      
my_book = Book("1984", "George Orwell", 1949)
print(my_book)          # Uses __str__ → "1984 by George Orwell, published in 1949"
print(repr(my_book))    # Uses __repr__ → "Book('1984', 'George Orwell', 1949)"
del my_book             # Uses __del__ → "Deleting 1984"
