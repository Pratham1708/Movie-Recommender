import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your dataset (replace with your actual data loading logic)
def load_dataset():
    # Replace this with your code to load the dataset from CSV or another source
    df = pd.read_csv(r"C:\Users\jinda\OneDrive\Desktop\IMDB-Movie-Dataset(2023-1951).csv")
    return df

# Preprocess data and create TF-IDF matrix (do this outside the function for efficiency)
def preprocess_data(df):
    df['combined_features'] = df['overview'].fillna('') + ' ' + df['cast'].fillna('')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    df['movie_name_lower'] = df['movie_name'].str.lower()  # Create a lowercased version of the movie names
    return df, tfidf_matrix, cosine_sim

# Function to get movie recommendations
def get_recommendations(movie_name, df, cosine_sim):
    movie_name_lower = movie_name.lower()
    
    # Get the index of the movie that matches the title (case-insensitive)
    idx = df.index[df['movie_name_lower'] == movie_name_lower].tolist()[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top 5 most similar movies
    top_5_scores = sim_scores[1:6]
    top_5_indices = [i[0] for i in top_5_scores]
    top_5_movies = df['movie_name'].iloc[top_5_indices].tolist()

    # Get the indices and scores of the remaining movies
    remaining_scores = sim_scores[6:]
    if remaining_scores:
        best_remaining_score = remaining_scores[0]
        best_remaining_movie = df['movie_name'].iloc[best_remaining_score[0]]
    else:
        best_remaining_movie = None

    return top_5_movies, best_remaining_movie

def main():
    # Custom CSS for styling
    st.markdown("""
        <style>
       body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f0f2f6;
        }
        .title {
            color: #1f77b4;
            text-align: center;
            margin-bottom: 20px;
        }
        .recommendations {
            margin: 20px 0;
        }
        .recommendations h2 {
            color: #ff7f0e;
        }
        .recommendations p {
            font-size: 18px;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Bollywood Movie Recommender")

    # Load data and preprocess
    df = load_dataset()
    df, tfidf_matrix, cosine_sim = preprocess_data(df)

    movie_titles = df['movie_name'].tolist()
    selected_movie = st.selectbox("Select a movie", movie_titles)

    if st.button("Recommend"):
        recommendations, best_remaining = get_recommendations(selected_movie, df, cosine_sim)
        st.markdown("<div class='recommendations'><h2>Top 5 Movies:</h2></div>", unsafe_allow_html=True)
        for movie in recommendations:
            st.write(movie)
        if best_remaining:
            st.markdown("<div class='recommendations'><h2>Best Remaining Movie:</h2></div>", unsafe_allow_html=True)
            st.write(best_remaining)

if __name__ == "__main__":
    main()
