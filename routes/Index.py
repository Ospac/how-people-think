from flask import make_response, render_template
from flask_restful import Resource
from db import DB
db=DB()
getwords = db.get_words()
tranwords = []
for i in range(len(getwords)):
    tranwords.extend(getwords[i])
    tranwords[i].split("(',)")
class Index(Resource):
    def get(self):
        return make_response(render_template('index.html', words = tranwords)) # words for recently searched words
        
