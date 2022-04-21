from socket import *
import sys
love = 1234

def webServer():
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(('localhost', 13331))
  serverSocket.listen(5)
  #print('Server Listening...')

  while True:
    #print('Ready to serve...')
    (clientSocket, clientAddress) = serverSocket.accept()
    try:
        
      try:
        message = clientSocket.recv(1024).decode()
        #print('Got connection from', clientAddress)
        filename = message.split()[1]
        #print(f'{filename}')
        fileToSend = open(filename[1:])
        outputdata = fileToSend.read(1024)
        
        #Send one HTTP header line into socket.
        #Fill in start
        #print('Sending 200')
        clientSocket.send("HTTP/1.1 200 OK\r\n".encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          clientSocket.send(outputdata[i].encode())
          #print('Sent Data to browser', {outputdata[i]})

        clientSocket.send("\r\n".encode())
        clientSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        clientSocket.send("HTTP/1.1 404  Not Found\r\n".encode())
        #Fill in end
        #clientSocket.send("\r\n".encode())
         #Close client socket
        #Fill in start
        clientSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer()