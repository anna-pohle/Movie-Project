import random
import movie_storage_sql as movie_storage
from sys import exit


print(f"{20 * '*'} My Movies Database {20 * '*'}")  # display title of application

menu_options = {0: "Exit",
                1: "List Movies",
                2: "Add Movie",
                3: "Delete Movie",
                4: "Update Movie",
                5: "Stats",
                6: "Random Movie",
                7: "Search Movies",
                8: "Show Movies sorted by rating"
                }


def main():
    """
    CLI accessing a movie database; two basic types of commands:
    CRUD: Create, Read, Update, Delete.
    Analytics: Top-rated movies, least-rated movies etc.
    display options to user
    execute the chosen function
    re-run program if user presses enter  (==empty input string)
    """
    movies_inventory = movie_storage.get_movies()
    while True:
        display_menu(menu_options)
        user_choice(movies_inventory)


def display_menu(menu_options):
    """
    show menu options
    """
    print("")
    for key, value in menu_options.items():
        print(f"{key}.: {value}")
    print("")


def user_choice(movies_inventory):
    """
    translate user input into menu choice
    """
    while True:
        user_choice_input = input("Please enter your choice (0-8) or press 'm' for menu: ")
        if user_choice_input == "0":
            print("Bye!")
            exit(0)
        elif user_choice_input == "1":
            list_movies()
        elif user_choice_input == "2":
            add_movie()
        elif user_choice_input == "3":
            delete_movie()
        elif user_choice_input == "4":
            update_movie()
        elif user_choice_input == "5":
            stats()
        elif user_choice_input == "6":
            random_movie()
        elif user_choice_input == "7":
            search_movie()
        elif user_choice_input == "8":
            movies_sorted_by_rating()
        elif user_choice_input == "m":
            display_menu(menu_options)
        else:
            print("invalid input")


def list_movies():
    """
    Option 1
    Print all the movies, along with their rating.
    In addition, the command prints how many movies there are in total in the database.
    """
    movies = movie_storage.get_movies()
    print(f"{len(movies)} movies in total")
    for movie, data in movies.items():
        print(f"{movie} ({data['year']}): {data['rating']}")



def add_movie():
    movies_inventory = movie_storage.get_movies()
    """
    Option 2
    Ask the user to enter a movie name and a rating.
    There is no need to validate the input
    (assume that the rating is a number between 1-10).
    """
    while True:
        new_title = input("Please enter the name of the movie you want to add: ")
        if len(new_title) == 0:
            print("Name cannot be empty.")
            print("")
            continue
        elif movies_inventory.get(new_title):
            print("The movie you want to add is already in the list.")
            print("")
            return None
        else:
            break
    while True:
        rating_input = (input("Please enter the rating of the movie you want to add: "))
        try:
            new_title_rating = float(rating_input)
            if not 0 <= new_title_rating <= 10:
                print("Please enter a positive number between 1 and 10.")
                continue
            else:
                break
        except ValueError:
            print("The rating must be a number.")
            print("")
            continue
    while True:
        year_input = (input("Please enter the publishing year of the movie you want to add: "))
        try:
            new_title_year = int(year_input)
            if not 1800 <= new_title_year <= 2025:
                print("Please enter a year between 1800 and 2025.")
                continue
            else:
                break
        except ValueError:
            print("The year must be a number.")
            print("")
            continue
    #{new_title: {"rating": new_title_rating, "year": new_title_year}}
    movie_storage.add_movie(new_title, new_title_year, new_title_rating)

    print(f"Successfully added the film '{new_title}' from the year {new_title_year}",
          f"with a rating of {new_title_rating} to the list.")
    print("")


def delete_movie():
    """
    Option 3
    Ask the user to enter a movie name, and delete it.
    If the movie doesn’t exist in the database, print an error message.
    """
    movies_inventory = movie_storage.get_movies()
    delete_movie_name = input(
        "Please enter the name of the movie you want to delete: ")
    while True:
        if delete_movie_name in movies_inventory.keys():
            del movies_inventory[delete_movie_name]
            movie_storage.delete_movie(delete_movie_name)
            print(f"The chosen movie {delete_movie_name} was successfully removed.")
            print("")
            break
        else:
            print(f"The movie {delete_movie_name} is not in the database.")
            continue


def update_movie():
    """
    Option 4
    Ask the user to enter a movie name, and then check if it exists.
    If the movie doesn’t exist prints an error message.
    If it exists, ask the user to enter a new rating,
    and update the movie’s rating in the database.
    There is no need to validate the input.
    """
    movies_inventory = movie_storage.get_movies()
    update_movie_name = input("Please enter the name of the movie you want to update: ")
    if update_movie_name not in movies_inventory.keys():
        print(f"The movie '{update_movie_name}' is not in the database.")
    else:
        while True:
            update_movie_rating_input = input("Please enter the films new rating: ")
            try:
                update_movie_rating = float(update_movie_rating_input)
                if not 0 <= update_movie_rating <= 10:
                    print("Please enter a positive number between 1 and 10.")
                    continue
                else:
                    break
            except ValueError:
                print("The rating must be a number.")
                print("")
                continue
        #movies_inventory[update_movie_name]["rating"] = update_movie_rating
        movie_storage.update_movie(update_movie_name, update_movie_rating)
        print(f"The chosen movie {update_movie_name} was successfully updated to rating {update_movie_rating}.")


def stats():
    """
    Option 5
    print statistics about movies in the database:
    1: average rating
    2: median rating
    3: best movie
    4: worst movie
    """
    movies_inventory = movie_storage.get_movies()
    ratings = []
    for film, info in movies_inventory.items():
        ratings.append(info["rating"])
    ratings.sort()

    avg_rating = get_avg_rating(ratings)
    median_rating = get_median_rating(movies_inventory, ratings)
    best_movie_by_rating = get_best_movie_by_rating(movies_inventory, ratings)
    worst_movie_by_rating = get_worst_movie_by_rating(movies_inventory, ratings)
    print("")
    print("Movie Statistics:\n")
    print(f"The average rating is: {avg_rating}\n")
    print(f"The median rating is: {median_rating}\n")
    print("The best movie(s) is/are:")
    for movie, rating in best_movie_by_rating.items():
         print(f"'{movie}', with a rating of {rating}")
    print("\nThe worst movie(s) is/are:")
    for movie, rating in worst_movie_by_rating.items():
        print(f"'{movie}', with a rating of {rating}")
    print("")


def get_avg_rating(ratings):
    """
    stats1: avg rating
    avg rating is sum of all ratings divided by number of ratings
    """
    avg = round((sum(ratings)) / (len(ratings)), 2)
    return avg


def get_median_rating(movies_inventory, ratings):
    """
    stats2: median
    for uneven numbers, the median is the middle number
    for even numbers, the median is the average of the two middle numbers
    """
    if len(movies_inventory) % 2 != 0:
        median_rating = ratings[(len(movies_inventory) // 2)]
    else:
        median_rating = (ratings[(len(movies_inventory) // 2) - 1] + ratings[(len(movies_inventory) // 2)]) / 2
    return median_rating


def get_best_movie_by_rating(movies_inventory, ratings):
    """
    stats3: best movie by rating.
    If there are multiple movies with the maximum rate, print all of them.
    """
    best_rating = ratings[-1]
    best_movie_s = {}
    for movie, info in movies_inventory.items():
        if info["rating"] == best_rating:
            best_movie_s[movie] = info["rating"]
    return best_movie_s


def get_worst_movie_by_rating(movies_inventory, ratings):
    """
    stats4: worst movie by rating
    If there are multiple movies with the minimum rate, print all of them.
    """
    worst_rating = ratings[0]
    worst_movie_s = {}
    for movie, info in movies_inventory.items():
        if info["rating"] == worst_rating:
            worst_movie_s[movie] = info["rating"]
    return worst_movie_s


def random_movie():
    """
    Option 6
    Display random movie
    from the list of all items in dict, choose a random one.
    print random movie and its rating.
    """
    movies_inventory = movie_storage.get_movies()
    movie, rating = random.choice(list(movies_inventory.items()))
    print("Your randomly chosen movie is:")
    print(movie, rating)
    print("")


def search_movie():
    """
    Option 7
    Ask the user to enter a movie name, and then check if it exists.
    If the movie doesn’t exist prints an error message.
    If it exists, ask the user to enter a new rating,
    and update the movie’s rating in the database.
    There is no need to validate the input.
    """
    movies_inventory = movie_storage.get_movies()
    user_looking_for = input("Please enter (a part of) the movie you are looking for: ")
    user_looking_for = user_looking_for.lower()
    for movie, rating in movies_inventory.items():
        if user_looking_for in movie.lower():
            print(movie, rating)
        else:
            print(f"Could not find movie '{user_looking_for}' in the database.")
    print("")


def get_value(item):
    """
    extract movie-rating from database
    """
    return item[1]["rating"]


def movies_sorted_by_rating():
    """
    Option 8
    Print all the movies and their ratings, in a descending order by the rating.
    (best movie first and the worst movie last.)
    """
    movies_inventory = movie_storage.get_movies()
    movies_list_sorted = sorted(movies_inventory.items(), key=get_value, reverse=True)
    print("")
    print("All movies in the database, from best to worst:")
    for title, info in movies_list_sorted:
        print(f"{title}: {info['rating']}")
    print("")


if __name__ == "__main__":
    main()
