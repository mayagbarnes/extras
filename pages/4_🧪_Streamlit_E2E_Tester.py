import streamlit as st
import time
import re
from execbox import execbox
from e2e_loader import select_script, get_script
from urllib.parse import urlparse


with st.sidebar:
    # st.subheader("Select a page:")
    # st.page_link("./📄_MPA_Commands_Demo.py", icon="🏠")
    # st.page_link(label="Streamlit Explorer", page="./pages/1_🚧_Streamlit_Issue_Explorer.py", icon="🚧")
    # st.page_link(page="/pages/2_📊_Streamlit_Issues_Summary.py", icon="📊")
    # st.page_link(label="Check Open Issues", page="./pages/3_🗃_Open_Issues.py", icon="🗃")
    # st.page_link(page="./pages/4_🧪_Streamlit_E2E_Tester.py", icon="🧪", help="Random help text that is pretty long")
    # st.write(":zap: Random text for spacing reference")
    st.subheader("Other sidebar content:")
    with st.spinner("Regular `st.spinner` Spinner..."):
        time.sleep(3)

with open("requirements.txt") as requirements:
    s3_url = requirements.read().split("\n")[-1]

col1, padding, col2 = st.columns([3, 0.1, 1])


def get_first_match(regex, s):
    match = re.search(regex, s)
    return match.group(1) if match else None


def get_branch_info():
    path = urlparse(s3_url).path
    path_parts = list(filter(None, path.split("/")))
    core_preview_branch = "/".join(path_parts[:-1])

    branch = get_first_match("(.*)-preview", core_preview_branch)
    # There's no nightly branch, so default to develop
    branch = "develop" if branch == "nightly" else branch
    pr = get_first_match("pr-(\\d+)", core_preview_branch)

    return branch, pr


branch, pr_number = get_branch_info()
if pr_number is not None:
    col2.write(
        f"🔭 [View PR on Github](https://github.com/streamlit/streamlit/pull/{pr_number})"
    )
col2.write(f"🎡 [Download wheel]({s3_url})")

with col1:
    selected_script = select_script(branch, pr_number)

# fallback if things fail
script = "import streamlit as st"

if selected_script:
    if 'download_url' in selected_script:
        script = get_script(selected_script["download_url"])
    else:
        with open(selected_script['path'], 'r', encoding='utf-8') as f:
            script = f.read()

st.header("Edit my source 👇")
execbox(
    script,
    autorun=True,
    line_numbers=True,
    height=300,
)