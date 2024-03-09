class Author:
    members = []  # class variable to track all members

    def __init__(self, name: str):
        self.name = name
        self.related_contracts = []  # a list to track related contracts
        self.related_books = []  # a list to track related books using the Contract class as an intermediary
        self.members.append(self)  # add the instance to the members list

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.related_contracts.append(contract)
        self.related_books.append(book)
        return contract
    
    def books(self):
        return self.related_books
    
    def contracts(self):
        return self.related_contracts

    def total_royalties(self):
        return sum([contract.royalties for contract in self.related_contracts])

class Book:
    members = []  # class variable to track all members

    def __init__(self, title: str):
        self.title = title
        self.related_contracts = []  # a list to track related contracts
        self.members.append(self)  # add the instance to the members list
        self.book_authors = []

    def contracts(self):
        return self.related_contracts
    
    def authors(self):
        return self.book_authors

class Contract:
    members = []  # class variable to track all members

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) and not isinstance(royalties, float):
            raise Exception("Royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.members.append(self)  # add the instance to the members list
    def get_unique_identifier(self):
        # Return a unique identifier for the contract
        return self.date
    
    @classmethod
    def contracts_by_date(cls, date):
        contracts = [contract for contract in cls.members if contract.date == date]
        sorted_contracts = sorted(contracts, key=lambda contract: contract.get_unique_identifier())
        return sorted_contracts