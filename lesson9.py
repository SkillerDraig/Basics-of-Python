# Usage of Dictionaries

import time

# add more movies to the dictionary
movies = {
    "Inception": {"score": 8.8, "genre": "Sci-Fi"},
    "The Dark Knight": {"score": 9.0, "genre": "Action"},
    "Interstellar": {"score": 8.6, "genre": "Adventure"},
    "The Matrix": {"score": 8.7, "genre": "Sci-Fi"},
    "Pulp Fiction": {"score": 8.9, "genre": "Crime"},
    "The Shawshank Redemption": {"score": 9.3, "genre": "Drama"},
    "Fight Club": {"score": 8.8, "genre": "Drama"},
    "The Godfather": {"score": 9.2, "genre": "Crime"},
    "The Prestige": {"score": 8.5, "genre": "Mystery"},
    "Spirited Away": {"score": 8.6, "genre": "Animation"},
    "The Social Network": {"score": 7.7, "genre": "Drama"},
}

time.sleep(1)

for key in movies:
    print(f"{key}")

time.sleep(1)

movie_name = input("Enter a movie name: ")

if movie_name in movies:
    score = movies[movie_name]["score"]
    genre = movies[movie_name]["genre"]
    print(f"{movie_name} has a score of {score} and belongs to the {genre} genre.")


    