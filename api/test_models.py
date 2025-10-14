from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()


# tester la recuperation de qqs films
movies = db.query(Movie).limit(5).all()

for movie in movies:
    print(f"ID : {movie.movieId} | Title : {movie.title} | Genres : {movie.genres}")
    
print("\n")
# Récupérer les films du genre action :
action_movie = db.query(Movie).filter(Movie.genres.like('%Action%')).limit(10)

for movie in action_movie:
    print(f"ID : {movie.movieId} | Title : {movie.title} | Genres : {movie.genres}")
    
print("\n")

# Récupérer les evaluations du genre action :
Ratings = db.query(Rating).limit(5)

for i in Ratings:
    print(f"UserID : {i.userId} | MovieID : {i.movieId} | Rating : {i.rating} | Timestamp : {i.timestamp}")
    

# Récupérer les evaluations > 4 :

Ratings = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating > 4.0)
    .limit(5)
    .all()

)
for title, rating in Ratings:
    print(f"Title : {title} | Rating : {rating}")
    
    # fermer la session
db.close()
