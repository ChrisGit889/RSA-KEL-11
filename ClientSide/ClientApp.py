import requests
import json
import time
import random
import sys
from PrimeNumberGeneration import generateLargePrime

sys.setrecursionlimit(10000)
print(chr(27) + "[2J")

def gcd(a,b) -> int:
    if(a < b):
        b , a = a , b
    while(b != 0):
        a , b = b , a%b
    return a

#Extended Euclidean algorithm
#Source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
x , y = 0 , 1
def gcdExtended(a, b):
    global x, y

    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b

    # To store results of recursive call
    gc = gcdExtended(b % a, a)
    x1 = x
    y1 = y

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gc

def modInverse(A, M):

    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")

    else:

        # m is added to handle negative x
        res = (x % M + M) % M
        return res

def get65535LessThanN(n):
    res = "65535"
    while int(res) < n :
        res += "65535"
    return len(res) - 5

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
    p = generateLargePrime(2048)
    q = generateLargePrime(2048)
    bigPrime = p*q
    phi = (p-1)*(q-1)
    print("*****\n*****\nPrimes Generated!\n*****")
    print("*****\nGenerating Keys\n*****")

    #Source https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
    e = 0
    while(True):
        i = random.randrange(2,phi)
        if gcd(i,phi) == 1:
            e = i
            break
    print('Public Key found!\nGenerating Private Key')

    #Inverse of e mod phi
    d= modInverse(e,phi)
    assert (d*e)%phi == 1

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
            results = None
            while(True):
                time.sleep(3)
                print('waiting')
                #TODO: receiving logic
                results = requests.get('http://127.0.0.1:5000/messages/'+email)
                if results.status_code == 202:
                    break

            data = json.loads(results.content)['messages']
            
            partitionLength = len(str(bigPrime))

            print(chr(27) + "[2J")
            print('\nMessages')
            
            for text in data:
                print('message: ')
                splitText = [text[i*partitionLength : i*partitionLength+partitionLength] for i in range(int(len(text)/partitionLength))]
                decrypted = [str(pow(int(num) , d , bigPrime)).rjust(partitionLength , '0') for num in splitText]
                fullMessage = ''.join(decrypted)
                fullMessage = [chr(int(fullMessage[i*5:i*5+5])) for i in range(int(len(fullMessage)/5))]
                while fullMessage[-1] == '\x00' :
                    fullMessage.pop()
                fullMessage = ''.join(fullMessage)
                print(fullMessage)
            input('Press enter to close')

        elif x == 2:
            data = None
            chosen = None
            while(True):
                print(chr(27) + "[2J")
                print('Querying for current users online')
                results = requests.get('http://127.0.0.1:5000/users')
                data =json.loads(results.content)['users']
                for i in range(len(data)):
                    print("["+str(i)+"] "+ data[i]['email'])
                print('[-1] Refresh')
                
                c = int(input('\nInput : '))
                if c <= -1 or c >= len(data):
                    continue
                chosen = data[c]
                break

            directedEmail = chosen['email']
            usingE = chosen['e']
            usingN = chosen['n']

            partitionLength = len(str(usingN))

            message = input('Put in your message:\n')

            listedMessage = ''.join([str(ord(c)).rjust(5,'0') for c in message])

            splitMessage = [listedMessage[i*partitionLength:i*partitionLength+partitionLength] for i in range(int(len(listedMessage) / partitionLength) + 1)]
            splitMessage[-1] = splitMessage[-1].ljust(partitionLength , '0')

            resultsList = [str(pow(int(nums) , usingE , usingN)).rjust(partitionLength, '0') for nums in splitMessage]
            message = ''.join(resultsList)

            requests.post(
                'http://127.0.0.1:5000/send',
                json ={
                    'email' : directedEmail,
                    'message' : message
                }
            )







main()