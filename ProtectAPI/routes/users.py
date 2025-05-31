from fastapi import APIRouter, Depends
from utils.auth import verify_token
from models import User

router = APIRouter()

@router.post("/add_user")
def add_user(user: User, _: str = Depends(verify_token)):
    return {"message": f"User {user.name} added!"}
