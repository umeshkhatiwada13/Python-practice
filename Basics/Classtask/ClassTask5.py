# # defining function with default size and message
# def make_shirt(size="L", message="I Love Python"):
#     print("Size is : {0} and message : {1}".format(size, message))
#
# # Call the function for default size and message
# make_shirt()
#
# # Call function for medium size and default message
# make_shirt(size="M")
#
# # Call function for default size and different message
# make_shirt(message="Hello World")
#
# # Call function for non-default size and message
# make_shirt(message="Hello World from Positional", size="L")

# defining function with default city and country
# def describe_city(city="Kathmandu", country="Nepal"):
#     print("{0} is in {1}".format(city, country))
#
# # Call the function for default city and country
# describe_city()
# # Call the function for non-default city and country
# describe_city("Ottawa", "Canada")
# describe_city(city="Wasington", country="USA")

# def city_country(city, country):
#     print('"{0}, {1}"'.format(city, country))
#
# city_country("Lima", "Peru")
# city_country("Roi de Jenerio", "Brazil")
# city_country("New-Delhi", "India")

# Declare function
# Initialize the function
# def make_album(artist_name, album_title):
#     # initializing dictionary with artist_name as key and album_title as value
#     album = {"Name": artist_name, "Album": album_title}
#     return album
#
#
# # calling the function and printing the dictionary created by the function
# john_album = make_album("John Legend", "Stand by Me")
# for key, item in john_album.items():
#     print("{0} : {1}".format(key, item))
#
# michale_album = make_album("Michale Jackson", "Michale Album")
# for key, item in michale_album.items():
#     print("{0} : {1}".format(key, item))
#
# sakira_album = make_album("Ole Ole", "Shakira")
# for key, item in sakira_album.items():
#     print("{0} : {1}".format(key, item))

def make_album(artist_name, album_title):
    # initializing dictionary with artist_name as key and album_title as value
    album = {"Name": artist_name, "Album": album_title}
    return album


# counter to keep track of user input
count = 0
# stop the while loop when user input 3 data
while count < 3:
    # user input for album name and artists
    album_name = input("Enter the Album name : ")
    artist = input("Enter the artist name : ")
    # call the function if user inputs artist and album name
    if album_name and artist:
        album = make_album(album_name, artist)
        for key, item in album.items():
            print("{0} : {1}".format(key, item))
        # increase the counter to track number of data inserted
        count += 1
    else:
        # if artist and album name are not inserted, print this message to user
        print("Enter Album and artist name first to continue.")
