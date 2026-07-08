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


def write_separate_data (path, data):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter= "\t")
        writer.writeheader()
        writer.writerows(data)
    return(data)


def main():
    file_name = input("Enter the name of your file: ") + ".csv"
    video_game_data = asking_data()
    sep_final = write_separate_data (file_name, video_game_data)
    print(sep_final)


if __name__ == "__main__":
    main()


