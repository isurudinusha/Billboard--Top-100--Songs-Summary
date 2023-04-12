import csv

# Reading the csv file and storing it in a list.
data_list = []
csv_file = open("charts.csv", mode="r")
billboard_data = csv.DictReader(csv_file)
for data in billboard_data:
    data_list.append(data)


def menu():
    """
    It prints a menu, asks the user to input a number, and then calls itself.
    """
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
    menu()


menu()
