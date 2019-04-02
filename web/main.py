from bottle import route, response
from bottle import run

@route('/')
def home():
    response.headers['Access-Control-Allow-Origin'] = '*'
    return "Hello world!"

run(host='localhost', port=9999)