from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str

class Punishment(BaseModel):
    user_id: str
    type: str  # "ban" or "warn"
    reason: str
