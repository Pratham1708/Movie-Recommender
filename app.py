from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset
df = pd.read_csv(r'C:\Users\jinda\OneDrive\Desktop\IMDB-Movie-Dataset(2023-1951).csv')

# Create a combined feature
df['combined_features'] = df['overview'].astype(str) + ' ' + df['cast'].astype(str)

# Convert movie names to lower case for case-insensitive comparison
df['movie_name_lower'] = df['movie_name'].str.lower()

# Initialize the TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform the combined features
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(movie_name, df, cosine_sim):
    # Convert the input movie name to lower case
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie_name')
    top_5_movies, best_remaining_movie = get_recommendations(movie_name, df, cosine_sim)
    return jsonify({
        'top_5_movies': top_5_movies,
        'best_remaining_movie': best_remaining_movie
    })

if __name__ == '__main__':
    app.run(debug=True)
