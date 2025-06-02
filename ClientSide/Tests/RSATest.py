import random

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
    

# def get65535LessThanN(n):
#     res = '65535'
#     p = res
#     while int(p) <= n :
#         p += res
#     return len(p)-len(res)

p = 1024383257
q = 53137619
bigPrime = p*q
phi = (p-1)*(q-1)
# numCount = get65535LessThanN(bigPrime)
numCount = len(str(bigPrime))
print(numCount)

e = 0
while(True):
    i = random.randrange(2,phi)
    if gcd(i,phi) == 1:
        e = i
        break

#Inverse of e mod phi
d= modInverse(e,phi)
assert (d*e)%phi == 1

message = "hahah h "

# message = message.replace(' ','pp')
print(message)
utf16_message = [str(ord(i)).rjust(5,'0') for i in message]
utf16_message = ''.join(utf16_message)

toEncrypt = [utf16_message[i*numCount:i*numCount+numCount] for i in range(int(len(utf16_message)/numCount+1))]
toEncrypt[-1] = toEncrypt[-1].ljust(numCount , '0')
print(toEncrypt)

encyrpted = [str(pow(int(nums) , e , bigPrime)).rjust(numCount , '0') for nums in toEncrypt]
print(encyrpted)
encyrpted = ''.join(encyrpted)

toDecrypt = [encyrpted[i*numCount:i*numCount+numCount] for i in range(int(len(encyrpted)/numCount))]
print(toDecrypt)
decrypted = [ str(pow(int(num) , d , bigPrime)).rjust(numCount,'0') for num in toDecrypt]
print(decrypted)
decrypted = ''.join(decrypted)

finall = [chr(int(decrypted[i*5:i*5+5])) for i in range(int(len(decrypted)/5))]

while(finall[-1] == '\x00'):
    finall.pop() 
print(finall)