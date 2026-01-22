# docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=mypassword -e MYSQL_DATABASE=weapons -p 3306:3306 -d mysql:latest


import mysql.connector
from mysql.connector import Error

config = {
        'host': '127.0.0.0',
        'port': 3306,
        'user': 'root',
        'password': 'mypassword'}

def create_SQL():

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
                weapon_id VARCHAR(100),
                weapon_name VARCHAR(100),
                weapon_type VARCHAR(100),
                range_km INT,
                weight_kg FLOAT,
                manufacturer VARCHAR(100),
                origin_country VARCHAR(100),
                storage_location VARCHAR(100),
                year_estimated INT,
                risk_level VARCHAR(100)
            )
        """)
        conn.commit()
        print("Table created.")

    except Error as e:
        print(f"mission failed successfully: {e}")
    


def insert_to_SQL(df):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = """
            INSERT INTO weapons 
            (weapon_id, weapon_name, weapon_type, range_km, weight_kg, manufacturer, origin_country, storage_location, year_estimated, risk_level)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        params = []
        added = 0
        for weapon in df.iterrows():
            weapon = weapon[1] # since its a tuple: (id, actual_object) im accessing the actual object
            params.append(
                (
                    weapon['weapon_id'],
                    weapon['weapon_name'],
                    weapon['weapon_type'],
                    weapon['range_km'],
                    weapon['weight_kg'],
                    weapon['manufacturer'],
                    weapon['origin_country'],
                    weapon['storage_location'],
                    weapon['year_estimated'],
                    weapon['risk_level']
                )
            )
            
            added += 1
            cursor.execute("USE weapons")
            cursor.executemany(query, params)
        cursor.close()
        return added
    
    except Error as e:
        print(f"mission failed successfully: {e}")