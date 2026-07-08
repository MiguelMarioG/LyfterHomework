import json

def read_json_pokemon (path):
    with open (path, "r", encoding = "utf-8") as file:
        pokemon = json.load(file)
    return pokemon


def search_pokemon_type (pokemon_info):
    for pokemon in pokemon_info:
        pokemon_type = pokemon["type"]
    return pokemon_type


def get_pokemon_total_by_type (pokemon_info, pokemon_type):
    total_counting = 0
    for pokemon in pokemon_info:
        if pokemon_type == pokemon["type"]:
            total_counting += 1
    return total_counting


def get_pokemon_level_total (pokemon_info, pokemon_type):
    level_total = 0
    for pokemon in pokemon_info:
        if pokemon_type == pokemon["type"]:
            level_total += pokemon["level"]
    return level_total


def average_pokemon_level (total_by_type, total_by_level):
    average = total_by_level / total_by_type
    return average


def main ():
    pokemon_info = read_json_pokemon ("list_pokemon.json")
    processed_pokemon_type = []
    for pokemon in pokemon_info:
        pokemon_type = pokemon["type"]
        if pokemon_type not in processed_pokemon_type:
            total_by_type = get_pokemon_total_by_type (pokemon_info, pokemon_type)
            total_by_level = get_pokemon_level_total (pokemon_info, pokemon_type)
            average_total = average_pokemon_level (total_by_type, total_by_level)
            processed_pokemon_type.append(pokemon_type)
            print(f"Type: {pokemon_type} → Average level: {average_total}")


if __name__ == "__main__":
    main()

