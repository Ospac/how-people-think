from flask import Flask
from flask_restful import Api
from routes.Index import Index
from api.SearchResult import SearchResult

app = Flask(__name__)
api = Api(app)

#routes
api.add_resource(Index, '/')
api.add_resource(SearchResult, '/api/search')

#API Server
if __name__ == '__main__':
    app.run(debug=True)
