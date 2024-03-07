import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8f3685ebb6724f24e1c1eedfacc94814&language=en-US'.format(movie_id))
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_list=pickle.load(open('movies.pkl','rb'))
mov_list=movies_list['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

option = st.selectbox(
    'Type or Select a movie and let me recommend you some similar movies :)',
    mov_list)

if st.button('Recommend'):
    namess,posters=recommend(option)
    import streamlit as st

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
       st.text(namess[0])
       st.image(posters[0])

    with col2:
       st.text(namess[1])
       st.image(posters[1])

    with col3:
       st.text(namess[2])
       st.image(posters[2])

    with col4:
       st.text(namess[3])
       st.image(posters[3])

    with col5:
       st.text(namess[4])
       st.image(posters[4])


