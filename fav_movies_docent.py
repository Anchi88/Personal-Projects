import streamlit as st
import json

if "favMovies" not in st.session_state:
    st.session_state["favMovies"] = []

if "genres" not in st.session_state:  # we save in st.session_state, so we don't have to open file more than once
    st.session_state["genres"] = set()
    with open("Movies.json", encoding = "utf-8") as file:
        for movie in json.load(file):
            for genre in movie["genre"].split("|"):
                st.session_state["genres"].add(genre)

st.title("Movie Search 🛸")

tabSearch, tabFav = st.tabs(["🔎Search Movies", f"♥Favorite Movies ({len(st.session_state['favMovies'])})"])

with tabSearch:
    inMovieTitle = st.text_input("Search movie title:")
    selGenre = st.multiselect("Select genre: ", st.session_state["genres"])

    result = list()
    with open ("Movies.json", encoding = "utf-8") as file:
        for movie in json.load(file):
            if not selGenre:
                if inMovieTitle.lower() in movie["title"].lower() and inMovieTitle !="":
                    result.append(movie)

            elif set(selGenre) == set(movie["genre"].split("|")):
                if inMovieTitle.lower() in movie["title"].lower():
                    result.append(movie)

    result = sorted(result, key=lambda val:val["title"])
    colTitle, colGenre, colFav = st.columns([3,2,1])

    with colTitle:
        st.write("**Title**")
    with colGenre:
        st.write("**Genre**")

    for i, movie in enumerate (result):
        with st.form(f"movies_{i}"):

            colTitle, colGenre, colFav = st.columns([3,2,1])

            with colTitle:
                st.write(movie["title"])

            with colGenre:
                st.write(movie["genre"])

            with colFav:
                if movie in st.session_state["favMovies"]:
                    if st.form_submit_button("❤"):
                        st.session_state["favMovies"].remove(movie)
                        st.experimental_rerun()
                else:
                    if st.form_submit_button("🤍"):
                        st.session_state["favMovies"].append(movie)
                        st.experimental_rerun()


with tabFav:
    if len(st.session_state["favMovies"]) == 0:
        st.write("No Favorites yet 😔")
    else:
        colTitle,colGenre,colFav = st.columns([3,2,1])

        with colTitle:
            st.write("**Title")

        with colGenre:
            st.write("**Genre**")

        for i, movie in enumerate(st.session_state["favMovies"]):
            with st.form(f"favMovie_{i}"):

                colTitle,colGenre,colFav = st.columns([3,2,1])

                with colTitle:
                    st.write(movie["title"])

                with colGenre:
                    st.write(movie["genre"])

                with colFav:
                    if movie in st.session_state["favMovies"]:
                        if st.form_submit_button("❤"):
                            st.session_state["favMovies"].remove(movie)
                            st.experimental_rerun()
                    else:
                        if st.form_submit_button("🤍"):
                            st.session_state["favMovies"].append(movie)
                            st.experimental_rerun()
