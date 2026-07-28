from datetime import date


class User:
    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        today = date.today()
        has_had_birthday_this_year = (today.month, today.day) >= (
            self.date_of_birth.month,
            self.date_of_birth.day,
            )
        return (today.year - self.date_of_birth.year - (not has_had_birthday_this_year))


def require_adult(func):
    def wrapper(user: User, *args, **kwargs):
        if user.age < 18:
            raise PermissionError(
            f"Access denied: User {user.name} is only {user.age} years old and"
            " must be at least 18 to buy Alcohol"
        )
        return func(user, *args, **kwargs)
    return wrapper


@require_adult
def buy_alcohol(user: User):
    print(f"Transaction approved for {user.name}!, you can buy Alcohol")


def main():
    adult_user = User(name="Maribel", date_of_birth=date(1995, 5, 10))
    minor_user = User(name="Miguel", date_of_birth=date(2012, 8, 20))
    try:
        print(f"{adult_user.name}'s age: {adult_user.age}") 
        buy_alcohol(adult_user)
        print(f"{minor_user.name}'s age: {minor_user.age}")
        buy_alcohol(minor_user)
    except PermissionError as error:
        print(error)


if __name__=="__main__":
    main()