PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('cual es la contraseña?.. ')
        if password == PASSWORD:
            return func()
        else:
            print('la contraseña no es correcta.')
    return wrapper

    
@password_required
def needs_password():
    print('LA CONTRACEÑAS ES CORRECTA')

def upper(func):
    def wrapper(*args, **kwargs): # quiero los parametros tal cual son
        result = func(*args, **kwargs)
        return result.upper() # combierte todo a mayusculas
    return wrapper

@upper  # es undecorador para 'say_my_name'
def say_my_name(name):
    return('hola, {}'.format(name))


if __name__ == "__main__":
    #needs_password()
    print(say_my_name('Ruber'))