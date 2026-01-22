# docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=mypassword -e MYSQL_DATABASE=weapons -p 3306:3306 -d mysql:latest


import mysql.connector
from mysql.connector import Error

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'mypassword'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS weapons")
    conn.commit()
    print("Database 'weapons' created")
    
    cursor.execute("USE weapons")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weapons (
            id INT AUTO_INCREMENT PRIMARY KEY,
            weapon_id VARCHAR(100)
            weapon_name VARCHAR(100)
            weapon_type VARCHAR(100)
            range_km INT
            weight_kg FLOAT
            manufacturer VARCHAR(100)
            origin_country VARCHAR(100)
            storage_location VARCHAR(100)
            year_estimated INT
            risk_level VARCHAR(100)
        )
    """)
    conn.commit()
    print("Table created.")
    
except Error as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
