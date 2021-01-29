import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

movie_genres = pd.read_csv('movie_genres.csv')
user_reviews = pd.read_csv('user_reviews.csv')
genre_only = movie_genres.iloc[:, 2:]

user = 0
ratings = user_reviews.iloc[user, 2:]
best_ind = np.argmax(ratings, axis=0)
best_title = user_reviews.columns[best_ind]

rated_movies = np.where(ratings > 0)
# movie1 = genre_only[movie_genres.movie_title == best_title].values
rating = []


jt = 127
movie1 = genre_only.iloc[jt, :].values
score = ratings[rated_movies[0][1]]

for it in range(len(genre_only)):

    if (it not in rated_movies[0]):

        movie2 = genre_only.iloc[it, :].values
        csn_sim = cosine_similarity(
            movie1.reshape(1, -1), movie2.reshape(1, -1))
        rating.append(csn_sim[0]*score)
        if csn_sim*score > 2.9:
            print(movie2)

rating = np.array(rating).reshape(1, -1)
top5 = rating.argsort()[0][len(rating)-6:]
top5 = top5[::-1]
print(user_reviews.columns[top5])
print(top5[0])
movie2 = genre_only.iloc[top5[0], :].values
print(movie2)est
print(movie1)
print(cosine_similarity(movie1.reshape(1, -1), movie2.reshape(1, -1)))
