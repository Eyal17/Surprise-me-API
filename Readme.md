# Installation

The 'Surprise me!' API requires the following modules: 

   
    $ pip install flask requests


Or you can just install the requirements txt with all the relevant modules inside:

    $ pip install -r req.txt

---

In order to use the application, you need to run in the command line the following command:
    
    python App.py


In order to use the tests, you need to run in the command line the following command:

    python Test_app.py

---


# Surprise me! API
The purpose of the API is to return a surprising response, according to the parameters passed by the client.
The surprising response will be chosen from a list of surprising response types, each type has its own internal logic and conditions.

We have 4  different types of surprising responses:

## 1. Chuck Norris Joke (chuck-norris-joke)
    Return a random Chuck Norris joke.
    This type is chosen when the user’s birth year is 2000 or before.
    Possible route: 
    http://localhost:3000/api/surprise?name=Eyal&birth_year=1994
## 2. Kanye West Quote (kanye-quote)
    Return a random Kanye West quote.
    This type is chosen when the user’s birth year is after 2000 and the user’s first name doesn’t start with ‘A’ or ‘Z’.
    Possible route: 
    http://localhost:3000/api/surprise?name=Eyal&birth_year=2001
## 3. User Name’s Sum (name-sum)
    Convert the user’s name to numbers and return the sum.
    This type is chosen when the user’s first name doesn’t start with ‘Q’.
    Possible route: 
    http://localhost:3000/api/surprise?name=Eyal&birth_year=1994
## 4. Donald Trump Quote ('donald-trump-quote')
    Return a random Donald Trump quote.
    This type is chosen when the user’s first name start with ‘Q’.
    Possible route: 
    http://localhost:3000/api/surprise?name=Quincy&birth_year=1994


In case there are more than one option to choose, the response will be random, between all of the relevant options.

---
Another possible route is the /stats route.

Its show the number of successful requests to the /surprise route.

    http://localhost:3000/api/stats

