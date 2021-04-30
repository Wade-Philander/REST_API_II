from flask_restful import from Resource,reqparse
from user import UserModel

class UserRegister(Resource):
    """
    This resourse allows users to register by sending a POST
    request with their username and password
    """
    parser = reqparse.RestParser()
    parser.add_argument('username',type=str, request=True, help="This field connot be blank.")
    parser.add_argument('password',type=str, request=True, help="This field connot be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username'])
        return {'message': 'usernamen alreaduy exist'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return{'message': 'A user was created successfully'},201