import unittest

from api import GiphyAPI

gAPI = GiphyAPI()

class Test(unittest.TestCase):
    # small tests
    def test_url(self):
        self.assertTrue(
            gAPI.get_data("trending")["meta"]["msg"] == "OK", "Responded message should be 'OK'"
        )

    # medium tests
    def test_trending_api(self):
        gAPI.trending()
        self.assertTrue(
            gAPI.data["meta"]["msg"]  == "OK", "Responded message should be 'OK'"
        )
        gAPI.trending(1)
        self.assertTrue(
            gAPI.data["meta"]["msg"]  == "OK", "Responded message should be 'OK'"
        )
        self.assertTrue(
            gAPI.data['pagination']['count']  == 1, "There should be 1 item"
        )
        
    def test_search_api(self):
        q = "hi"
        gAPI.search(q)
        self.assertTrue(
            gAPI.data["meta"]["msg"]  == "OK", "Responded message should be 'OK'"
        )
        gAPI.search(q, 1)
        self.assertTrue(
            gAPI.data["meta"]["msg"]  == "OK", "Responded message should be 'OK'"
        )
        self.assertTrue(
            gAPI.data['pagination']['count']  == 1, "There should be 1 item"
        )
        
if __name__ == "__main__":
    unittest.main()
