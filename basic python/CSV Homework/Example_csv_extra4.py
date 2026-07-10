import csv

def search_for_developer (path, developer_option):
    dev_videogame = {}
    with open(path, 'r', encoding='utf-8') as file:
        developer = csv.DictReader(file)
        for index in developer:
            if index["Developer"] == developer_option:
                if developer_option not in dev_videogame:
                    dev_videogame[developer_option] = []
                index.pop("Developer")
                dev_videogame[developer_option].append(index)
    return dev_videogame     


def search_print (search_result):
    for developer, game_info in search_result.items():
        print(f"---------------------VideoGame developed by {developer}---------------------")
        for games_data in game_info:
            name = games_data.get("Name")
            gender = games_data.get("Gender")
            classification = games_data.get("Classification ESRB")
            print(f"{name} (Classification: {classification}, Gender: {gender})")
        print()


def main():
    developer_option = input("Enter the Developer your looking for: ")
    search_result = search_for_developer ("video_games.csv", developer_option)
    search_print(search_result)


if __name__ == "__main__":
    main()