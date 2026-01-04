from bson import ObjectId

class User:
    def __init__(self, email: str, hashed_password: str):
        self.email = email
        self.hashed_password = hashed_password


class Task:
    def __init__(self, title: str, description: str, completed: bool, owner_id: ObjectId):
        self.title = title
        self.description = description
        self.completed = completed
        self.owner_id = owner_id
