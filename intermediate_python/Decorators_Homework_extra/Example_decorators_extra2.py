def requires_login(func):
    def wrapper(user_logged_in : bool, *args, **kwargs):
        if not user_logged_in:
            raise Exception("Unauthenticated user")
        return func(user_logged_in, *args, **kwargs)
    return wrapper


@requires_login
def view_profile(user_logged_in : bool):
    print("Showing user profile")


view_profile(True) 
view_profile(False)