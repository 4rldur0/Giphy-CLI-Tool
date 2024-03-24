import os

from data import Data


class GiphyAPI:
    def __init__(self):
        self.params = {
            "api_key": os.environ["GIPHY_API_KEY"],
            "limit": 25,
            "offset": 0,
            "rating": "g",
            "bundle": "messaging_non_clips",
        }

    def trending(self):
        print("trending subcommand called!")
        d = Data("trending", self.params)
        return d.get_data()

    def search(self, q):
        print("search subcommand called!")
        self.params["q"] = q
        d = Data("search", self.params)
        return d.get_data()
