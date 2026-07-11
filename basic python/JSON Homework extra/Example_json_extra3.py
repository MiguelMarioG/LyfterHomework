import json

def read_json_pokemon (path):
    with open (path, "r", encoding = "utf-8") as file:
        pokemon = json.load(file)
    return pokemon


def search_pokemon_stats (pokemon_info):
    pokemon_name = ""
    pokemon_stats = {}
    for pokemon in pokemon_info:
        pokemon_name = pokemon["name"]
        print(f"--------------- Your Pokemon Stats ---------------")
        print(f"Name: {pokemon_name}")
        pokemon_stats_order = []
        pokemon_stats = (pokemon["stats"])
        for key, value in pokemon_stats.items():
            pokemon_stats_order.append(f"{key} : {value}")
        print("\n".join(pokemon_stats_order))
        print()


def main ():
    pokemon_info = read_json_pokemon("list_pokemon.json")
    search_pokemon_stats(pokemon_info)


if __name__ == "__main__":
    main()

