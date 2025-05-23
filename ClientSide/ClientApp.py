import requests
import json
from PrimeNumberGeneration import generateLargePrime

print(chr(27) + "[2J")

while(True):
    email = input("Input your email: ")

    #Email validation
    if(email.count('@') != 1):
        print('Email is invalid. Please input a valid email')
    else:
        break

bigPrime1 = generateLargePrime(2048)
bigPrime2 = generateLargePrime(2048)

results = requests.post(
    'http://127.0.0.1:5000/login',
    json={'email': 'aaah@hhhd.com','pubKey':117117}
)

results = requests.get('http://127.0.0.1:5000/users/')

print(json.loads(results.content))