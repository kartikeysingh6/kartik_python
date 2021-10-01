import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input(str("Enter host address ::\t"))
port = 8080

s.connect((host,port))
print("Connected to...")

f = open(input(str("Enter name for incoming file ::\t")), 'wb')

while True:
    fData = s.recv(1024)
    while fData:
        f.write(fData)
        fData = s.recv(1024)
    f.close()
    break

print("Recieved !")