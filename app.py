import pandas as pd
import streamlit as st
import pickle
import requests
st.title('Movie Recommender System')
movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_posters(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6ae70443ac46a1f9fa2f87ef818d81d2&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    #recommende_movie_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #recommende_movie_posters.append(fetch_posters(movie_id))
    return recommended_movies #,recommende_movie_posters

movies_list = movies_list['title'].values
selected_movie = st.selectbox(
    'Enter the name of the Movie',
    movies_list
)

if st.button('Recommend'):
    names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
        #st.image(posters[0])


    with col2:
        st.header(names[1])
        #st.image(posters[1])

    with col3:
        st.header(names[2])
        #st.image(posters[2])


    with col4:
        st.header(names[3])
        #st.image(posters[3])


    with col5:
        st.header(names[4])
        #st.image(posters[4])

