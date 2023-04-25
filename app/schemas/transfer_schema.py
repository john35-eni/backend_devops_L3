from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class TransferCreate(BaseModel):
    todo_id: UUID
    couleur: str = Field(..., title='Title', max_length=55, min_length=3)
    marque: str = Field(..., title='Title', max_length=55, min_length=3)
    quantite: float
    restant: float
    description: str = Field(..., title='Title', max_length=755, min_length=1)
    destinateur: UUID
    envoyeur: UUID

class TransferUpdate(BaseModel):
    couleur: Optional[str] = Field(..., title='Title', max_length=55, min_length=1)
    marque: Optional[str] = Field(..., title='Title', max_length=55, min_length=1)
    quantite: Optional[float]
    restant: Optional[float]
    description: Optional[str] = Field(..., title='Title', max_length=755, min_length=1)

class TransferOut(BaseModel):
    transfer_id: UUID 
    todo_id: UUID
    couleur: str
    marque: str
    quantite: float
    restant: float
    description: str 
    created_at : datetime
    updated_at : datetime
    destinateur : UUID
    envoyeur: UUID
