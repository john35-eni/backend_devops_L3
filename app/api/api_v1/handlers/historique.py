from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.models.historique_model import Historique
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.historique_schema import HistoriqueOut, HistoriqueCreate, HistoriqueUpdate
from app.services.historique_service import HistoriqueService


historique_router = APIRouter()

@historique_router.get('/', summary="Get all historique of the user ", response_model=List[Historique])
async def list(current_user: User = Depends(get_current_user)):
    return await HistoriqueService.list_historique(current_user)


@historique_router.post('/create', summary="Create Historique", response_model=Historique)
async def create_historique(data: HistoriqueCreate, current_user: User = Depends(get_current_user)):
    return await HistoriqueService.create_historique(current_user, data)


@historique_router.get('/{historique_id}', summary="Get historique by historique_id", response_model=Historique)
async def retrieve(historique_id: UUID, current_user: User = Depends(get_current_user)):
    return await HistoriqueService.retrieve_historique(current_user, historique_id)

@historique_router.put('/{historique_id}', summary="Update historique by historique_id", response_model=HistoriqueOut)
async def update(historique_id: UUID, data: HistoriqueUpdate, current_user: User= Depends(get_current_user)):
    return await HistoriqueService.update_historique(current_user, historique_id, data)


@historique_router.delete('/{historique_id}', summary="Delete historique by historique_id")
async def delete(historique_id: UUID, current_user: User = Depends(get_current_user)):
    await HistoriqueService.delete_historique(current_user, historique_id)
    return None