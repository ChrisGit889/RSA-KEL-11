import requests
import json
import time
from PrimeNumberGeneration import generateLargePrime

print(chr(27) + "[2J")

def gcd(a,b) -> int:
    if(a < b):
        b , a = a , b
    while(b != 0):
        a , b = b , a%b
    return a

def get25LessThanN(n):
    res = "25"
    while int(res) < n :
        res += "25"
    return len(res) - 2

def main():
    email = ''

    while(True):
        email = input("Input your email: ")

        #Email validation
        if(email.count('@') != 1):
            print('Email is invalid. Please input a valid email')
        else:
            break

    print("*****\nGenerating two new primes for you . . .")
    p = generateLargePrime(4056)
    q = generateLargePrime(4056)
    bigPrime = p*q
    phi = (p-1)*(q-1)
    print("*****\n*****\nPrimes Generated!\n*****")
    print("*****\nGenerating Keys\n*****")

    #Source https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
    e = 0
    for i in range(2,phi):
        if gcd(i,phi) == 1:
            e = i
            break


    #Inverse of e mod phi
    d=0
    for i in range(2,phi):
        if (i*e)%phi == 1:
            d = i
            break

    print("*****\n\nKeys successfully Created\n\n*****")
    results = requests.post(
        'http://127.0.0.1:5000/login',
        json={
            'email': email,
            'e': e,
            'n': bigPrime
        }
    )
    if results.status_code != 202: raise ValueError('An Internal server error as occured')

    while(True):
        print(chr(27) + "[2J")
        print('What would you like to do?')
        print('1. Recieve a message')
        print('2. Send a message')
        x = int(input('Input: '))
        
        print(chr(27) + "[2J")

        if x == 1:
            print(chr(27) + "[2J")
            print('Calling to the server for recieved messages. . .')
            while(True):
                time.sleep(3)

                #TODO: receiving logic
                results = requests.get()
        elif x == 2:
            print('Querying for current users online')
            data = None
            chosen = None
            while(True):
                results = requests.get('http://127.0.0.1:5000/users')
                data =json.loads(results.content)['users']
                for i in len(data):
                    print("["+str(i)+"] "+ data[i]['email'])
                print('[-1] Refresh')

                if int(input('\nInput : ')) == -1:
                    continue
                chosen = data[i]
                break

            directedEmail = chosen['email']
            usingE = chosen['e']
            usingN = chosen['n']

            partitionLength = get25LessThanN(usingN)

            message = input('Put in your message:\n')





# main()