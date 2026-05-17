from http.client import responses

import requests
from APIObjects.user_api_objects import userAPIObjects

class APIhelpers:
    user_api = userAPIObjects()

    def post_api(self,url,endpoint,payload) -> responses:
        """

        :param url:
        :param endpoint:
        :param payload:
        :return:
        """
        api_url = url+endpoint
        print("Post API URL:", api_url)
        print("************************Post API will Start*************************")
        api_response =  requests.post(api_url,payload)
        return api_response

    def get_api(self, url,endpoint,payload):
        api_geturl = url+endpoint
        print(f"Get API URL is {api_geturl}")
        print("************************Get API will Start*************************")
        getapi_response = requests.get(api_geturl,payload)
        print(f"Get api response is :{getapi_response}")
        return getapi_response

    def delete_api(self,url,endpoint,payload):
        api_del_url = url+endpoint
        print(f"Del API URL is {api_del_url}")
        print("************************Deleted API will Start*************************")
        delapi_response = requests.get(api_del_url,payload)
        print(f"Get api response is :{delapi_response}")
        return delapi_response

    def pacth_api(self):
        pass