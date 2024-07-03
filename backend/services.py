import asyncio
from database import addUser

async def createUser(username):
    try:
        await addUser(username)
        print(f"Created user with name '{username}'")
    except Exception as e:
        print(f"Failed to create user: {e}")
