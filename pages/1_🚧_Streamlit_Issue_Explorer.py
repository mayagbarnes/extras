import json
import os
import pathlib
import platform
import re
import urllib.request
from typing import Union

import pokebase as pb
import random
import pandas as pd
import numpy as np
from PIL import Image
import time

import streamlit as st
import streamlit.components.v1 as components


st.title("🚧 Streamlit Issues")

st.caption(
    f"""
A collection of Streamlit apps to replicate issues and bugs. Add your issue script [here](https://github.com/streamlit/st-issues).

Running with Python {platform.python_version()} and Streamlit {st.__version__}.
"""
)
DEFAULT_SELECTION = ""
DEFAULT_SCRIPT_NAME = "app.py"
DEFAULT_ISSUES_FOLDER = "issues"

st.selectbox(
    "Select Issue",
    [1,2,3,4,5,6,7,8,9,10],
    index=8,
)


with st.sidebar:
    # st.subheader("Select a page:")
    # st.page_link("./📄_MPA_Commands_Demo.py", icon="🏠", use_container_width=True)
    # st.page_link(label="Streamlit Explorer", page="./pages/1_🚧_Streamlit_Issue_Explorer.py", icon="🚧")
    # st.page_link(page="/pages/2_📊_Streamlit_Issues_Summary.py", icon="📊")
    # st.page_link(label="Check Open Issues", page="./pages/3_🗃_Open_Issues.py", icon="🗃")
    # st.page_link(page="./pages/4_🧪_Streamlit_E2E_Tester.py", icon="🧪", help="Random help text that is pretty long")
    st.write(":zap: Random text for spacing reference")
    st.divider()

    def clear_cache():
        st.cache_data.clear()

    st.header("⚠️ Vital Sidebar Content")
    # cache_load = st.slider("**Choose Cache Function Load Time:**", 0, 30, 1)
    st.button("Clear :red[**ALL**] Caches", on_click=clear_cache)


    @st.cache_resource
    def fetch_pokemon():
        # time.sleep(cache_load)
        random_id = random.randint(1, 251)
        pokemon = pb.pokemon(random_id)
        pokemon_name = pokemon.name
        sprite = pb.SpriteResource('pokemon', random_id, official_artwork=True)
        return pokemon_name.capitalize(), sprite.url
    # st.divider()
    st.write("**Cached Pokemon** :fire:")
    pokemon_name, sprite = fetch_pokemon()
    st.image(sprite, width=150)
    st.caption(f"**{pokemon_name}**")

    @st.cache_data
    def render_df():
        df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
        # time.sleep(cache_load)
        return df

    @st.cache_data
    def render_chart():
        df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
        # time.sleep(cache_load)
        return df