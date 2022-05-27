from flask_restful import Resource, reqparse
from controller.CrawledDataHandler import CrawledDataHandler

class SearchResult(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('search_input', type=str, help="search_input cannot be converted", required=True, location="form")
            args = parser.parse_args()
            _searchInput = args['search_input']
            return {'search_input': _searchInput}   

        except Exception as e:
            return {'error': str(e)}