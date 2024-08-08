<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Recommender System</title>
</head>
<body>

<h1>Movie Recommender System</h1>

<p>Welcome to the Movie Recommender System project! This project leverages machine learning techniques to recommend movies based on user preferences.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#model">Model</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
</ul>

<h2 id="introduction">Introduction</h2>
<p>The Movie Recommender System is designed to suggest movies to users based on their previous ratings and preferences. This system uses collaborative filtering techniques to provide personalized recommendations.</p>

<h2 id="features">Features</h2>
<ul>
    <li>Collaborative filtering for movie recommendations</li>
    <li>User-based and item-based filtering</li>
    <li>Easy-to-use interface with Streamlit</li>
    <li>Scalable to accommodate large datasets</li>
</ul>

<h2 id="installation">Installation</h2>
<p>To install and run this project, follow these steps:</p>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/Pratham1708/Movie-Recommender.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd Movie-Recommender</code></pre>
    </li>
    <li>Install the required dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h2 id="usage">Usage</h2>
<p>To use the Movie Recommender System with Streamlit:</p>
<ol>
    <li>Ensure you have installed all dependencies as described in the Installation section.</li>
    <li>Run the Streamlit application using the following command:
        <pre><code>streamlit run app.py</code></pre>
    </li>
    <li>A web browser should open automatically with the Streamlit interface. If not, navigate to <code>http://localhost:8501</code> in your browser.</li>
    <li>Select a movie from the dropdown menu and click the "Recommend" button to see the list of recommended movies.</li>
</ol>

<h2 id="dataset">Dataset</h2>
<p>The dataset used in this project is the <a href="https://github.com/Pratham1708/Movie-Recommender/blob/main/datasets/IMDB-Movie-Dataset(2023-1951).csv">IMDB Movie Dataset</a>. It contains a large collection of movie ratings provided by users.</p>

<h2 id="model">Model</h2>
<p>The recommendation model is based on collaborative filtering techniques, including user-based and item-based filtering. It leverages the similarity between users or items to provide accurate recommendations.</p>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.</p>
<ol>
    <li>Fork the Project</li>
    <li>Create your Feature Branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
    <li>Commit your Changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
    <li>Push to the Branch (<code>git push origin feature/AmazingFeature</code>)</li>
    <li>Open a Pull Request</li>
</ol>

<h2 id="contact">Contact</h2>
<p>Pratham Jindal - <a href="mailto:jindalpratham68@gmail.com">Gmail</a></p>
<p>Project Link: <a href="https://pratham-movie-recommender.streamlit.app/">Streamlit</a></p>

</body>
</html>
