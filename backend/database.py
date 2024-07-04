import sqlite3
from concurrent.futures import ThreadPoolExecutor
import random
import asyncio

async def runQuery(query, variables):
    """
    Executes a given SQL query with the provided variables asynchronously and closes the connection.
    
    :param query: str, SQL query to be executed
    :param variables: list, List of variables to be used in the query
    :return: result of the query if it's a SELECT statement, otherwise None
    """
    def sync_query(query, variables):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        
        try:
            if "SELECT" in query.upper():
                cursor.execute(query, variables)
                result = cursor.fetchall()
                return result
            else:
                cursor.execute(query, variables)
                connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            connection.close()
    
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, sync_query, query, variables)
    

#----------------------------------------------------------------------------------------------------------


# Functions for the Member/User
async def generate_unique_user_id():
    """
    Generates a random 4-digit userId that is not already in use in the database.
    
    :return: int, Unique userId
    """
    while True:
        user_id = random.randint(1001, 9999)  # Generate random 4-digit number
        query = "SELECT userId FROM users WHERE userId = ?"
        variables = (user_id,)
        
        result = await runQuery(query, variables)
        if not result:  # If result is empty, userId is unique
            return user_id


async def addUser(name):
    """
    Inserts a new user with the provided name and unique userId into the users table using runQuery.
    
    :param name: str, Username of the user to be inserted
    """
    user_id = await generate_unique_user_id()
    
    query = "INSERT INTO users (userId, name) VALUES (?, ?)"
    variables = (user_id, name)
    
    try:
        await runQuery(query, variables)
        print(f"Created user with userId '{user_id}' and name '{name}'")
    except Exception as e:
        print(f"Failed to create user: {e}")


async def editUser(user_id, new_name):
    """
    Updates the name of a user with the given user_id.

    :param user_id: int, The ID of the user to be updated.
    :param new_name: str, The new name of the user.
    """
    query = "UPDATE users SET name = ? WHERE userId = ?"
    variables = (new_name, user_id)

    try:
        await runQuery(query, variables)
        print(f"Updated user with ID '{user_id}' - new name: '{new_name}'")
    except Exception as e:
        print(f"Failed to update user: {e}")


#---------------------------------------------------------------------------------------------------------


# Functions for the Books
async def generate_unique_book_id():
    """
    Generates a random 3-digit bookId that is not already in use in the database.
    
    :return: int, Unique bookId
    """
    while True:
        book_id = random.randint(101, 999)  # Generate random 3-digit number
        query = "SELECT bookId FROM books WHERE bookId = ?"
        variables = (book_id,)
        
        result = await runQuery(query, variables)
        if not result:  # If result is empty, bookId is unique
            return book_id


async def addBook(book_name, quantity, number_of_issues):
    """
    Inserts a new book with the provided name, quantity, number of issues, and unique bookId into the books table using runQuery.
    
    :param book_name: str, Name of the book to be inserted
    :param quantity: int, Quantity of the book to be inserted
    :param numberOfIssues: int, Number of issues of the book to be inserted
    """
    book_id = await generate_unique_book_id()
    
    query = "INSERT INTO books (bookId, book_name, quantity, number_of_issues) VALUES (?, ?, ?, ?)"
    variables = (book_id, book_name, quantity, number_of_issues)
    
    try:
        await runQuery(query, variables)
        print(f"Added book '{book_name}' with bookId '{book_id}', quantity '{quantity}', and number of issues '{number_of_issues}'")
    except Exception as e:
        print(f"Failed to add book: {e}")


async def editBook(book_id, new_quantity, new_book_name):
    """
    Updates the quantity and book_name of a book with the given book_id.

    :param book_id: int, The ID of the book to be updated.
    :param new_quantity: int, The new quantity of the book.
    :param new_book_name: str, The new name of the book.
    """
    query = "UPDATE books SET quantity = ?, book_name = ? WHERE bookId = ?"
    variables = (new_quantity, new_book_name, book_id)

    try:
        await runQuery(query, variables)
        print(f"Updated book with ID '{book_id}' - new quantity: {new_quantity}, new book name: {new_book_name}")
    except Exception as e:
        print(f"Failed to update book: {e}")
