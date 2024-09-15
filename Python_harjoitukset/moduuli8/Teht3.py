from geopy import distance
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1', # localhost
        port=3306,
        database='flight_game',
        user='root',
        password='12345',
        autocommit=True,
        collation='utf8mb4_general_ci'
    )

def fetch_airport_coords(code):
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{code}'")
    cursor.execute(sql)
    result_row = cursor.fetchone()
    return result_row


efhk_input = input("Anna ensimmäisen lentoaseman ICAO-koodi: ")
efvu_input = input("Anna toisen lentoaseman ICAO-koodi: ")
efhk_coords = fetch_airport_coords(efhk_input)
efvu_coords = fetch_airport_coords(efvu_input)
distance_result = distance.distance((efhk_coords), (efvu_coords))
# I tried to round up the final answer, but it is giving me error:
# unsupported format string passed to geodesic.__format__
# I couldn't figure out how to get it to work so now it gives ugly long answers.
print(f"Lentoaseman {efhk_input} ja {efvu_input} etäisyys on {distance_result}")