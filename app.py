import streamlit as st
from datetime import date
import altair as alt
from vega_datasets import data

st.set_page_config(initial_sidebar_state="collapsed")

c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    st.button('V1 - container', use_container_width=True)
with c2:
    st.button('V2 - container', use_container_width=True)
with c3:
    st.button('V3 - container+help', use_container_width=True, help='example')

st.button("Normal Button")
st.button("Normal Button with help", help='testing tooltip')
st.button("Normal Button with container & help", use_container_width=True, help='testing tooltip')

st.download_button("Normal Download Button", data='data')
st.download_button("Download Button with help", help='download button tooltip', data='data')
st.download_button("Download Button with container & help", help='download button tooltip', use_container_width=True, data='data')

with st.form(key='form'):
    st.form_submit_button("Form Submit Button with help", help='form submit tooltip')
with st.form(key='form2'):
    st.form_submit_button("Form Submit Button with container & help", use_container_width=True, help='form submit tooltip')



# st.subheader("barley example")
# source = data.barley()
# st.write(source)
# st.write(
#     alt.Chart(source)
#     .mark_bar()
#     .encode(x="year:O", y="sum(yield):Q", color="year:N", column="site:N")
# )

# dates = st.slider('date range',
#                   min_value=date(2019, 8, 1), max_value=date(2021, 6, 4),
#                   value=(date(2021, 5, 21), date(2021, 6, 4)))

# user_input = st.text_input("Enter Movie Name")
# st.write(user_input)


# st.subheader("Radio Examples:")
# st.radio("Normal Radio Group Title:", ('Regular Options:', 'Corgi', 'Husky', 'Golden Retriever'))
# # st.radio("Normal Radio Group Title:", ('Regular Options:', 'Corgi', 'Husky', 'Golden Retriever'),label_visibility="collapsed")
# # st.radio("Normal Radio Group Title:", ('Regular Options:', 'Corgi', 'Husky', 'Golden Retriever'), horizontal=True)

# st.radio("Radio Group Title with simple markdown: **bold** *italics* ~strikethrough~ Emoji: ✅ Shortcode: :blush:", ('Fancy Markdown:', 'link = [link](www.example.com)', 'code = `code`', 'colored text = :red[red!] :blue[blue!] :green[green!] :violet[violet!] :orange[orange!]'))
# st.radio("Radio Group Title with fancy markdown: link = [link](www.example.com) code = `code` :red[red!] :blue[blue!] :green[green!] :violet[violet!] :orange[orange!]", ('Simple Markdown:', 'bold: **Corgi**', 'italics: *Husky*', 'emoji shortcode: Golden Retriever :blush:', 'strikethrough: ~Snake~'))

# st.subheader("Checkbox Examples:")
# st.checkbox("Normal Checkbox Label")
# st.checkbox("Checkbox Label with simple markdown: **bold** *italics* ~strikethrough~ Emoji: ✅ Shortcode: :blush:")
# st.checkbox("Checkbox Label with fancy markdown: link = [link](www.example.com) code = `code` :red[red!] :blue[blue!] :green[green!] :violet[violet!] :orange[orange!]")
