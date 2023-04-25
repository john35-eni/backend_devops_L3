from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.historique_model import Historique
from app.schemas.historique_schema import HistoriqueCreate, HistoriqueUpdate

class HistoriqueService:
    @staticmethod
    async def list_historique(user: User) -> List[Historique]:
        historique = await Historique.find(Historique.createur.id == user.id).to_list()
        return historique
    
    @staticmethod
    async def create_historique(user: User, data: HistoriqueCreate) -> Historique:
        historique = Historique(**data.dict(), createur=user)
        return await historique.insert()

    @staticmethod
    async def retrieve_historique(current_user: User, historique_id: UUID) -> Historique:
        historique = await Historique.find_one(Historique.createur.id == current_user.id, Historique.historique_id == historique_id)
        return historique

    @staticmethod
    async def update_historique(current_user: User, historique_id: UUID, data: HistoriqueUpdate):
        historique = await HistoriqueService.retrieve_historique(current_user, historique_id)
        await historique.update({"$set" : data.dict(exclude_unset=True)})

        await historique.save()
        return historique

    @staticmethod
    async def delete_historique(current_user: User, historique_id: UUID):
        historique = await HistoriqueService.retrieve_historique(current_user, historique_id)
        if historique:
            await historique.delete()
        return None        