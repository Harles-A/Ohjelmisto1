from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='12345',
        autocommit=True,
        collation='utf8mb4_general_ci'
    )

def fetch_airport_by_icao(code):
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = f"SELECT name, municipality FROM airport WHERE ident='{code}'"
    cursor.execute(sql)
    result_row = cursor.fetchone()
    cursor.close()
    connection.close()
    return result_row

@app.route('/kenttä/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    icao_code = icao_code.upper()

    try:
        result = fetch_airport_by_icao(icao_code)
        response = {
            "ICAO": icao_code,
            "Name": result[0],
            "Municipality": result[1]
        }
    except ValueError as e:
        response = {
            "error": "404 Airport not found"
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
