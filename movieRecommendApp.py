# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Firstly, the code import necessary libraries
# After that, the code pulls movie data from csv file. 
# Then, it recommends movies using the difflib library and cosine similarity based on the inputs entered by the user. 
# Finally, it creates website using streamlit library.
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import streamlit as st #To convert the project into interactive web applications
from PIL import Image #To perform operations such as opening, manipulating, editing and saving image files
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# streamlit run movieRecommendApp.py

# Load the data from the csv file using pandas
movie_data = pd.read_csv('..\python\movieRecommend\movies.csv')

# Replace the null values with empty strings
selected_features = ['genres', 'keywords', 'original_title', 'tagline', 'cast', 'director']
for feature in selected_features:
    movie_data[feature] = movie_data[feature].fillna('')

# Combine all the selected features
combine_features = movie_data['genres'] + movie_data['keywords'] + movie_data['tagline'] + movie_data['cast'] + movie_data['director']

# Convert textual data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combine_features)

# Getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)

# Create a list with all the movie names in the dataset
title_list = movie_data['title'].tolist()
genre_list = movie_data['genres'].tolist()

# 'get_similar_movies' is a backend function. The function is the same as what we did in movieRecommend.ipynb. 
# It is just a collection of codes to be used for web application. 
def get_similar_movies(movie_name, movie_count=5):
    # Find the close match for the given input
    close_match = difflib.get_close_matches(movie_name, title_list)

    if not close_match:
        return []

    first_value = close_match[0]
    index = movie_data[movie_data.title == first_value]['index'].values[0]

    # Get the list of similar movies
    similarity_score = list(enumerate(similarity[index]))
    sorted_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    # Print the name of similar movies based on the index
    recommended_movies = []
    count = 0
    for movie in sorted_movies:
        idx = movie[0]
        title = movie_data[movie_data.index == idx]['title'].values[0]
        genre = movie_data[movie_data.index == idx]['genres'].values[0]
        if (count > 0) and (count <= movie_count):
            recommended_movies.append(title)
        count += 1

    return recommended_movies

# The main() function contains the main function of the web application.
def main():
    
     # to center the title
    st.markdown('<style> .centered-title { text-align: center; } </style>', unsafe_allow_html=True)
    st.markdown('<h1 class="centered-title">Movie Recommendation System</h1>', unsafe_allow_html=True)

    #to image open
    img1 = Image.open('poster.jpeg')
    img1 = img1.resize((500,250))
    st.image(img1,use_column_width=False,caption='Movie Recommendation Poster')

    #creates a text input box in the web application
    select_movie = st.selectbox('Select Movie: (Recommendation will be based on this selection)',['--Select--']+ title_list)
  
    #creates a number input box in the web application
    movie_count = st.number_input('How many movie suggestions do you want?', min_value=1, max_value=10, value=5) 
    #The input is assigned to the movie_count variable. Here, the minimum value is limited to 1 and 
    #the maximum value is 10, and the default value is set to 5.

    #creates a button in the web application
    #Clicking this button will execute the code block below.
    if st.button('Get recommendations'):

        #Checks that the user has entered a movie name. If the user has entered a movie name, the code block below will work.
        if select_movie:

            #By calling the get_similar_movies() function, it retrieves recommended movies based on the movie name the user entered.
            recommended_movies = get_similar_movies(select_movie, movie_count)

            #If there are recommended movies, the code block below will work.
            if recommended_movies:

                #The title with the recommended movies is printed.
                st.write('Recommended movies:')

                #The enumerate() function is used to enumerate and print the suggested movies. 
                #Enumerate returns elements as index and value in pairs in a loop.
                for i, movie,genre in enumerate(recommended_movies):
                    st.write(f'{i + 1}. {movie}')
                    st.write({genre})
            
            #If there are no recommended movies, the code block below will work.
            else:
                st.warning('No recommendation was found.',icon="😢")
        
        #If the user has not entered a movie name, the code block below will work.
        else:
            st.warning('Please enter a movie name.',icon="⚠️")

#It runs the main() function and starts the application.
if __name__ == '__main__':
    main()
