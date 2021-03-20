import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.bind(('127.3.0.02', 7011))
nome = input("Digite seu nome: ")
while True:
        mensagem_enviar = input("Digite uma mensagem: ")
        socket.sendto(nome.encode(), ("127.8.0.01",7010))

        socket.sendto(mensagem_enviar.encode(), ("127.8.0.01", 7010))
        mensagem_bytes, endereco_ip = socket.recvfrom(1048)
        mensagem_by, endereco = socket.recvfrom(1048)

        print(mensagem_bytes.decode())
        print("Mensagem enviada")
