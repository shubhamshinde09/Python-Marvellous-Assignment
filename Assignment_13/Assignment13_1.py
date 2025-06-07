class BookStore:
    NoOfBooks = 0  # Class variable

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1  # Increment class variable

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")


# Creating objects
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()  # Output: Linux System Programming by Robert Love. No of books : 1

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  # Output: C Programming by Dennis Ritchie. No of books : 2
