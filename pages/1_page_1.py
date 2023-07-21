import streamlit as st
import pandas as pd
import time 
import random 

st.sidebar.subheader("Radio Examples:")
st.sidebar.radio("Normal Radio Group Title:", ('Regular Options:', 'Corgi', 'Husky', 'Golden Retriever'))
# st.sidebar.radio("Normal Radio Group Title:", ('Regular Options:', 'Corgi', 'Husky', 'Golden Retriever'),label_visibility="collapsed")
# st.sidebar.radio("Normal Radio Group Title:", ('Regular Options:', 'Corgi', 'Husky', 'Golden Retriever'), horizontal=True)

st.sidebar.radio("Radio Group Title with simple markdown: **bold** *italics* ~strikethrough~ Emoji: ✅ Shortcode: :blush:", ('Fancy Markdown:', 'link = [link](www.example.com)', 'code = `code`', 'colored text = :red[red!] :blue[blue!] :green[green!] :violet[violet!] :orange[orange!]'))
st.sidebar.radio("Radio Group Title with fancy markdown: link = [link](www.example.com) code = `code` :red[red!] :blue[blue!] :green[green!] :violet[violet!] :orange[orange!]", ('Simple Markdown:', 'bold: **Corgi**', 'italics: *Husky*', 'emoji shortcode: Golden Retriever :blush:', 'strikethrough: ~Snake~'))

st.sidebar.subheader("Checkbox Examples:")
st.sidebar.checkbox("Normal Checkbox Label")
st.sidebar.checkbox("Checkbox Label with simple markdown: **bold** *italics* ~strikethrough~ Emoji: ✅ Shortcode: :blush:")
st.sidebar.checkbox("Checkbox Label with fancy markdown: link = [link](www.example.com) code = `code` :red[red!] :blue[blue!] :green[green!] :violet[violet!] :orange[orange!]")

st.sidebar.subheader("⤵️ **Sidebar Toasts:**")
st.sidebar.caption("Toasts triggered from the sidebar")

def sidebar_callback():
    toast_index = [0, 1, 2, 3]
    # toast_types = [None, 'success', 'warning', 'error']
    toast_messages = ["This is a toast triggered from the sidebar", "Short: This is a toast message!", "Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit"]
    for i in toast_index:
        # style = toast_types[i]
        text = random.choice(toast_messages)
        st.toast(f"{i+1} of 4: {text}", icon='⬅️')

st.sidebar.write("Toast triggered using `st.toast` in a callback from sidebar:")
st.sidebar.button("✔️ Sidebar Toast", type="secondary", on_click=sidebar_callback)

def with_sidebar_callback():
    toast_index = [0, 1, 2, 3]
    # toast_types = [None, 'success', 'warning', 'error']
    toast_messages = ["This is a toast triggered directly **ON** st.sidebar", "Short: This is a toast message!", "Long: Random toast message that is a really really really really really really really long message, going way past the 3 line limit"]
    for i in toast_index:
        # style = toast_types[i]
        text = random.choice(toast_messages)
        st.toast(f"{i+1} of 4: {text}", icon='⬅️')

with st.sidebar:
    st.write("Toast triggered under `with st.sidebar:` notation:")
    st.button("🙃 More sidebar toasts", on_click=with_sidebar_callback)


