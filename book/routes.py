from fastapi import APIRouter, status
from Basic_project_Fastapi.book.book_data import books
from Basic_project_Fastapi.book.schema import Book, BookUpdateModel
from typing import List
from fastapi.exceptions import HTTPException

book_router= APIRouter()





@book_router.get('/', response_model =List[Book])
def get_all_book():
    return books


@book_router.post('/', status_code= status.HTTP_201_CREATED)
def create_book(book_data:Book):
    new_book = book_data.model_dump()

    books.append(new_book)
    return new_book



@book_router.get('/{book_id}')
def get_book(book_id:int):
    for book in books:
        if book['id']== book_id:
            return book
        
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Book Not Found")


@book_router.patch('/{book_id}')
def update_book(book_id:int, book_update_data: BookUpdateModel):
    for book in books:
        if book['id']== book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['langauge'] = book_update_data.langauge

            return book
        
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Book not found")

        

@book_router.delete('/{book_id}')
def delete_book(book_id:int):
    for book in books:
        if book['id']== book_id:
            books.remove(book)

            return{}
        
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Book not found")
        