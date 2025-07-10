import streamlit as st
import pickle
import pandas as pd

movie_dict=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_dict)


def recommend(movie):
    movie_index= movies[movies['title']== movie].index[0]
    distance= similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

st.title('Movie Recommender System')

selected_movie_name=st.selectbox('What movie do you want recommendation on?',movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)