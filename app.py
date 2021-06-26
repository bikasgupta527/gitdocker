from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
value = {}
api = Api(app)
parser = reqparse.RequestParser()

class FlaskAppTest(Resource):
  def get(self):
    return "This response is coming from get"

  def post(self):
    parser.add_argument("text")
    args = parser.parse_args()
    val = args["text"]
    value = "Hello your text was "+str(val) 
    return value,201

api.add_resource(FlaskAppTest, '/')
