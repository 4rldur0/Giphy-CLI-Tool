from data import Data
import unittest

class DataTest(unittest.TestCase):
    def test_url(self):
        api_key = "oZhufry2NyjOWfmCItORiADf8lPGTN2j"
        params = {
            "api_key": api_key,
            "limit": 25,
            "offset": 0,
            "rating": "g",
            "bundle": "messaging_non_clips"
        }
        d = Data("trending", api_key, params)
        self.assertTrue(d.get_data() != None, "Data is not invoked")

if __name__ == "__main__":
    unittest.main()
