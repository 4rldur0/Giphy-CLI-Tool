import os

import requests


class GiphyAPI:
    def __init__(self):
        self.__params = {
            "api_key": os.environ["GIPHY_API_KEY"],
            "limit": 25,
            "offset": 0,
            "rating": "g",
            "bundle": "messaging_non_clips",
        }
        self.url = ""
        self.data = {}
        self.status = None

    def get_data(self, endpoint):
        url = "https://api.giphy.com/v1/gifs"
        self.url = "/".join([url, endpoint])
        data_json = requests.get(self.url, params=self.__params)
        return data_json.json()

    # Extract titles, urls, status from the data
    def extract_data(self):
        self.titles = []
        self.urls = []
        self.status = self.data["meta"]["msg"]
        if self.status == "OK":
            for i in range(len(self.data["data"])):
                self.titles.append(self.data["data"][i]["title"])
                self.urls.append(self.data["data"][i]["url"])

    def trending(self, limit=25):
        if limit <= 0:
            return
        print("trending subcommand called!")
        self.__params["limit"] = limit
        self.data = self.get_data("trending")
        self.extract_data()

    def search(self, q, limit=25):
        if limit <= 0:
            return
        print("search subcommand called!")
        self.__params["q"] = q
        self.__params["limit"] = limit
        self.data = self.get_data("search")
        self.extract_data()
