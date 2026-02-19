from models.user_model import User

# Temporary in-memory storage
users = []

def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }
    users.append(new_user)
    return new_user


def get_all_users():
    return users


def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
