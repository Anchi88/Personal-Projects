import streamlit as st
import requests
import json
from PIL import Image


url = r"https://rickandmortyapi.com/api/character"
resp = requests.get(url)
pages = resp.json()

urlList = []


if "species" not in st.session_state:
    st.session_state["species"] = set()

if "specType" not in st.session_state:
    st.session_state["specType"] = set()

    for i in range(1, pages["info"]["pages"]+1):
        urlList.append(f"https://rickandmortyapi.com/api/character/?page={i}")
        urlVar = urlList[i-1]
        respVar = requests.get(urlVar)
        characters = respVar.json()

        for character in characters["results"]:
            st.session_state["species"].add(character["species"])
            st.session_state["specType"].add(character["type"])

if "viewFullProfile" not in st.session_state:
    st.session_state["viewFullProfile"] = []

st.title("Rick & Morty🛸 Character Search")
st.caption("Character Search using _https://rickandmortyapi.com_ ")

image = Image.open("rickandmorty.jpg")
st.image(image)

tab1,tab2 = st.tabs(["**Search**", "**Full Profile**"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        selSpecies = st.multiselect("Choose Species Type: ", st.session_state["species"])
    with col2:
        selSpecType = st.multiselect("Choose Type:", st.session_state["specType"])
    name = st.text_input("Search by name")
    result = []

    for i in range(1, pages["info"]["pages"] + 1):
        urlList.append(f"https://rickandmortyapi.com/api/character/?page={i}")
        urlVar = urlList[i - 1]
        respVar = requests.get(urlVar)
        characters = respVar.json()

        for character in characters["results"]:
            if not selSpecies and not selSpecType:
                if name.lower() in character["name"].lower() and name != "":
                    result.append(character)

            elif selSpecies and selSpecType:
                if selSpecies[0] == character["species"] and selSpecType[0] == character["type"]:
                    if name.lower() in character["name"].lower():
                        result.append(character)

            elif selSpecies:
                if selSpecies[0] == character["species"] and not selSpecType:
                    if name.lower() in character["name"].lower():
                        result.append(character)
                        break

            elif selSpecType:
                if selSpecType[0] == character["type"] and not selSpecies:
                    if name.lower() in character["name"].lower():
                        result.append(character)

    result = sorted(result, key=lambda val: val["name"])

    colName,colSpec,colSpecType, colEpt = st.columns([2, 1, 1, 1])

    with colName:
        st.write("**Name**")
    with colSpec:
        st.write("**Species**")
    with colSpecType:
        st.write("**Type**")


    for i, character in enumerate(result):
        with st.form(f"Character {i}"):

            colName, colSpec, colSpecType, colButt = st.columns([2, 1, 1, 1])
            with colName:
                st.write(character["name"])
            with colSpec:
                st.write(character["species"])
            with colSpecType:
                st.write(character["type"])
            with colButt:
                if st.form_submit_button("Full profil"):
                    st.session_state["viewFullProfile"].append(character)
                    st.experimental_rerun()


with tab2:
    colName, colStatus, colSpec, colSpecType, colImg, colEmpt = st.columns(6)

    with colName:
        st.write("**Name**")
    with colStatus:
        st.write("**Status**")
    with colSpec:
        st.write("**Species**")
    with colSpecType:
        st.write("**Type**")
    with colImg:
        st.write("**Image**")


    for i, character in enumerate(st.session_state["viewFullProfile"]):
        with st.form(f"Full Profile {i}"):

            colName, colStatus, colSpec, colSpecType, colImg, colButt = st.columns(6)
            with colName:
                st.write(character["name"])
            with colStatus:
                st.write(character["status"])
            with colSpec:
                st.write(character["species"])
            with colSpecType:
                st.write(character["type"])
            with colImg:
                st.image(character["image"])
            with colButt:
                if st.form_submit_button("Remove"):
                    st.session_state["viewFullProfile"].remove(character)
                    st.experimental_rerun()



