def criptografar(chave,mensagem):
	lista = list(mensagem)
	nova_mensagem = ""
	for i in lista:
		# verificar se carac  eh letra
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				caract = (ord(i) - ord('a') + chave) % 26
				nova_mensagem += chr(caract + ord('a'))
			else:
				caract = (ord(i) - ord('A') + chave) % 26
				nova_mensagem += chr(caract + ord('A'))
		else:
			nova_mensagem += i
	return nova_mensagem

def decriptografar(chave, mensagem):
	lista = list(mensagem)
	criptografar = ""
	for i in lista:
                # verificar se carac  eh letra
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				caract = (ord(i) - ord('a') - chave) % 26
				criptografar += chr(caract + ord('a'))
			else:
				caract = (ord(i) - ord('A') - chave) % 26
				criptografar += chr(caract + ord('A'))
		else:
			criptografar += i
	return criptografar

print("mensagem criptografada:",criptografar(3,"casa"))
print("mensagem decriptografada:",decriptografar(3,"fdvd"))
