import asyncio
from .database import addUser, addBook, editBook, editUser, create_users_table, create_books_table, create_issues_table, getAllUsers, getAllBooks


async def init():
    await create_users_table()
    await create_books_table()
    await create_issues_table()

asyncio.run(init())

async def createMember(username):
    try:
        await addUser(username)
        print(f"Created user with name '{username}'")
    except Exception as e:
        print(f"Failed to create user: {e}")


async def updateMember(user_id, new_name):
    """
    Updates the name of a user with the given user_id.

    :param user_id: int, The ID of the user to be updated.
    :param new_name: str, The new name of the user.
    """
    try:
        await editUser(user_id, new_name)
        print(f"Updated user with ID '{user_id}' - new name: '{new_name}'")
    except Exception as e:
        print(f"Failed to update user: {e}")


async def createBook(book_name, quantity, number_of_issues=0):
    try:
        await addBook(book_name, quantity, number_of_issues)
        print(f"Added book '{book_name}' with quantity '{quantity}' and number of issues '{number_of_issues}'")
    except Exception as e:
        print(f"Failed to add book: {e}")


async def updateBook(book_id, new_quantity, new_book_name):
    """
    Updates the quantity and name of a book with the given book_id.

    :param book_id: int, The ID of the book to be updated.
    :param new_quantity: int, The new quantity of the book.
    :param new_book_name: str, The new name of the book.
    """
    try:
        await editBook(book_id, new_quantity, new_book_name)
        print(f"Updated book with ID '{book_id}' - new quantity: {new_quantity}, new book name: {new_book_name}")
    except Exception as e:
        print(f"Failed to update book: {e}")


async def fetchAllUsers():
    try:
        users = await getAllUsers()
        print("All users:", users)
        return users
    except Exception as e:
        print(f"Failed to fetch users: {e}")
        return []

async def fetchAllBooks():
    try:
        books = await getAllBooks()
        print("All books:", books)
        return books
    except Exception as e:
        print(f"Failed to fetch books: {e}")
        return []