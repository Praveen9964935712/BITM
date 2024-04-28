class Book:
    def _init_(self,title,quantity,author,price):
        self.title=title
        self.quantity=quantity
        self.author=author
        self.price=price
    def _repr_(self):
        return f"Book: {self.title},Quantity: {self.quantity},Author:{self.author},Price:{self.price}"
    
book1=Book('Book 1',12,'author 1',120)
book2=Book('Book 2',18,'author 2',220)
book3=Book('Book 3',22,'author 3',320)
    
print(book1)
print(book2)
print(book3)
    