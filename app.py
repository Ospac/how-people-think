from flask import Flask
from flask_restful import Api
from routes.Index import Index
from routes.Result import Result
#from controller.ThreadingStart import InitThreading

app = Flask(__name__)
api = Api(app)

#routes
api.add_resource(Index, '/')
api.add_resource(Result, '/result')

#automatic crawling with interval
index = 0
trendinglist = []
#InitThreading()

#API Server
if __name__ == '__main__':
    app.run(debug=True)
