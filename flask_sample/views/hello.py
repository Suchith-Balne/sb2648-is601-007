import os

from flask import Blueprint, Flask, request

app = Flask(__name__)
#sample = Blueprint('hello', __name__, url_prefix='/')


@app.route('/')
def hello_world():
    name = request.args.get('name', 'World')
    return f'Hello {name}!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))