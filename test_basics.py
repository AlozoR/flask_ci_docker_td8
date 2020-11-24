import unittest

from flaskapp
from redis import Redis

class CounterTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    # actual tests
    def test_welcome_page(self):
        """ test that assesses my index '/' route works"""
        response = self.app.get('/')
        # HTTP status code == 200
        self.assertEqual(response.status_code, 200)

    # another test
    def test_redis_connection(self):
        redis = Redis(host="redis-server", db=0)
        self.app.get('/visit')
        self.assertEqual(int(redis.get("counter")), 1)

if __name__ == "__main__":
    unittest.main()
