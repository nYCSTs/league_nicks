import requests

def verificar (file):
	with open(file + '.txt', mode = 'r') as f:
	    nicks = f.readlines()
	nicks = [x.strip() for x in nicks if len(x) <= 16] 

	for nick in nicks:
	    r = requests.get('https://lolnames.gg/en/br/' + nick)
	    if 'Cleanup date (if inactive)' not in r.text:
	        print(nick + ' - DISPONIVEL')
	    else: 
	    	index = r.text.find('(if inactive)')
    		print(nick + ' - ' + r.text[index + 15:index + 26])


print('\t1) Adicionar um novo nick\n\t2) Verificar por todos os nicks\n\t3) Verificar por um nick\n\t4) EXTRA')
opc = int(input('>>> '))

#ADICIONAR NICK
if (opc == 1):
	novo_nick = input('Insira um nick a ser adicionado a lista: ')
	#CHECAR POR NICK IGUAL
	with open('nicks.txt', mode = 'r') as f:
	    nicks = f.readlines()
	nicks = [x.strip() for x in nicks if len(x) <= 16] 
	#CASO COM NICK PRESENTE
	if novo_nick in nicks:
		print('Nick ja presente no .txt')
	#ADICIONAR NO .TXT
	else:
		f = open('nicks.txt', mode = 'a')
		f.write('\n' + novo_nick)
		f.close()

elif (opc == 2):
	with open('nicks.txt', mode = 'r') as f:
	    nicks = f.readlines()
	nicks = [x.strip() for x in nicks if len(x) <= 16] 

	for nick in nicks:
	    r = requests.get('https://lolnames.gg/en/br/' + nick)
	    if 'Cleanup date (if inactive)' not in r.text:
	        print(nick + ' - DISPONIVEL')
	    else: 
	    	index = r.text.find('(if inactive)')
    		print(nick + ' - ' + r.text[index + 15:index + 26])

elif (opc == 3):
	while (True):
		nick = input('Insira o nick: ')
		if (len(nick) > 16):
			print(f'O nick possui mais que 16 caracteres ({len(nick)} caracteres). Tente novamente')
		else:
			break
	r = requests.get('https://lolnames.gg/en/br/' + nick)
	if 'Cleanup date (if inactive)' not in r.text:
	    print(nick + ' - DISPONIVEL')
	else:
		index = r.text.find('(if inactive)')
		print(nick + ' - ' + r.text[index + 15:index + 26])

elif (opc == 4):
	verificar('livres')

else:
	print('Opcao invalida, tente novamente')

try:
	r.close()
except:
	pass