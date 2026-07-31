user_logged_in = True
# user_logged_in = False


def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("Usuario no autenticado")
        return func(*args, **kwargs)
    return wrapper


@requires_login
def view_profile():
    return ("Mostrando el perfil del usuario")

print(view_profile())