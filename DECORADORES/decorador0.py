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


if __name__ == "__main__": # hace que se inicialice primero este codigo
    needs_password()
    