from fastapi import APIRouter, Depends
from models import Punishment
from utils.auth import verify_token

router = APIRouter()

@router.post("/punish")
def punish(punishment: Punishment, _: str = Depends(verify_token)):
    return {"message": f"{punishment.type.capitalize()} issued to user {punishment.user_id} for: {punishment.reason}"}
