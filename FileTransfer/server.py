import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.247.135'
# print(host)
port = 8080

s.bind((host,port))
s.listen(1)

print("Server up and running at", host, "\nPlease Connect...")

conn, addr = s.accept()
print("Connected to ", addr)

# f = input(str("Enter file path ::\t"))
f = open(input(str("Enter file path ::\t")), 'rb')
fData = f.read(1024)

while fData:
    conn.send(fData)
    fData = f.read(1024)
# conn.send(fData)
f.close()
print("Sent !!")