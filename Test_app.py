import unittest
from App import app

class FlaskTest(unittest.TestCase):
    

    # Check if response is 400 when there is no name and birth year
    def test_response(self):
        response = self.getResponse('/api/surprise')
        status = response.status_code
        self.assertEqual(status, 400)

    # Check if response is 400 when there is no name
    def test_no_name(self):
        response = self.getResponse('/api/surprise?birth_year=2000')
        status = response.status_code
        self.assertEqual(status, 400)

    # Check if response is 400 when there is no birth year
    def test_no_birth_year(self):
        response = self.getResponse('/api/surprise?name=Eyal')
        status = response.status_code
        self.assertEqual(status, 400)

    # Check if response is 400 when there is number in the name
    def test_name(self):
        response = self.getResponse('/api/surprise?name=Eyal2&birth_year=2000')
        status = response.status_code
        self.assertEqual(status, 400)

    # Check if response is 400 when there is special character in the name
    def test_name2(self):
        response = self.getResponse('/api/surprise?name=Eya!l&birth_year=2000')
        status = response.status_code
        self.assertEqual(status, 400)

    # Check if response is 400 when there is letter in the birth year
    def test_birth_year(self):
        response = self.getResponse('/api/surprise?name=Eyal&birth_year=20e00')
        status = response.status_code
        self.assertEqual(status, 400)

    # Check if response is 400 when there is special character in the birth year
    def test_birth_year2(self):
        response = self.getResponse('/api/surprise?name=Eyal&birth_year=20*00')
        status = response.status_code
        self.assertEqual(status, 400)


    # Check if response is 200 when name start with 'E' and birth year <= 2000
    def test1(self):
        response = self.getResponse('/api/surprise?name=Eyal&birth_year=2000')
        self.assertTrue(b'chuck-norris-joke' or b'name-sum' in response.data)

    # Check if response is 200 when name start with 'E' and birth year > 2000
    def test2(self):
        response = self.getResponse('/api/surprise?name=Eyal&birth_year=2001')
        self.assertTrue(b'kanye-quote' or b'name-sum' in response.data)

    # Check if response is 200 when name start with 'A' and birth year > 2000
    def test3(self):
        response = self.getResponse('/api/surprise?name=Amir&birth_year=2001')
        self.assertTrue(b'name-sum' in response.data)

    # Check if response is 200 when name start with 'Q' and birth year <= 2000
    def test4(self):
        response = self.getResponse('/api/surprise?name=Quincy&birth_year=2000')
        self.assertTrue(b'chuck-norris-joke' or b'donald-trump-quote' in response.data)

    # Check if response is 200 when name start with 'Q' and birth year > 2000
    def test5(self):
        response = self.getResponse('/api/surprise?name=Quincy&birth_year=2001')
        self.assertTrue(b'kanye-quote' or b'donald-trump-quote' in response.data)

    # Check if the response of the stats is 200 when route is correct
    def test_stats(self):
        response = self.getResponse('/api/stats')
        status = response.status_code
        self.assertEqual(status, 200)

    # Function that return the response for the given url
    def getResponse(self, url):
        test = app.test_client(self)
        return test.get(url)


if __name__ == '__main__':
    unittest.main()