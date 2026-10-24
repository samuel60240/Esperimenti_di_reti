
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Il server è pronto a ricevere")
while(1):
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    upperSentence = sentence.upper().encode()
    connectionSocket.send(upperSentence)
    connectionSocket.close()

