clients = 'Pablo, Ricardo' #creamos el string


def create_client(client_name):
	global clients  #Utilizamos global para definir que la variable es la globarl, es decir la que definimos con pablo y ricardo

	if client_name not in clients:
		clients += client_name
		_add_coma()
	else:
		print('client already is the client\'s list')

def _add_coma():#el nombre de la función comienza con un guión bajo para establecer que será una funcion privada
	global clients
	clients +=", "#se agrega una coma y un espacio al string para separar los nuevos valores

def list_clients():#función que muestra la lista de clientes
	global clients
	print (clients) #imprimimos el string clientes

def _print_welcome():
	 print('WELCOME TO PLATZI VENTAS')
	 print('*' * 50)
	 print('what would you to do today')
	 print('[C]reate cliente')
	 print('[D]elete cliente')


if __name__ == '__main__': #funcion main
	_print_welcome()
	command = input()
	if command == 'C':
		client_name = input('what is the cliente name? ')
		create_client(client_name)
		list_clients()	     #Listamos los clientes
	elif command == 'D':
		pass
	else:
		print('invalid command')
