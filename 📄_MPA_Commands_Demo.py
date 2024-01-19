import streamlit as st
import time
from PIL import Image

corgi = Image.open("kevin.jpg")
corgi2 = Image.open("kevin2.jpg")

st.title("🎮&nbsp; MPA `st.page_link` Demo")
st.subheader("", divider="rainbow")

with st.sidebar:
    # st.subheader("Select a page:")
    # st.page_link("./📄_MPA_Commands_Demo.py", icon="🏠")
    # st.page_link(label="Streamlit Explorer", page="./pages/1_🚧_Streamlit_Issue_Explorer.py", icon="🚧")
    # st.page_link(page="/pages/2_📊_Streamlit_Issues_Summary.py", icon="📊")
    # st.subheader("Other Page Section:")
    # st.page_link(label="Check Open Issues", page="./pages/3_🗃_Open_Issues.py", icon="🗃")
    # st.page_link(page="./pages/4_🧪_Streamlit_E2E_Tester.py", icon="🧪", help="Random help text that is pretty long")
    # st.page_link(label="Google", page="http://google.com", icon="🌎")
    # st.divider()

    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


with st.container():
    st.write(" ")
    st.write(" ")

# st.subheader("Example Nav Bar Orientation:")

# colA, colB, colC = st.columns(3)

# with colA:
#     st.page_link(label="Streamlit Explorer", page="./pages/1_🚧_Streamlit_Issue_Explorer.py", icon="🚧", use_container_width=True)
# with colB:
#     st.page_link(page="/pages/2_📊_Streamlit_Issues_Summary.py", icon="📊", use_container_width=True)
# with colC:
#     st.page_link(label="Check Open Issues", page="./pages/3_🗃_Open_Issues.py", icon="🗃", use_container_width=True)

st.divider()

st.image(corgi, width=250)
st.write("🚗 Kevin the Corgi on a Roadtrip")

st.divider()

# st.subheader("Example List Orientation:")
# st.page_link(label="Google", page="http://google.com", icon="🌎")
# st.page_link(label="Check Open Issues", page="./pages/3_🗃_Open_Issues.py", icon="🗃")
# st.page_link(page="./pages/4_🧪_Streamlit_E2E_Tester.py", icon="🧪", help="Random help text that is pretty long")

# st.divider()

st.image(corgi2, width=250)
st.write("😍 More Necessary Corgi Content")

st.divider()

# st.subheader("Example Grid Orientation:")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.page_link(label="Streamlit Explorer", page="./pages/1_🚧_Streamlit_Issue_Explorer.py", icon="🚧", use_container_width=True)
#     st.page_link(page="/pages/2_📊_Streamlit_Issues_Summary.py", icon="📊", use_container_width=True)
#     st.page_link(label="Check Open Issues", page="./pages/3_🗃_Open_Issues.py", icon="🗃", use_container_width=True)
# with col2:
#     st.page_link(page="./pages/4_🧪_Streamlit_E2E_Tester.py", icon="🧪", help="Random help text that is pretty long")
#     st.page_link(label="Streamlit Website", page="https://streamlit.io", icon="🎈")
#     st.page_link(label="Github - Streamlit", page="https://github.com/streamlit/streamlit", icon="🤖")
# with col3:
#     st.page_link(label="Streamlit Docs", page="https://docs.streamlit.io", icon="🤓")
#     st.page_link(label="Streamlit Forum", page="https://discuss.streamlit.io/", icon="🎙️")
#     st.page_link(label="Google", page="http://google.com", icon="🌎")


