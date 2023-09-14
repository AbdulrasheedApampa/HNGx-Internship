from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Uncomment the following line to initialize the database
db.create_all()  # Create the database tables

# Define the UserModel representing a user in the database
class UserModel(db.Model):
    id = db.Column(db.String, primary_key=True)  # Changed to db.String for id
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"

# Define request parsers for input validation
user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type=str, help="Name of the user is required", required=True)
user_put_args.add_argument("age", type=int, help="Age of the user is required", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("name", type=str, help="Name of the user")
user_update_args.add_argument("age", type=int, help="Age of the user")

# Define resource fields for response formatting
resource_fields = {
    'id': fields.String,  # Changed to fields.String for id
    'name': fields.String,
    'age': fields.Integer
}

# Define the User resource
class User(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        # Retrieve a user by ID or return a 404 error if not found
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, user_id):
        args = user_put_args.parse_args()
        # Check if the user ID already exists and return a 409 conflict error if it does
        if UserModel.query.filter_by(id=user_id).first():
            abort(409, message="User id taken...")

        # Create a new user and add it to the database
        user = UserModel(id=user_id, name=args['name'], age=args['age'])
        db.session.add(user)
        db.session.commit()
        return user, 201

    @marshal_with(resource_fields)
    def patch(self, user_id):
        args = user_update_args.parse_args()
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User doesn't exist, cannot update")

        # Update user attributes if provided in the request
        if args['name']:
            result.name = args['name']
        if args['age']:
            result.age = args['age']

        db.session.commit()
        return result

    def delete(self, user_id):
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User doesn't exist, cannot delete")

        # Delete the user from the database
        db.session.delete(result)
        db.session.commit()
        return {'message': 'User deleted'}, 204

# Add the User resource with a route that includes the user_id parameter
api.add_resource(User, "/api/<string:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
