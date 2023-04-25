from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.transfer_model import Transfer
from app.schemas.transfer_schema import TransferCreate, TransferUpdate

class TransferService:
    @staticmethod
    async def list_transfer(user: User) -> List[Transfer]:
        transfer = await Transfer.find(Transfer.destinateur == user.user_id).to_list()
        return transfer
    
    @staticmethod
    async def create_transfer(user: User, data: TransferCreate) -> Transfer:
        transfer = Transfer(**data.dict(), createur=user)
        return await transfer.insert()

    @staticmethod
    async def retrieve_transfer(current_user: User, transfer_id: UUID) -> Transfer:
        transfer = await Transfer.find_one(Transfer.destinateur == current_user.user_id, Transfer.transfer_id == transfer_id)
        return transfer

    @staticmethod
    async def update_transfer(current_user: User, transfer_id: UUID, data: TransferUpdate):
        transfer = await TransferService.retrieve_transfer(current_user, transfer_id)
        await transfer.update({"$set" : data.dict(exclude_unset=True)})

        await transfer.save()
        return transfer

    @staticmethod
    async def delete_transfer(current_user: User, transfer_id: UUID):
        transfer = await TransferService.retrieve_transfer(current_user, transfer_id)
        if transfer:
            await transfer.delete()
        return None        