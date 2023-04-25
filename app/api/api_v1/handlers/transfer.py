from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.models.transfer_model import Transfer
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.transfer_schema import TransferOut, TransferCreate, TransferUpdate
from app.services.transfer_service import TransferService


transfer_router = APIRouter()

@transfer_router.get('/', summary="Get all transfer of the user ", response_model=List[Transfer])
async def list(current_user: User = Depends(get_current_user)):
    return await TransferService.list_transfer(current_user)


@transfer_router.post('/create', summary="Create Transfer", response_model=Transfer)
async def create_transfer(data: TransferCreate, current_user: User = Depends(get_current_user)):
    return await TransferService.create_transfer(current_user, data)


@transfer_router.get('/{transfer_id}', summary="Get transfer by transfer_id", response_model=Transfer)
async def retrieve(transfer_id: UUID, current_user: User = Depends(get_current_user)):
    return await TransferService.retrieve_transfer(current_user, transfer_id)

@transfer_router.put('/{transfer_id}', summary="Update transfer by transfer_id", response_model=TransferOut)
async def update(transfer_id: UUID, data: TransferUpdate, current_user: User= Depends(get_current_user)):
    return await TransferService.update_transfer(current_user, transfer_id, data)


@transfer_router.delete('/{transfer_id}', summary="Delete transfer by transfer_id")
async def delete(transfer_id: UUID, current_user: User = Depends(get_current_user)):
    await TransferService.delete_transfer(current_user, transfer_id)
    return None