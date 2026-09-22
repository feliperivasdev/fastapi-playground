from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Initializing the server with uvicorn users:app --reload

#entidad user
class User(BaseModel):
    id: int
    name: str
    email: str

users = [User(id=1, name="John Doe", email="john.doe@example.com"),
         User(id=2, name="Jane Smith", email="jane.smith@example.com"),
         User(id=3, name="Alice Johnson", email="alice.johnson@example.com")]

@app.get("/users")
async def read_users():
    return {"users": users}

@app.get("/users/{user_id}")
async def read_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return {"user": user}
    return {"error": "User not found"}