ratings_link = 'data/raw/ml-100k/u.data'
movies_link = 'data/raw/ml-100k/u.item'
data_link = 'data/raw/data.csv'
from src.data_loader import load_data
from src.preprocessing import preprocess_data   

if __name__ == "__main__":
   data =  load_data(ratings_link, movies_link)
   data.to_csv('data/raw/data.csv', index=False)
   user_matrix = preprocess_data(data_link)
   user_matrix.to_csv('data/preprocessed/user_matrix.csv', index=False)
