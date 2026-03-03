'''
One principle that's violated is Liscov Substitution. The PublicReadingLibrary class is a subclass of Library, but it doesn't implement the lend_book method. This means that if we try to use a PublicReadingLibrary object in place of a Library object, it will not work as expected.
'''

class Library:
    def __init__(self):
        self.books = []
        self.borrowed = []

    def add_book(self, title, author, year):
        self.books.append((title, author, year))

    def lend_book(self, title, author, year):
        loaned = None
        for i, (t, a, y) in enumerate(self.books):
            if t == title and a == author and y == year:
                loaned = i
        if loaned is not None:
           self.borrowed.append(self.books[loaned])
           del self.books[loaned]

    def display_book(self, idx):
        title, author, year = self.books[idx]
        return f'Title: {title}, Author: {author}, Year:  {year}'

class PublicReadingLibrary(Library):
    def lend_book(self, title, author, year):
        # raise NotImplementedError()
        '''
        you can fix this by either putting
        `pass` or by calling the parent method using `super()`
        '''
        return super().lend_book(title, author, year)

lib = PublicReadingLibrary()
lib.add_book('1984', 'Orwell', 1949)
print(lib.display_book(0))
lib.lend_book('1984', 'Orwell', 1949)
