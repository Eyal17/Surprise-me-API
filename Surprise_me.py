import requests
from flask import jsonify

class Surprise:
    apiCounter = []
    # Constructor
    def __init__(self):
        
        # Array of dictionaries of amount of successful requests for each response.
        self.apiCounter.append({'type': 'chuck-norris-joke','count': 0})
        self.apiCounter.append({'type': 'kanye-quote','count': 0})
        self.apiCounter.append({'type': 'name-sum','count': 0})
        self.apiCounter.append({'type': 'donald-trump-quote','count': 0})

    # *args : allows you to pass a variable number of arguments to a function.     
    # Chuck Norris joke.
    def getChuckNorris(self, *args):
        result = self.getResult('https://api.chucknorris.io/jokes/random')
        # Update the apiCounter in the relevant position
        self.setCounter('chuck-norris-joke')
        return jsonify({'type': 'chuck-norris-joke','result': result.json()['value']})
    
    # Kanye West quote.
    def getKanyeWest(self, *args):
        result = self.getResult('https://api.kanye.rest')
        self.setCounter('kanye-quote')
        return jsonify({'type': 'kanye-quote','result': result.json()['quote']})

    # Calculate the name-sum
    def getNameSum(self, name):
        # Using ord method to convert the letters in the name to numbers and then calculate the sum.
        # The ord function returns an integer representing the Unicode character 
        numbers = sum([ord(letter) - 96 for letter in name])
        self.setCounter('name-sum')
        return jsonify({'type': 'name-sum','count': numbers})

    # Donald Trump quote.
    def getDonaldTrump(self):
        result = self.getResult('https://www.tronalddump.io/random/quote')
        self.setCounter('donald-trump-quote')
        return jsonify({'type': 'donald-trump-quote','result': result.json()['value']})

    # Function that get and return the response from the given url 
    def getResult(self, url):
        return requests.get(url)

    # Update the apiCounter array
    def setCounter(self, strType):
        # enumerate : add counter to an iterable
        index = [i for i, d in enumerate(self.apiCounter) if strType in d.values()][0]
        self.apiCounter[index]['count'] = self.apiCounter[index]['count'] + 1

