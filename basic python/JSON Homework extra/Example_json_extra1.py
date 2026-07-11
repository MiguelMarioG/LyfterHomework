import json

def read_json_pokemon (path):
    with open (path, "r", encoding = "utf-8") as file:
        pokemon = json.load(file)
    return pokemon


def show_pokemon_stats (pokemon_info):
    for pokemon in pokemon_info:
        print(f"--------------- Your Pokemon Information ---------------")
        for index, data in pokemon.items():
            print(f"{index} : {data}")
        print()

def main ():
    pokemon_info = read_json_pokemon("list_pokemon.json")
    show_pokemon_stats (pokemon_info)


if __name__ == "__main__":
    main()

