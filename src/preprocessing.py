import pandas as pd


def preprocess_data(data_link):
    data = pd.read_csv(data_link)
    
    # Remove duplicates
    data = data.drop_duplicates()
    
    # Filter out users with less than 20 ratings
    user_counts = data['user_id'].value_counts()
    active_users = user_counts[user_counts > 20].index
    data = data[data['user_id'].isin(active_users)]
    
    # Filter out movies with less than 20 ratings
    movie_counts = data['movie_id'].value_counts()
    active_movies = movie_counts[movie_counts > 20].index
    data = data[data['movie_id'].isin(active_movies)]
    
    
    
    
    print("Data preprocessing completed.")
    print(f"Data shape after preprocessing: {data.shape}")
    return data
    
   
    
    