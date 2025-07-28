import json
from book import Book

class Library:
    def __init__(self):
        self.books = []
        # 初始化时加载 library.json 文件中的数据。
        self.load_books()

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
    def load_books(self):
        try:
            with open('library.json',"r",encoding="utf-8") as file:
                # 检查文件是否为空
                content=file.read()

                ## 文件为空的处理：
                # 检查文件是否为空。如果文件为空，打印警告信息并返回，避免后续处理。
                # strip()去除字符串首尾的空白字符（包括换行符、空格等）。
                # if not content.strip():
                #     print("警告：library.json文件为空，初始化为空列表")
                #     return None

                # 将指针放回文件开头
                # file.read()读取文件后，文件指针位于文件末尾。file.seek(0)将文件指针移动到文件开头，以便后续读取操作（如json.load(file)）能够正确读取文件内容。
                file.seek(0)
                books_data=json.load(file)
                for book_info in books_data:
                    book=Book(**book_info)
                    self.books.append(book)
        # # 文件为空或非有效json格式处理
        # 如果文件内容不是有效的JSON格式，捕获json.JSONDecodeError异常。
        except json.JSONDecodeError:
            print("警告：library.json 文件非有效json格式或文件为空，初始化为空列表。")
            self.books = []

        except FileNotFoundError:
            pass # 如果文件不存在，则初始化为空列表
