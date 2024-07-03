import sqlite3
from concurrent.futures import ThreadPoolExecutor
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
    

async def addUser(name):
    """
    Inserts a new user with the provided name into the users table using runQuery.
    
    :param name: str, Username of the user to be inserted
    """
    query = "INSERT INTO users (name) VALUES (?)"
    variables = (name,)
    
    try:
        await runQuery(query, variables)
        print(f"Created user with name '{name}'")
    except Exception as e:
        print(f"Failed to create user: {e}")