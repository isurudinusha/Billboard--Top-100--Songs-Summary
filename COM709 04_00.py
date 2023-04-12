import csv

# Reading the csv file and storing it in a list.
data_list = []
csv_file = open("charts.csv", mode="r")
billboard_data = csv.DictReader(csv_file)
for data in billboard_data:
    data_list.append(data)


def top_ranked_songs(data):
    """
    It filters the data to only include songs with a rank of 1, then sorts the list by date, and then
    prints the date and song name for each song

    Args:
      data: the list of song details dictionaries
    """
    toprankedsongs = list(filter(lambda x: x["rank"] == "1", data))
    toprankedsongs = sorted(toprankedsongs, key=lambda d: d["date"])
    for songs in toprankedsongs:
        print(songs["date"], songs["song"])


def top_ranked_songs_artist(data):
    """
    It filters the data to only include songs that have a rank of 1, sorts the data by date, and then
    prints the date, song, and artist for each song
    
    Args:
      data: the list of song details dictionaries
    """
    toprankedsongs = list(filter(lambda x: x["rank"] == "1", data))
    toprankedsongs = sorted(toprankedsongs, key=lambda d: d["date"])
    for songs in toprankedsongs:
        print(songs["date"], songs["song"], "-", songs["artist"])

def songs_with_the_longest_number_of_weeks_on_the_board(data):
    longestnumberofweekssongs = sorted(data, key=lambda d: int(d["weeks-on-board"]), reverse=True)
    uniquesonglist = []
    for songs in longestnumberofweekssongs:
        if songs["song"] not in uniquesonglist and len(uniquesonglist)!=10:
            uniquesonglist.append(songs["song"])
            print(songs["song"], songs["weeks-on-board"])
        

def menu():
    """
    It prints a menu, asks the user to input a number, and then calls itself.
    """
    print("")
    print("Billboard “Top 100” Songs Summary")
    print("-------------------------")
    user_input = int(
        input(
            """
    1.Retrieve the details for the top ranked song for a particular day
    2.Retrieve the details of the artist with the most top ranked songs
    3.Retrieve the details of the 10 songs with the longest number of weeks on the board
    4.Retrieve the song that has moved the most in ranking on the board
    5.Visualise the top songs
    0.Exit
    
    Please enter your choice: """
        )
    )

    functions = {1: top_ranked_songs, 2: top_ranked_songs_artist}
    functions[user_input](data_list)

    menu()


# top_ranked_songs(data_list)
# menu()
# top_ranked_songs_artist(data_list)
# print(data_list)
songs_with_the_longest_number_of_weeks_on_the_board(data_list)