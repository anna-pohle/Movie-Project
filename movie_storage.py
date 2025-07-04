import json


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    with open("data.json", "r") as fileobj:
        movies_inventory = json.load(fileobj)
        return movies_inventory


def save_movies(movies_inventory):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("data.json", "w") as fileobj:
        json.dump(movies_inventory, fileobj)


def add_movie(movies_inventory):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data.json", "w") as fileobj:
        json.dump(movies_inventory, fileobj)


def delete_movie(movies_inventory):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data.json", "w") as fileobj:
        json.dump(movies_inventory, fileobj)


def update_movie(movies):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data.json", "w") as fileobj:
        json.dump(movies, fileobj)
