from database import SessionLocal
from api.query_helpers import *

db = SessionLocal()

movies = get_movies(db, limit=5)
for film in movies:
    print(f"{film.movieId} ({film.title}) - {film.genres}")
    
print("\n")

rating = get_rating(db, movie_id=1, user_id=1)
print(f"Rating for movie 1 by user {rating.userId}: {rating.rating}")

print("\n")

ratings = get_ratings(db, min_rating=3.5, limit=5)
for film in ratings:
    print(f"{film.movieId} - {film.rating}")

print("\n")

# tag = get_tag(db, user_id=1, movie_id=1, tag_text="funny")
# print(tag)
# print(f"Tag found: {tag.userId} for movie {tag.movieId} by user {tag.tag}")

n_movies = get_movie_count(db)
print(f"Total number of movies: {n_movies}")



db.close()