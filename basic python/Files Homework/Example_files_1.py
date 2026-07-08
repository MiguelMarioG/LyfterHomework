def write_new_file (path, ordered_music):
    with open(path, "w", encoding="utf-8") as file:
        ordered_music.sort()
        file.writelines(ordered_music)
        print()
        print("--------------songs ordered alphabetically--------------")
        print(ordered_music)


def read_file (path):
    play_list = []
    with open(path, 'r', encoding='utf-8') as file:
        music_list = file.readlines()
        for number, line in enumerate(music_list, start=1):
            print(f"Song #{number}: {line.strip()}")
            play_list.append(line)
    return (play_list)


def main():
    order_music = read_file("music_list_rock.txt")
    write_new_file("music_list_rock_ordered.txt", order_music)


if __name__ == "__main__":
    main()



