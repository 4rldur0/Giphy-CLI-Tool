from data import Data
from api import GiphyAPI
import unittest

class Test(unittest.TestCase):
    # small tests
    def test_url(self):
        api_key = "oZhufry2NyjOWfmCItORiADf8lPGTN2j"
        params = {
            "api_key": api_key,
            "limit": 25,
            "offset": 0,
            "rating": "g",
            "bundle": "messaging_non_clips"
        }
        d = Data("trending", self.params)
        self.assertTrue(d.get_data()['meta']['msg'] == 'OK', "responded message should be 'OK'")

    # medium tests
    def test_trending_api(self):
        ga = GiphyAPI()
        self.assertTrue(ga.trending()['meta']['msg'] == 'OK', "responded message should be 'OK'")

    def test_search_api(self):
        ga = GiphyAPI()
        q = "hi"
        self.assertTrue(ga.search(q)['meta']['msg'] == 'OK', "responded message should be 'OK'")
        
if __name__ == "__main__":
    unittest.main()
