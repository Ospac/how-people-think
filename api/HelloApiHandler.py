from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

class HelloApiHandler(Resource):
    def get(self):
        return {"hello": "world!"}