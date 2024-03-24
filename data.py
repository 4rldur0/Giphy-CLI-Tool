import requests

class Data:
    def __init__(self, endpoint, params):
        url = "https://api.giphy.com/v1/gifs"
        self.url = "/".join([url, endpoint])
        self.params = params
        self.data = None

    def get_data(self):
        data_json = requests.get(self.url, params=self.params)
        self.data = data_json.json()
        return self.data
