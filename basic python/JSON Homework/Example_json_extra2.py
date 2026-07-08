import json

def read_json_pokemon (path):
    with open (path, "r", encoding = "utf-8") as file:
        pokemon = json.load(file)
    return pokemon


def search_pokemon_type (pokemon_info):
    pokemon_type = input("Enter the type of the pokemon you want to search(water, electric, fire, etc.): ")
    pokemon_names = []
    for pokemon in pokemon_info:
        if pokemon["type"] == pokemon_type:
            pokemon_names.append(pokemon["name"])
    pokemon_name_order = "\n".join(pokemon_names)               #tuve que buscar un poco en codigos pasados para usar el join y que se viera el resultado mas estetico que impreso como una lista
    print(f"Your pokemons with the type {pokemon_type}:")       
    print(pokemon_name_order)


def main ():
    pokemon_info = read_json_pokemon("list_pokemon.json")
    search_pokemon_type(pokemon_info)


if __name__ == "__main__":
    main()
