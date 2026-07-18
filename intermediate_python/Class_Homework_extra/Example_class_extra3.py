class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products_list = []

    def add_a_product(self, product_object):
        self.products_list.append(product_object)

    def show_all_products(self):
        for product in self.products_list:
            print(f"{product.name}: ${product.price} (Quantity: {product.quantity})")
        print("===================================================================\n")

    def calculate_total_value_of_inventory(self):
        total = 0
        for product in self.products_list:
            total += product.price * product.quantity
        return total


def main():
    product1 = Product("Mouse", 5000, 3)
    product2 = Product("Keyboard", 8000, 2)

    data_product = Inventory()

    data_product.add_a_product(product1)
    data_product.add_a_product(product2)

    data_product.show_all_products()

    total_value = data_product.calculate_total_value_of_inventory()
    print(f"Total inventory value: ${total_value}")


if __name__ == "__main__":
    main()