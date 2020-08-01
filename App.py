from flask import Flask, request, jsonify, Response
import random
from Surprise_me import Surprise

# Creates the flask application object.
app = Flask(__name__)

# creates object of Surprise class
surprise = Surprise()

# GET / api / surprise
@app.route("/api/surprise", methods=['GET'])
def surprise_route():

    # Check if name and birth year are include in the request and save it for further use.
    if 'name' in request.args:
        name = str(request.args['name'])
        # Remove all spaces from the name
        name = name.replace(" ","")
        # Check if name include only letters
        if (any(not str.isalpha(letter) for letter in name)):
            return Response('Please enter a valid name', 400)
    else:
        if 'birth_year' in request.args:
            # If only name is not in the client request
            return Response('Please include name in your request', 400)
        else:
            # If name and birth year are not in the client request 
            return Response('Please include name and birth year in your request', 400)

    if 'birth_year' in request.args:
        birthYear = str(request.args['birth_year'])
        # Check if birth year include only numbers
        if (any(not str.isdigit(num) for num in birthYear)):
            return Response('Please enter a valid birth year', 400)
        # Changing birth year to int for further comparing
        birthYear = int(birthYear)
    else:
        return Response('Please include birth year in your request', 400)

    # Change all the letters in name to lowercase
    name = name.lower()
    firstLetter = name[0]

    # Checking what kind of surprising response is relevant for the given information.
    if firstLetter != 'q':
        
        if birthYear <= 2000:
            # 'chuck-norris-joke' or 'name-sum'
            return random.choice([surprise.getChuckNorris, surprise.getNameSum])(name)
        elif birthYear > 2000 and firstLetter not in ('a','z'):
            # 'kanye-quote' or 'name-sum'
            return random.choice([surprise.getKanyeWest, surprise.getNameSum])(name)
        else:
            # 'name-sum'
            return surprise.getNameSum(name)

    elif birthYear <= 2000:
        # 'chuck-norris-joke' or 'donald-trump-quote'
        return random.choice([surprise.getChuckNorris, surprise.getDonaldTrump])()
    elif birthYear > 2000:
        # 'kanye-quote' or 'donald-trump-quote'
        return random.choice([surprise.getKanyeWest, surprise.getDonaldTrump])()

# # GET / api / stats
@app.route('/api/stats', methods=['GET'])
def stats_route():
    # Sum all values of count from apiCounter array
    apiSum = sum(num['count'] for num in surprise.apiCounter)
    # return empty array if there were no successful requests to the /surprise route
    if(apiSum == 0):
        return jsonify(requests=apiSum, distribution=[])
    # return the number of successful requests for each response
    return jsonify(requests = apiSum, distribution = surprise.apiCounter)

if __name__ == '__main__':
    # A method that runs the application server
    app.run()
