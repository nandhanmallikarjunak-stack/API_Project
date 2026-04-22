

import requests
from API_Practice.Helpers.api_helpers import APIhelpers
from API_Practice.APIObjects.user_api_objects import userAPIObjects
from API_Practice.TestData.user_account import UserAccountTestData

class userAPI:

    url= "https://automationexercise.com/api"
    api_helper = APIhelpers()
    api_users = userAPIObjects()
    api_Testdata = UserAccountTestData()
    # url = UserAccountTestData.application_URL

    def create_user_account(self):
        #URL
        #end point along  with path parameters
        #payload
        # Post method
        print("********************** Create user account is started *******************************")
        data = self.api_helper.post_api(url=self.url,endpoint =self.api_users.create_user,
                                        payload=self.api_Testdata.create_user_data)
        # print("Create account response is :",data.text)
        print("********************** Create user account is ended *******************************")
        return data

    def validate_user(self):
        print("********************** verify user test case is started *******************************")
        data = self.api_helper.post_api(url=self.url, endpoint = self.api_users.verify_login,
                                 payload =  self.api_Testdata.Verify_login_data)
        # print("Create account response is :",data.text)
        print("********************** verify user test case is ended *******************************")
        return data
    def get_user_email_details(self):
        print("********************** Get Email Details test case is started *******************************")
        data = self.api_helper.get_api(url = self.url,endpoint = self.api_users.user_email_id,
                                payload = self.api_Testdata.Verify_email_data)
        print("********************** Get Email Details test case is Ended *******************************")
        return data
    def del_user_accounts(self):
        print("********************** Delete user account test case is started *******************************")
        data = self.api_helper.delete_api(self.url,self.api_users.delete_account,
                                   self.api_Testdata.delete_user_acc)
        print("********************** Delete user account test case is Ended *******************************")
        return data