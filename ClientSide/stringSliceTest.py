message = "Hellofofof"

message = [message[i*3:i*3+3].ljust(3,' ') for i in range(int(len(message)/3+1))]

x = []
for i in message:
    temp = ''.join([str(ord(character)).rjust(5,'0') for character in i])
    x.append(temp)

# message = [ord(s) for s in message]

print(x)