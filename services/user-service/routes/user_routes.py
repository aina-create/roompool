from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])

# -------- Data Model --------
class User(BaseModel):
    name: str
    email: str
    role: str   # seeker or owner

# Temporary storage (later will be database)
users = []


# -------- Routes --------

# Register a new user
@router.post("/register")
def register_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }
    users.append(new_user)
    return {
        "message": "User registered successfully",
        "user": new_user
    }


# Get all users
@router.get("/")
def get_all_users():
    return users


# Get user by ID
@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
