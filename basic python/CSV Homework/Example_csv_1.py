import csv

def asking_data ():
    list_videogame_info = []
    index = True
    while index == True:
        print("-------------- Your VideoGame Information --------------")
        name = input("Enter the Videogame name: ")
        gender = input("Enter the Gender of your Videogame: ")
        developer = input("Enter the Developer of the Videogame: ")
        classification = input("Enter the Classification of your Videogame: ")

        videogame_info = {
            "Name": name,
            "Gender": gender,
            "Developer": developer,
            "Classification ESRB": classification
        }

        list_videogame_info.append(videogame_info)
        print()
        option = input("Do you want to add another Videogame Information (y or n): ")
        if option != "y":
            index = False            
    return list_videogame_info


def input_data (path, data):
    with open(path, 'w', encoding='utf-8', newline="") as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    return(data)


def main():
    video_games_data = asking_data()
    dict_videogame = input_data ("video_games.csv", video_games_data)
    print(dict_videogame)


if __name__ == "__main__":
    main()