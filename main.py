from fastapi import FastAPI, HTTPException

from models import Editorial, Libro

app = FastAPI(title="API Biblioteca")

editoriales = [
    Editorial(idEd=1, nombre="Prentice Hall", pais="USA"),
    Editorial(idEd=2, nombre="Addison-Wesley Professional", pais="USA"),
    Editorial(idEd=3, nombre="The MIT Press", pais="USA"),
]

libros = [
    Libro(ISBN="9780132350884", titulo="Clean Code: A Handbook of Agile Software Craftsmanship", autor="Robert C. Martin", precio=48.00, idEd=1),
    Libro(ISBN="9780135957059", titulo="The Pragmatic Programmer: Your Journey to Mastery", autor="Andrew Hunt, David Thomas", precio=50.00, idEd=1),
    Libro(ISBN="9780201633610", titulo="Design Patterns: Elements of Reusable Object-Oriented Software", autor="Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", precio=55.00, idEd=2),
    Libro(ISBN="9780134757599", titulo="Refactoring: Improving the Design of Existing Code", autor="Martin Fowler", precio=52.00, idEd=2),
    Libro(ISBN="9780262046305", titulo="Introduction to Algorithms (4th Edition)", autor="Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein", precio=95.00, idEd=3),
]


@app.get("/")
def read_root():
    return {"message": "API Biblioteca - bienvenido"}


@app.get("/libros")
def get_libros():
    return libros


@app.get("/libros/{isbn}")
def get_libro(isbn: str):
    """Consulta un libro por su ISBN. Lanza 404 si no existe."""
    for libro in libros:
        if libro.ISBN == isbn:
            return libro
    raise HTTPException(status_code=404, detail="Libro no registrado")


@app.post("/libros")
def create_libro(libro: Libro):
    libros.append(libro)
    return libro


@app.get("/editoriales")
def get_editoriales():
    return editoriales


@app.get("/editoriales/{id_ed}")
def get_editorial(id_ed: int):
    """Consulta una editorial por su idEd. Lanza 404 si no existe."""
    for editorial in editoriales:
        if editorial.idEd == id_ed:
            return editorial
    raise HTTPException(status_code=404, detail="Editorial no registrada")