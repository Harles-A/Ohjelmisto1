import json

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def print_joku_juttu():
    return 'Siinä sulla joku uusi juttu'

@app.route('/sum')
def calculate_sum():
    #print(request.args.get('num2'))
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except ValueError:
        return 'Ooopsies!'
    except TypeError:
        'uh-oh!'
    return {
        'function': "calculate sum of two values",
        'result': num1 + num2
    }


names = ['Aku', 'Maku', 'Paku', 'Vaku']

@app.route('/names')
def get_names():
    return {'names':names}
@app.route('/names/<id>')
def get_name(id):
    try:
        result = {'id':id, 'name':names[int(id)]}
    except IndexError:
        res_body = {'error': 'not found'}
        res_body=json.dumps(res_body)
        error_response = Response(status=404, response=res_body, content_type='application/json')
        return error_response
    return result

@app.errorhandler(404)
def not_found(error):
    #print(error)
    #print(request.path)
    res_body = {'requested route': request.path, 'error': 'not found'}
    res_body = json.dumps(res_body)
    error_response = Response(status=404, response=res_body, content_type='application/json')
    return error_response

if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)
