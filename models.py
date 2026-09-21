from pydantic import BaseModel, Field


class Editorial(BaseModel):
    idEd: int = Field(..., description="Identificador único de la editorial")
    nombre: str = Field(..., description="Nombre de la editorial")
    pais: str = Field(..., description="País de la editorial")


class Libro(BaseModel):
    ISBN: str = Field(..., description="Código ISBN del libro")
    titulo: str = Field(..., description="Título del libro")
    autor: str = Field(..., description="Autor del libro")
    precio: float = Field(..., description="Precio del libro")
    idEd: int = Field(..., description="idEd de la editorial que lo publica")