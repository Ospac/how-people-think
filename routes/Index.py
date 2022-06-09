from flask import make_response, render_template
from flask_restful import Resource
from db import DB
class Index(Resource):
    def get(self):
        db=DB()
        getwords = db.get_words()
        tranwords = []
        for i in range(len(getwords)):
            tranwords.extend(getwords[i])
            tranwords[i].split("(',)")
        return make_response(render_template('index.html', words = tranwords))
