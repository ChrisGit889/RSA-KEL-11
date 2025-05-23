import random
import sys
import time

#Source: https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/
#Other Source: https://youtu.be/tBzaMfV94uA?si=x5bLtPcC2Nl_2mg8
def generateLargePrime(n : int) -> int:
    lowerLimit = 2**(n-1)+1
    upperLimit = 2**n-1
    random.seed(time.time())

    lowerPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

    while(True):
        number = random.randrange(lowerLimit,upperLimit)
        # print(number)
        sieved = False
        
        #Sieve of Arithosteles
        for sieve in lowerPrimes:
            if number % sieve == 0 and sieve**2 <= number: 
                sieved = True
                break
        
        #if prime was sieved by lower primes, continue and generate a new candidate
        if sieved : continue

        evenComponent = number-1
        cantGetLower = evenComponent

        powersShouldBeTested = []

        while(cantGetLower % 2 == 0):
            powersShouldBeTested.append(cantGetLower)
            cantGetLower >>= 1  #Divide prime by two
        powersShouldBeTested.append(cantGetLower)

        testCount = 20
        isPrime = True
        for i in range(testCount):
            #Take the even component

            #Get a random number as witness
            witness = random.randrange(2,number)

            #Fermat's Little Theorem Test
            if(pow(witness,evenComponent,number) != 1) :
                isPrime = False
                break

            for i in range(len(powersShouldBeTested)):
                if pow(witness,powersShouldBeTested[i],number) == 1:
                    if i+1 < len(powersShouldBeTested):
                        if pow(witness,powersShouldBeTested[i+1],number) not in [evenComponent,1]:
                            isPrime = False
                            print(i)
                            break
        
        if not isPrime:
            continue
        else:
            return number

if __name__ == '__main__':
    x = generateLargePrime(4056)
    print(sys.getsizeof(x))