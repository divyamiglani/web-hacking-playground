import sqlite3

# Function to fetch user data from the database
def fetch_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerable SQL query with user-controlled input
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    user_data = cursor.fetchone()
    
    conn.close()
    
    return user_data

# Example usage
username = input("Enter username: ")
user_data = fetch_user_data(username)
print(user_data)
