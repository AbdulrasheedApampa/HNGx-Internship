from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = {
    "user_id": {"age": 19, "gender": "male"},
    "bill": {"age":25, "gender":"male"}
    
    }

videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="naame of the video is required", required=True)



class HelloWorld(Resource):
    def get(self, user):
        return users[user]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        video[video_id] = args
        return video[video_id], 201



# class HelloWorld(Resource):
#     def get(self, name, test):
#         return {"name": name, "test": test}

api.add_resource(HelloWorld, "/api/<string:user>")

if __name__ == "__main__":
    app.run(debug=True)
    