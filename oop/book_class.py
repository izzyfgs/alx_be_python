class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        # This print must be inside __init__
        print(f'Creating book: {self.title}')

    def __del__(self):
        # Destructor: runs automatically when a Book object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # User-friendly string for print()
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official representation to recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Testing the class
my_book = Book("1984", "George Orwell", 1949)
print(my_book)          # Uses __str__
print(repr(my_book))    # Uses __repr__
del my_book             # Triggers __del__
