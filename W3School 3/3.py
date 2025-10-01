# Dictionary of movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#Function: check if single movie score > 5.5-----------------------------------------------------------------------
def is_above_55(movie):
    return movie["imdb"] > 5.5

#Function: sublist of movies with IMDB score > 5.5-------------------------------------------------------------------
def high_rated_movies(movies_list):
    return [m for m in movies_list if m["imdb"] > 5.5]

#Function: movies in a specific category-------------------------------------------------------------------
def movies_by_category(movies_list, category):
    return [m for m in movies_list if m["category"].lower() == category.lower()]

#Function: average IMDB score of a list of movies-----------------------------------------------------------
def average_imdb(movies_list):
    if not movies_list:  # avoid division by zero
        return 0
    return sum(m["imdb"] for m in movies_list) / len(movies_list)

#Function: average IMDB score of a specific category----------------------------------------------------
def average_imdb_by_category(movies_list, category):
    category_movies = movies_by_category(movies_list, category)
    return average_imdb(category_movies)


# ------------------ Example Usage -------------------------------------------------------------------------

print("Is 'Hitman' above 5.5?", is_above_55(movies[1]))

print("\nHigh rated movies (>5.5):")
for m in high_rated_movies(movies):
    print(m["name"], m["imdb"])

print("\nRomance movies:")
for m in movies_by_category(movies, "Romance"):
    print(m["name"])

print("\nAverage IMDB score of all movies:", average_imdb(movies))

print("\nAverage IMDB score of Romance movies:", average_imdb_by_category(movies, "Romance"))
