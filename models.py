from dataclasses import Field

from pydantic import BaseModel, Field
class Book(BaseModel):
    id: int = Field(..., description="Identificador unico del libro")
    title: str = Field(..., description="Titulo del libro")
    author: str = Field(..., description="Autor del libro")
    year: int = Field(..., description="Año de publicacion")
