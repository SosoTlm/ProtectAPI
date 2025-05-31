from fastapi import FastAPI
from routes import users, moderation

app = FastAPI(title="ProtectAPI", version="1.0.0")

app.include_router(users.router, prefix="/users")
app.include_router(moderation.router, prefix="/moderation")

@app.get("/")
def root():
    return {"status": "ProtectAPI is up and running!"}
