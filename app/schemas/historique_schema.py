from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class HistoriqueCreate(BaseModel):
    todo_id: UUID
    couleur: str = Field(..., title='Title', max_length=55, min_length=3)
    marque: str = Field(..., title='Title', max_length=55, min_length=3)
    quantite: float
    description: str = Field(..., title='Title', max_length=755, min_length=1)
    destinateur: UUID

class HistoriqueUpdate(BaseModel):
    couleur: Optional[str] = Field(..., title='Title', max_length=55, min_length=1)
    marque: Optional[str] = Field(..., title='Title', max_length=55, min_length=1)
    quantite: Optional[float]
    description: Optional[str] = Field(..., title='Title', max_length=755, min_length=1)

class HistoriqueOut(BaseModel):
    historique_id: UUID 
    todo_id: UUID
    couleur: str
    marque: str
    quantite: float
    description: str 
    created_at : datetime
    updated_at : datetime
    destinateur : UUID
