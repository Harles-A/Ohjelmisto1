from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def onko_alkuluku(luku):
    if luku < 2:
        on_alkuluku = False
    else:
        on_alkuluku = True
        for jakaja in range(2, int(math.sqrt(luku)) + 1):
            if luku % jakaja == 0:
                on_alkuluku = False
                break

    vastaus = {
        'Number': luku,
        'isPrime': on_alkuluku
    }

    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
