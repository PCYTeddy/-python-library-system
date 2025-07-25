import json
from book import Book

class Library:
    def __init__(self):
        self.books = []
        # 初始化时加载 library.json 文件中的数据。
        self.load_bolks()

    # 添加一本书并保存到文件。
    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    # 根据ISBN查找一本书。
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    # 列出所有书籍。
    def list_books(self):
        for book in self.books:
            book.display_info()

    # 将所有书籍信息保存到library.json 文件。
    def save_books(self):
        books_data=[]
        for book in self.books:
            books_data.append({
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn
            })
        with open('library.json', 'w',encoding='utf-8') as file:
            json.dump(books_data,file,indent=4,ensure_ascii=False)

    # 从 library.json 文件加载书籍数据。
    def load_bolks(self):
        try:
            with open('library.json') as file:
                books_data=json.load(file)
                for book_info in books_data:
                    book=Book(**book_info)
                    self.books.append(book)
        except FileNotFoundError:
            pass # 如果文件不存在，则初始化为空列表
