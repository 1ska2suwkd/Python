"""
1. 프로그램 요구사항

기능:
    1. 책 등록
    2. 책 검색
    3. 책 대여
    4. 책 반납
    5. 대여 현황 확인

2. 프로그램 설계

클래스 설계
1. Book 클래스:
    - 책의 제목, 저자, ISBN, 대여 여부를 속성으로 가짐.
2. Library 클래스:
    - 책 목록(리스트)을 관리.
    - 책 등록, 검색, 대여, 반납, 대여 현황 출력 기능 포함.
"""

class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_rented = False
        
    def __str__(self):
        status = "대여중" if self.is_rented else "이용 가능"
        return f"[{self.isbn}] {self.title} - {self.author} ({status})"

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self,title,author,isbn):
        new_book = Book(title,author,isbn)
        self.books.append(new_book)
        print(f"책 '{title}'이(가) 등록되었습니다.") #add_book의 매개변수인 title임 self.title은 Book의 속성
        
    def search_books(self,keyword):
        print(f"'{keyword}' 검색 결과:")
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)

    def rent_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_rented:
                    book.is_rented = True
                    print(f"책 '{book.title}'을(를) 대여했습니다.")
                else:
                    print(f"책 '{book.title}'은(는) 이미 대여 중입니다.")
                return
        print(f"ISBN이 '{isbn}'인 책을 찾을 수 없습니다.")
        
    def return_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_rented:
                    book.is_rented = False
                    print(f"책 '{book.title}'을(를) 반납했습니다.")
                else:
                    print(f"책 '{book.title}'은(는) 대여되지 않았습니다.")
                return
        print(f"ISBN이 '{isbn}'인 책을 찾을 수 없습니다.")
        
    def show_rent_status(self):
        print("대여 현황:")
        for book in self.books:
            if book.is_rented:
                print(book)
                
library = Library()

library.show_rent_status()

library.add_book("쉽게 풀어쓴 C언어 Expreess","천인국","978-89-7050-667-8")
library.add_book("Do it! 점프 투 파이썬","박응용","979-11-6303-091-1")

library.search_books("쉽게 풀어쓴 C언어 Expreess")
library.search_books("박응용")

library.rent_book("978-89-7050-667-8")
library.rent_book("978-89-7050-667-8")
library.rent_book("979-11-6303-091-1")

library.return_book("978-89-7050-667-8")
library.show_rent_status()