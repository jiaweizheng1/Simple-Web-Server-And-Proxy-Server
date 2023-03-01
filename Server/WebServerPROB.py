from socket import *

define 

webserverSocket = socket(AF_INET, SOCK_STREAM)
webserverSocket.bind(("", 6789))
webserverSocket.listen(1)

while True:
        print('Ready to serve...')

        connectionSocket, addr = webserverSocket.accept()

        try:
                request = connectionSocket.recv(1048576)

                first_line = request.split(b'\n')[0]
                
                url = first_line.split()[1]

                filename_pos = url.rfind(b'/')

                filename = url[filename_pos + 1:]

                data = []

                data.append(b'HTTP/1.1 200 OK\r\n\r\n')

                with open(filename, "rb") as file:
                        data.append(file.read())

                connectionSocket.sendall(b''.join(data))

                connectionSocket.close()
                
        except:
                connectionSocket.sendall(b'HTTP/1.1 404 Not Found\r\n\r\n')
        
                connectionSocket.close()

webserverSocket.close()