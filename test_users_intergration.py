from models.user import UserModel
from test.integration_base_test import integration_base_test

class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')

            self.assertIsNono(UserModel.find_by_username('test'))
            self.assertIsNono(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'))
            self.assertIsNotNono(UserModel.find_by_id(1))