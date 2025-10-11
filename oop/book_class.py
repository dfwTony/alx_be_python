class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # ✅ Added the missing comma
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__(self):
        print(f"Deleting {self.title}")


# Create the object
my_book = Book("1984", "George Orwell", 1949)

# Print outputs
print(my_book)        # __str__
print(repr(my_book))  # __repr__
del my_book           # __del__
