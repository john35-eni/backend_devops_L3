from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    couleur: str = Field(..., title='Title', max_length=55, min_length=3)
    marque: str = Field(..., title='Title', max_length=55, min_length=3)
    quantite: float
    restant: float
    description: str = Field(..., title='Title', max_length=755, min_length=1)

class TodoUpdate(BaseModel):
    couleur: Optional[str] = Field(..., title='Title', max_length=55, min_length=1)
    marque: Optional[str] = Field(..., title='Title', max_length=55, min_length=1)
    quantite: Optional[float]
    restant: Optional[float]
    description: Optional[str] = Field(..., title='Title', max_length=755, min_length=1)

class TodoOut(BaseModel):
    todo_id: UUID
    couleur: str
    marque: str
    quantite: float
    restant: float
    description: str 
    created_at : datetime 
    updated_at : datetime 
