#  Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation. 



class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        
    def BookDescription(self):
        print(f"The book {self.title} was written by {self.author} and it goes for ${self.price} on all bookshops")
    
    
    
class Novel(Book):
        def __init__(self,title,author,price):
            super(). __init__(title,author,price)   
    
book1=Book("the river and the source","Margret Ogolla",20)   
book1.BookDescription() 


book2=Novel("becoming","mitchelle obama",30)
book2.BookDescription()