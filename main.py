from book import Book
from library import Library

def main():
    library = Library()

    # 添加书籍
    book1=Book("Python编程：从入门到实践","埃里克·马瑟斯","978-7115427547")
    book2=Book("深入浅出Python","马库斯·奥尔松","978-7115427554")
    library.add_book(book1)
    library.add_book(book2)

    # 查找书籍
    found_book=library.find_book("978-7115427547")
    if found_book:
        print("找到书籍：")
        found_book.display_info()
    else:
        print("未找到该书籍。")

    # 列出所有书籍
    print("所有书籍：")
    library.list_books()

if __name__ == '__main__':
    main()