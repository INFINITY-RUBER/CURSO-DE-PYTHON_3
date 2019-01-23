import sys
# clase 25 se hace actualizacion el las entradas
# con dicionario y ID 


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
	{
        'name': 'Ruber',
        'company': 'Ericsson',
        'email': 'ruber@facebook.com',
        'position': 'Engineer teleco',
    },
]
 #creamos el dicionario


def create_client(client):
	global clients  # Utilizamos global para definir que la variable es la globarl, es decir la que definimos con pablo y ricardo

	if client not in clients:
		clients.append(client)

	else:
		print('client already is the client\'s list')

def list_clients():#función que muestra la lista de clientes
	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(# imprime todos los elementos que estan dentro del {}
			uid=idx, 
			name=client['name'],
			company=client['company'],
			email=client['email'],
			position=client['position']
			)) 


def update_client(client_id, updated_client):
	global clients

	if len(clients)-1 >= client_id:
		clients[client_id] = updated_client
	else:
		print('client is Not in clients list')

def delete_client(client_id):
	global clients

	for idx, client in enumerate(clients):
		if idx == client_id:
			del clients[idx]
		break


def search_client(client_name):
	for client in clients:
		if client != client_name:
			continue 
		else:
			return True



def _get_client_field(field_name, messege='What is the client {}?.. '):
	field = None

	while not field:
		field = input(messege.format(field_name))
	return field


def _get_cliente_name():
	client_name = None # asigna como variable vacia
	while not client_name: # espera hasta que escriva un cliente
		client_name = input('what is the cliente name?..')
		if client_name == 'exit': # si escribe exit se sale de book
			client_name = None # asigna como variable vacia
			break
	if not client_name:
			sys.exit()
	return client_name

def _get_client_from_user():
	client = {
		'name': _get_client_field('name'),
		'company': _get_client_field('company'),
		'email': _get_client_field('email'),
		'position': _get_client_field('position'),
	}
	return client

def _print_welcome():
	 print('WELCOME TO PLATZI VENTAS')
	 print('*' * 50)
	 print('what would you to do today')
	 print('[C]reate cliente')
	 print('[U]pdate cliente')
	 print('[D]elete cliente')
	 print('[L]ist cliente')
	 print('[S]earch cliente')

if __name__ == '__main__': #funcion main
	_print_welcome()
	command = input()
	command = command.upper()
	if command == 'C':
		client = _get_client_from_user()

		create_client(client)
		list_clients()	     #Listamos los clientes
	elif command == 'L':
		list_clients()

	elif command == 'U':
		client_id = int(_get_client_field('id'))
		updated_client = _get_client_from_user()

		update_client(client_id, updated_client)
		list_clients()	
	elif command == 'D':
		client_id = int(_get_client_field('id'))
		delete_client(client_id)
		list_clients()
	
	elif command == 'S':
		client_name = _get_client_field('name')
		found = search_client(client_name)

		if found:
			print('The client is in the client\'s list')
		else:
			print('The Client: {} is not our client\'s list'.format(client_name))

	else:
		print('invalid command')
