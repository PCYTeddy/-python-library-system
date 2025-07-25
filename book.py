from pprint import pprint


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    # 显示书籍信息
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print("----------------------")


if __name__ == "__main__":

    pprint(Book.__dict__)