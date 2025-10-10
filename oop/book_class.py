class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Human-friendly representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Developer-friendly representation (recreatable)
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Called automatically when object is deleted
        print(f"Deleting {self.title}")