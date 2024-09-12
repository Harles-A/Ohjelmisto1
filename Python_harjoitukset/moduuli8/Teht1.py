import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
         host='127.0.0.1', # localhost
         port=3306,
         database='flight_game',
         user='root',
         password='12345',
         autocommit=True,
        # tarvitaan uudelle 9.0 versiolle ajurista:
         collation='utf8mb4_general_ci'
         )


def fetch_airport_by_icao(code):
    connection = get_db_connection()
    sql = (f"select name, municipality from airport where ident='{code}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    print(result_row)
    return result_row

user_input = input("Anna ICAO koodi: ")
user_input = user_input.upper()
result = fetch_airport_by_icao(user_input)
if result: # Sama kuin vertailu: result != None
    print(f"Haettu kenttä: {result[0]}, {result[1]}")
else:
    print("Eipä löydy.")

