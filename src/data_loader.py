import pandas as pd

def load_data(ratings_link, movies_link):
    ratings = pd.read_csv(ratings_link,sep='\t',names = ['user_id','movie_id','rating','timestamp'])
    movies = pd.read_csv(movies_link,sep='|',encoding='latin-1',names = ['movie_id','movie_title'] + list(range(22)))
    movies = movies[['movie_id','movie_title']]
    ratings = ratings.drop('timestamp', axis=1)
    data = pd.merge(ratings, movies, on='movie_id')

    print('Data loaded successfully')
    return data

