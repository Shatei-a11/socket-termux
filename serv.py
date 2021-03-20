import socket

so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


so.bind(('127.8.0.01', 7010))


while True:
	print("\nESPERANDO MENSAGEM")
	nome, endereco = so.recvfrom(1048)
	
	memsagem, endereco_ip = so.recvfrom(1048)
	
	res = nome.decode().upper()
	so.sendto(res.encode(), endereco)
	
	resposta = memsagem.decode().upper()
	so.sendto(resposta.encode(), endereco)
	
	print(f"Nome: {res}")
	print(f"Mensagen enviada: {resposta}")
