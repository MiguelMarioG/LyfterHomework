import json

def read_json_pokemon (path):
    with open (path, "r", encoding = "utf-8") as file:
        pokemon = json.load(file)
    return pokemon


def if_pokemon_is_shiny (p_is_shiny):
    try:
        if p_is_shiny == "y":
            p_is_shiny = True
        else:
            p_is_shiny = False
    except ValueError as error:
        print("Sorry you must to enter (y or n), you enter a invalid value")
    return p_is_shiny


def if_pokemon_held_item (p_held_item):
    try:
        if p_held_item == "n" or p_held_item == "":
            p_held_item = None
        else:
            p_held_item =  input("Enter what item your Pokemon is holding: ")
    except ValueError as error:
        print("Sorry you must to enter (y or n), you enter a invalid value")
    return p_held_item


def define_pokemon_skills ():
    skills_option = "y"
    skills_counter = 1
    pokemon_new_skills = []
    while skills_option == "y":
        pokemon_skills = input(f"Enter your Pokemon skill #{skills_counter}: ")
        pokemon_new_skills.append(pokemon_skills)
        skills_counter += 1
        try:
            skills_option = input("Do you want to add another skill (y or n): ")
        except ValueError as error:
                print("Sorry you must to enter (y or n), you enter a invalid value")
    return pokemon_new_skills


def write_new_pokemon (path, data_pokemon):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data_pokemon, file, indent=4)


def asking_pokemon_data (pokemon_info):
    print("----------------Your PokeDex Data----------------")
    pokemon_name = input("Enter your Pokemon name: ")
    pokemon_type = input("Enter your Pokemon type: ")
    pokemon_level = int(input("Enter your Pokemon level: "))
    pokemon_weight = float(input("Enter your Pokemon weight on kg: "))
    print()
    pokemon_is_shiny = input("Enter if your Pokemon is shiny (y or n): ")
    pokemon_is_shiny = if_pokemon_is_shiny(pokemon_is_shiny)
    print()
    pokemon_held_item = input("Enter if your Pokemon is holding an item: ")
    pokemon_held_item = if_pokemon_held_item(pokemon_held_item)
    print()
    pokemon_new_skills = define_pokemon_skills()
    pokemon_data = {
        "name": pokemon_name,
        "type": pokemon_type,
        "level": pokemon_level,
        "weight_kg": pokemon_weight,
        "is_shiny": pokemon_is_shiny,
        "held_item": pokemon_held_item,
        "skills": pokemon_new_skills,
        "stats":{}
    }
    print()
    pokemon_hp = int(input("Enter the HP points of your pokemon: "))
    pokemon_attack = int(input("Enter the ATTACK points of your pokemon:"))
    pokemon_defense = int(input("Enter the DEFENSE points of your pokemon: "))
    pokemon_sp_attack = int(input("Enter the SP-ATTACK points of your pokemon:"))
    pokemon_sp_defense = int(input("Enter the SP-DEFENSE points of your pokemon: "))
    pokemon_speed = int(input("Enter the SPEED points of your pokemon: "))
    pokemon_stats = {
        "hp": pokemon_hp,
        "attack": pokemon_attack,
        "defense": pokemon_defense,
        "sp_attack": pokemon_sp_attack,
        "sp_defense": pokemon_sp_defense,
        "speed": pokemon_speed
        }
    pokemon_data["stats"] = pokemon_stats
    pokemon_info.append(pokemon_data)
    return pokemon_info


def main ():
    file_name = input("Enter your file name: ") + ".json"
    pokemon_info = read_json_pokemon(file_name)
    data_pokemon = asking_pokemon_data(pokemon_info)
    write_new_pokemon (file_name, data_pokemon)


if __name__ == "__main__":
    main()

