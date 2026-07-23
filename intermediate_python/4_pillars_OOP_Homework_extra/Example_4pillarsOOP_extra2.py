from abc import ABC, abstractmethod


class User():

    @abstractmethod
    def get_role(self) -> str:
        pass

    @abstractmethod
    def has_permission(self, permission: str ) -> bool:
        pass


class AdminUser(User):
    def __init__(self, name: str):
        self.name= name

    def get_role(self):
        print(f"{self.name}, Your Role is Administrator")

    def has_permission(self, permission: str) -> bool:
        return True

class RegularUser(User):
    def __init__(self, name: str):
        self.name= name

    def get_role(self):
        print(f"{self.name}, Your Role is a Regular User")

    def has_permission(self, permission: str) -> bool:
        return permission == "read"

def main():
    user1 = AdminUser("Miguel")
    user2 = RegularUser("Maribel")

    user1.get_role()
    user2.get_role()

    print(user1.has_permission("delete"))
    print(user2.has_permission("delete"))
    print(user2.has_permission("read"))


if __name__=="__main__":
    main()