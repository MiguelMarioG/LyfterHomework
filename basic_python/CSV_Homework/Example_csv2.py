import csv


def save_series_ranking(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


top_10_ranking = [
    {
        "Name": "Avatar: The Last Airbender",
        "Platform": "Nickelodeon",
        "Score": 9.3,
        "Episodes": 61,
        "Seasons": 3,
        "Genre": "Animation",
        "Year": 2005,
        "Director": "Michael Dante DiMartino",
    },
    {
        "Name": "Rick and Morty",
        "Platform": "Adult Swim",
        "Score": 9.1,
        "Episodes": 71,
        "Seasons": 7,
        "Genre": "Comedy",
        "Year": 2013,
        "Director": "Justin Roiland",
    },
    {
        "Name": "Batman: The Animated Series",
        "Platform": "Fox Kids",
        "Score": 9.0,
        "Episodes": 85,
        "Seasons": 4,
        "Genre": "Action",
        "Year": 1992,
        "Director": "Bruce Timm",
    },
    {
        "Name": "Arcane",
        "Platform": "Netflix",
        "Score": 9.0,
        "Episodes": 9,
        "Seasons": 1,
        "Genre": "Action",
        "Year": 2021,
        "Director": "Pascal Charrue",
    }
]


save_series_ranking('new_series_ranking.csv', top_10_ranking)


