class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print("{}, written by {}".format(self.title, self.author))


# Instantiate two objects
book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Print objects using display() function
book1.display()
book2.display()