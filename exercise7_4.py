# Create list, which contains dictionaries
# Create list, which contains dictionaries
movie1 = {
    "name": "Casablanca",
    "year": 1942,
}

movie2 = {
    "name": "Forrest Gump",
    "year": 1994,
}

movie3 = {
    "name": "Avatar",
    "year": 2009,
}
movie4 = {
    "name": "Man of Steel",
    "year": 2013,
}

movie5 = {
    "name": "Ironman",
    "year": 2008,
}

movie6 = {
    "name": "Superman 2",
    "year": 2010,
}
movies = [movie1, movie2, movie3, movie4, movie5, movie6]

# Create variables, which store the movies into two separate lists called old_movies and new_movies
old_movies = []
new_movies = []

# Create variables for year = 1000, x = 1
year = 2000

# Create a statement, which sorts and defines movies to their lists based on their year of release
for movie in movies:
    if movie["year"] < year:
        old_movies.append(movie["name"])
    else:
        new_movies.append(movie["name"])

# Create two loops, which print movies in both old_movies and new_movies
print("These movies have been released before the year 2000:\n" + ", ".join(old_movies))
print(f"These movies have been released on or after the year 2000:\n" + ", ".join(new_movies))
