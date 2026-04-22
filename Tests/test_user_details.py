from encodings import search_function

import pytest
from API_Practice.Utilities.user_utilities import userAPI
from API_Practice.TestData.user_account import UserAccountTestData

class TestUserAccount:
    print("************************Test c@se execution is Started***************************")
    user_api_obj = userAPI()
    user_Test_data = UserAccountTestData.create_user_data
    # print(f"data:{user_Test_data}")
    # for creationdata in user_Test_data:
    #     # user1 =  creationdata["email"]
    #     # passw1 = creationdata["password"]
    # @pytest.mark.user
    # @pytest.mark.parametrize("username, password", [creationdata["email"],creationdata["password"]])
    def test_create_user_account(self):
        resp = self.user_api_obj.create_user_account()
        print(f"resp:{resp.json()}")
        assert resp.status_code == 200, "HTTP request failed"
        assert resp.json()["responseCode"] == 201, "User not created successfully"
    print("************************ test_create_user_account Test c@se execution is completed******************************")

    # @pytest.mark.user
    def test_verify_user_login(self):
        resp = self.user_api_obj.validate_user()
        print(f"response is:{resp.status_code}")
        assert resp.status_code == 200,"user is not validate"
        print("************************ test_verify_user_login Test c@se execution is completed******************************")

    # @pytest.mark.user
    def test_getuser_detail_by_email(self):
        resp = self.user_api_obj.get_user_email_details()
        # print(f"Get response code is :{resp.status_code}")
        print(f"Get response is:{resp.status_code}")
        assert resp.status_code == 200, "user is not validate"
        print("************************ test_getuser_detail_by_email Test c@se execution is completed******************************")
    @pytest.mark.user
    def test_deleteuser_account(self):
        resp = self.user_api_obj.del_user_accounts()
        print(f"Deletes response is:{resp.status_code}")
        assert resp.status_code == 200, "user is not validate"
        print("************************ test_delete user_account Test c@se execution is completed******************************")
