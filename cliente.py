import socket

udp = "127.0.0.1" # ip local
porta = 1337 # porta
mensagem = b"Olá mundo"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
