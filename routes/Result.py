from flask import make_response, render_template
from flask_restful import Resource, reqparse
from controller.CrawledDataHandler import CrawledDataHandler
from controller.InitThreading import trendinglist
class Result(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('search_input', type=str, help="search_input cannot be converted", required=True, location="args")
            args = parser.parse_args()
            _searchInput = args['search_input']
            data = CrawledDataHandler(_searchInput)
            
            return make_response(render_template(
                'result.html', 
                sentimentData   = data["sentiment"][0],
                searchInput     = data["searchInput"],
                imgPath         = data["imgPath"],
                keywordHistory  = data["keywordHistory"],
                trendingData    = trendinglist
            ))
        except Exception as e:
            return {'error': str(e)}
