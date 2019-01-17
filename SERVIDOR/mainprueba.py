clients = 'Pablo,Ricardo,claudia,yenni' #creamos el string


def create_client(client_name):
	global clients  # Utilizamos global para definir que la variable es la globarl, es decir la que definimos con pablo y ricardo

	if client_name not in clients:
		_add_coma()
		clients += client_name

	else:
		print('client already is the client\'s list')

def _add_coma():#el nombre de la función comienza con un guión bajo para establecer que será una funcion privada
	global clients
	clients +=","#se agrega una coma y un espacio al string para separar los nuevos valores

def list_clients():#función que muestra la lista de clientes
	global clients
	print (clients) #imprimimos el string clientes

def update_client(client_name, update_client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',' , update_client_name + ',')
	else:
		print('client is not in clients list')

def delete_client(client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', '')
	else:
		print('client is not in clients list')

def search_client(client_name):
	global clients
	clients_list = clients.split(',')

	for client in clients_list:
		
		if client != client_name:
			print(clients_list)
			print(client)
			print('buscar:', client_name)
			continue 
		else:
			return True

def _print_welcome():
	 print('WELCOME TO PLATZI VENTAS')
	 print('*' * 50)
	 print('what would you to do today')
	 print('[C]reate cliente')
	 print('[U]pdate cliente')
	 print('[D]elete cliente')
	 print('[L]ist cliente')
	 print('[S]earch cliente')

def _get_cliente_name():
	return input('what is the cliente name? ' + clients + '.. ')

if __name__ == '__main__': #funcion main
	_print_welcome()
	command = input()
	command = command.upper()
	if command == 'C':
		client_name = _get_cliente_name()
		create_client(client_name)
		list_clients()	     #Listamos los clientes
	elif command == 'D':
		client_name = _get_cliente_name()
		delete_client(client_name)
		list_clients()
	elif command == 'U':
		client_name = _get_cliente_name()
		update_client_name = input('what is the updated client name ')
		update_client(client_name, update_client_name)
		list_clients()
	elif command == 'L':
		list_clients()
	elif command == 'S':
		client_name = _get_cliente_name()
		found = search_client(client_name)

		if found:
			print('The client is in the client\'s list')
		else:
			print('The Client: {} is not our client\'s list'.format(client_name))

	else:
		print('invalid command')
