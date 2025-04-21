from fastapi import FastAPI
from Basic_project_Fastapi.book.routes import book_router

app= FastAPI()


app.include_router(book_router, prefix= "/books")