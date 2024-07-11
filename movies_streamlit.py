import streamlit as st 
import pickle 
import requests 
import pandas as pd
from urllib.parse import urlencode


# Load the movie data and similarity matrix
movies = pickle.load(open("new_Data.pkl", 'rb'))
similar = pickle.load(open("simi.pkl", 'rb'))

# Streamlit app title
st.title('Movie Recommendation System')

# Selectbox to choose a movie
select = st.selectbox("Select a movie", movies['Movie_Title'].values)

def fetch_poster(movie):
    """Fetch the poster of a movie using the OMDB API"""
    try:
        res = requests.get(f"http://www.omdbapi.com/?apikey=9bf19187&t={movie}")
        data = res.json()
        return data.get("Poster", "https://via.placeholder.com/150") 
    except Exception as e:
        st.error("Error fetching poster: " + str(e))
        return "https://via.placeholder.com/150"  

def recommend(movie_name):
    """Recommend movies based on the similarity matrix"""
    idx = movies[movies['Movie_Title'] == movie_name].index[0]
    dis = sorted(list(enumerate(similar[idx])), key=lambda x: x[1], reverse=True)
    movie_list = []
    poster_list = []
    for i in dis[1:6]:
        movie_title = movies.iloc[i[0]].Movie_Title
        movie_list.append(movie_title)
        poster_list.append(fetch_poster(movie_title))
    return movie_list, poster_list

# Get the recommended movies and their posters
movie_list, poster_path = recommend(select)



# Show the recommended movies when the button is clicked
if st.button('Show Recommendations'):
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_list[0])
        params = {"movie_name": movie_list[0]}

        local_html_url = "http://localhost:8000/formovie.html"
        url_with_params = f"{local_html_url}?{urlencode(params)}"
        st.markdown(f"""
        <a href="{url_with_params}" target="_blank">
            <img src="{poster_path[0]}" alt="poster" style="height:200px;">
        </a>
    """, unsafe_allow_html=True)
    with col2:
        st.text(movie_list[1])
        params = {"movie_name": movie_list[0]}

        local_html_url = "http://localhost:8000/formovie.html"
        url_with_params = f"{local_html_url}?{urlencode(params)}"
        st.markdown(f"""
        <a href="{url_with_params}" target="_blank">
            <img src="{poster_path[1]}" alt="poster" style="height:200px;">
        </a>
    """, unsafe_allow_html=True)
    with col3:
        st.text(movie_list[2])
        params = {"movie_name": movie_list[0]}

        local_html_url = "http://localhost:8000/formovie.html"
        url_with_params = f"{local_html_url}?{urlencode(params)}"
        st.markdown(f"""
        <a href="{url_with_params}" target="_blank">
            <img src="{poster_path[2]}" alt="poster" style="height:200px;">
        </a>
    """, unsafe_allow_html=True)

    with col4:
        st.text(movie_list[3])
        params = {"movie_name": movie_list[0]}

        local_html_url = "http://localhost:8000/formovie.html"
        url_with_params = f"{local_html_url}?{urlencode(params)}"
        st.markdown(f"""
        <a href="{url_with_params}" target="_blank">
            <img src="{poster_path[3]}" alt="poster" style="height:200px;">
        </a>
    """, unsafe_allow_html=True)
    with col5:
        st.text(movie_list[4])
        params = {"movie_name": movie_list[0]}

        local_html_url = "http://localhost:8000/formovie.html"
        url_with_params = f"{local_html_url}?{urlencode(params)}"
        st.markdown(f"""
        <a href="{url_with_params}" target="_blank">
            <img src="{poster_path[4]}" alt="poster" style="height:200px;">
        </a>
    """, unsafe_allow_html=True)