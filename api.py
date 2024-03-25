import os
import requests


class GiphyAPI:
    def __init__(self):
        self.params = {
            "api_key": os.environ["GIPHY_API_KEY"],
            "limit": 25,
            "offset": 0,
            "rating": "g",
            "bundle": "messaging_non_clips",
        }
        self.url = None
        self.data = None
        
    def get_data(self, endpoint):
        url = "https://api.giphy.com/v1/gifs"
        self.url = "/".join([url, endpoint])
        data_json = requests.get(self.url, params=self.params)
        self.data = data_json.json()
        return self.data

    def trending(self):
        print("trending subcommand called!")
        return self.get_data("trending")

    def search(self, q):
        print("search subcommand called!")
        self.params["q"] = q
        return self.get_data("search")
