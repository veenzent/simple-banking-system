from fastapi import APIRouter, HTTPException
from schemas import users_schema
from uuid import UUID

user_router = APIRouter()


############  Reusable Functions  ############
def get_user(id: str):
    for i in users_schema.users:
        if i == id:
            return users_schema.users.get(i)
    return None
#############################################

@user_router.get("/")
async def home():
    return {"message": "Welcome to my simple banking API"}

@user_router.post("/sign up")
async def create_user(user: users_schema.UserCreate):
    id = str(UUID(int=len(users_schema.users)+1))
    new_user = {id: user}
    users_schema.users.update(new_user)
    return {"message": "User created successfully", "data": new_user}

@user_router.get("/all-users")
async def get_users():
    return users_schema.users

@user_router.get("/user/{id}")
async def get_user_by_id(id: str):
    user = get_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@user_router.put("/update/{id}")
async def update_user(id: str, user_update: users_schema.User):
    user = get_user(id)
    if user:
        users_schema.users[id] = user_update
        return {"message": "User updated successfully", "data": users_schema.users[id]}
    raise HTTPException(status_code=404, detail="User does not exist")
    