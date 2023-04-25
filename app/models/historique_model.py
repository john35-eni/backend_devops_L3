from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field, EmailStr
from .user_model import User

class Historique(Document):
    historique_id: UUID = Field(default_factory=uuid4, unique = True)
    todo_id: UUID
    couleur: Indexed(str)
    marque: Indexed(str)
    quantite: float
    description: str = None
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    destinateur : UUID
    createur : Link[User]

    def __repr__(self) -> str:
        return f"<Historique {self.couleur}>"

    def __str__(self) -> str:
        return self.couleur

    def __hash__(self) -> int:
        return hash(self.couleur)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Historique):
            return self.historique_id == other.historique_id
        return False
    
    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at= datetime.utcnow()

    class Collection:
        name = "historique"    
