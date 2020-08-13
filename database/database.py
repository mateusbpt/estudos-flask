from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_db(app):
    app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/estudos-flask'

    db.init_app(app)
