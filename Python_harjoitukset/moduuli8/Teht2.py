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

def fetch_airports_by_country(code):
    connection = get_db_connection()
    sql = (f"SELECT type FROM airport WHERE iso_country = '{code}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    return result_row

maakoodi = input("Anna maakoodi: ")

small_airport_count = 0
medium_airport_count = 0
large_airport_count = 0
heliport_count = 0
seaplane_base_count = 0
balloonport_count = 0
closed_count = 0

result = fetch_airports_by_country(maakoodi)

for i in result:
    # This will xtract the first element from the tuple, otherwise it will consider the entire tuple
    # as simply one i and airport counters will all remain as 0.
    airport_type = i[0]
    # Now we can properly go through each tuple element one by one and increase the counters.
    if airport_type == 'small_airport':
        small_airport_count += 1
    elif airport_type == 'medium_airport':
        medium_airport_count += 1
    elif airport_type == 'large_airport':
        large_airport_count += 1
    elif airport_type == 'heliport':
        heliport_count += 1
    elif airport_type == 'seaplane_base':
        seaplane_base_count += 1
    elif airport_type == 'balloonport':
        balloonport_count += 1
    elif airport_type == 'closed':
        closed_count += 1

# Finally we print the results. I have made separate entry for each type of airport depending on if there is only
# 1 of them in the country or more than 1, to make sure grammar stays correct.
# For example 1 small airport vs. 2 small airports.
# I'm sure there are more elegant ways of doing this, but it'll have to do for now.
print(f"In {maakoodi} you can find: ")
if 0 < small_airport_count < 2:
    print(f"{small_airport_count} Small Airport")
elif small_airport_count > 1:
    print(f"{small_airport_count} Small Airports")
if 0 < medium_airport_count < 2:
    print(f"{medium_airport_count} Medium Airport")
elif medium_airport_count > 1:
    print(f"{medium_airport_count} Medium Airports")
if 0 < large_airport_count < 2:
    print(f"{large_airport_count} Large Airport")
elif large_airport_count > 1:
    print(f"{large_airport_count} Large Airports")
if 0 < heliport_count < 2:
    print(f"{heliport_count} Heliport")
elif heliport_count > 1:                     
    print(f"{heliport_count} Heliports")
if 0 < seaplane_base_count < 2:
    print(f"{seaplane_base_count} Seaplane Base")
elif seaplane_base_count > 1:
    print(f"{seaplane_base_count} Seaplane Bases")
if 0 < balloonport_count < 2:
    print(f"{balloonport_count} Balloonport")
elif balloonport_count > 1:
    print(f"{balloonport_count} Balloonports")
if 0 < closed_count < 2:
    print(f"{closed_count} Closed Airport")
elif closed_count > 1:
    print(f"{closed_count} Closed Airports")
