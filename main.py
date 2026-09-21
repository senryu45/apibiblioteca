from fastapi import FastAPI, HTTPException
from models import Book

app = FastAPI(title="API Biblioteca")

books = [
    Book(id = 1, title = "Cien años de soledad", author = "Gabriel Garcia Marquez", year = 1967),
    Book(id = 2, title = "Don Quijote de la Mancha", author = "Miguel de Cervantes", year = 1605),
    Book(id = 3, title = "1984", author = "George Orwell", year = 1949),
    Book(id = 4, title = "Rayuela", author = "Julio Cortazar", year = 1963),
    Book(id = 5, title = "El Principito", author = "Antoine de Saint-Exupery", year = 1943),
]
@app.get("/")
def read_root():
    return{"message": "API Biblioteca - bienvenido"}
@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code = 404, detail = "Libro no registrado")

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book