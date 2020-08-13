from flask import Flask, request

from database.database import init_db
from database.models import *

app = Flask(__name__)

init_db(app)


@app.route('/users/all', methods=['GET'])
def find_all_users():
    return app.response_class(response=User.objects().to_json(),
                              status=200,
                              mimetype='application/json')


@app.route('/users/<string:id>', methods=['GET'])
def find_one_user(id):
    data = User.objects(id=id)

    if not data:
        return app.response_class(status=404,
                                  mimetype='application/json')

    return app.response_class(response=data.to_json(),
                              status=200,
                              mimetype='application/json')


@app.route('/users', methods=['POST'])
def add_user():
    body = request.get_json()
    new_user = {
        'name': body['name']
    }
    return app.response_class(response=User(**new_user).save().to_json(),
                              status=201,
                              mimetype='application/json')


if __name__ == '__main__':
    app.run()
