import csv
import matplotlib.pyplot as plt

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
    """
    It sorts the data by the number of weeks on the board, then iterates through the sorted list and
    adds the song to a list of unique songs if it's not already in the list and the list is not full

    Args:
      data: the list of song details dictionaries
    """
    longestnumberofweekssongs = sorted(
        data, key=lambda d: int(d["weeks-on-board"]), reverse=True
    )
    uniquesonglist = []
    for songs in longestnumberofweekssongs:
        if songs["song"] not in uniquesonglist and len(uniquesonglist) != 10:
            uniquesonglist.append(songs["song"])
            print(songs["song"], songs["weeks-on-board"])


def song_moved_the_most_in_ranking_on_the_board(data):
    """
    It first creates a dictionary of unique songs and their ranks, then it creates a dictionary of
    unique songs and the number of times their rank changed, then it sorts the second dictionary by the
    number of times the rank changed, and finally it prints the song that changed the most in ranking on the board


    Args:
      data: the list of song details dictionaries
    """
    uniquesonglist = {}
    numberofrankofthesong = {}
    sortedsongs = sorted(data, key=lambda s: s["rank"])
    for songs in sortedsongs:
        if songs["song"] in uniquesonglist:
            if songs["rank"] != uniquesonglist[songs["song"]]:
                if songs["song"] not in numberofrankofthesong:
                    numberofrankofthesong[songs["song"]] = 2
                else:
                    numberofrankofthesong[songs["song"]] += 1
                uniquesonglist[songs["song"]] = songs["rank"]
        else:
            uniquesonglist[songs["song"]] = songs["rank"]
    sortedlist = sorted(numberofrankofthesong.items(), key=lambda x: x[1], reverse=True)
    print("Song Name: ", sortedlist[0][0])
    # print(marklist)


def visualise_the_top_songs(data):
    """
    It takes the data, sorts it by the number of weeks on board, then creates a list of the top 3 songs
    with the longest number of weeks on board, and then plots a bar chart of the songs and the number of
    weeks on board
    
    Args:
      data: the list of song details dictionaries
    """
    longestnumberofweekssongs = sorted(
        data, key=lambda d: int(d["weeks-on-board"]), reverse=True
    )
    uniquesonglist = []
    weekslist = []
    for songs in longestnumberofweekssongs:
        if songs["song"] not in uniquesonglist and len(uniquesonglist) != 3:
            uniquesonglist.append(songs["song"])
            weekslist.append(int(songs["weeks-on-board"]))
    plt.bar(uniquesonglist, weekslist)
    plt.xlabel("Song Names")
    plt.ylabel("Weeks On Board")
    plt.title("Top 3 songs with the longest number of weeks on the board")
    plt.show()


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
    
    Please enter your choice:"""
        )
    )
    print("")
    functions = {
        1: top_ranked_songs,
        2: top_ranked_songs_artist,
        3: songs_with_the_longest_number_of_weeks_on_the_board,
        4: song_moved_the_most_in_ranking_on_the_board,
        5: visualise_the_top_songs,
    }
    functions[user_input](data_list)

    menu()


# top_ranked_songs(data_list)
menu()
# top_ranked_songs_artist(data_list)
# print(data_list)
# songs_with_the_longest_number_of_weeks_on_the_board(data_list)
# visualise_the_top_songs(data_list)
