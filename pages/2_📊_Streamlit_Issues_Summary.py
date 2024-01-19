import streamlit as st
import json
import urllib.request
from urllib.parse import quote
import altair as alt
import pandas as pd

# st.set_page_config(page_title="GitHub Issues Summary", page_icon="📊")

with st.sidebar:
    # st.subheader("Select a page:")
    # st.page_link("./📄_MPA_Commands_Demo.py", icon="🏠", use_container_width=True)
    # st.page_link(label="Streamlit Explorer", page="./pages/1_🚧_Streamlit_Issue_Explorer.py", icon="🚧")
    # st.page_link(page="/pages/2_📊_Streamlit_Issues_Summary.py", icon="📊")
    # st.page_link(label="Check Open Issues", page="./pages/3_🗃_Open_Issues.py", icon="🗃")
    # st.page_link(page="./pages/4_🧪_Streamlit_E2E_Tester.py", icon="🧪", help="Random help text that is pretty long")
    # st.write(":zap: Random text for spacing reference")
    # st.divider()

    st.write("Repeat widgets")
    st.radio("Radio", ["A", "B", "C"])
    st.slider("Slider", 0, 10, 5)
    st.multiselect("Multiselect", ["A", "B", "C"])
    st.checkbox("Checkbox", value=True)

st.title("GitHub Issues Summary")

# Paginate through all open issues in the streamlit/streamlit repo
# and return them all as a list of dicts.
@st.cache_data(ttl=60 * 60 * 6)  # cache for 6 hours
def get_all_github_issues():
    issues = []
    page = 1
    while True:
        try:
            with urllib.request.urlopen(
                f"https://api.github.com/repos/streamlit/streamlit/issues?state=open&per_page=100&page={page}"
            ) as response:
                if response:
                    data = json.loads(response.read())
                    if not data:
                        break
                    issues.extend(data)
                    page += 1
        except Exception as ex:
            print(ex, flush=True)
            break
    return issues

# Ignore Pull Requests
all_issues = [issue for issue in get_all_github_issues() if 'pull_request' not in issue]
all_labels = set()
all_uncategorized_labels = []
for issue in all_issues:
    for label in issue['labels']:
        all_labels.add(label['name'])

all_categories = {}

for label in all_labels:
    if ":" in label:
        category, name = label.split(":")
        if category not in all_categories:
            all_categories[category] = []
        all_categories[category].append(name)
    else:
        all_uncategorized_labels.append(label)

params = st.experimental_get_query_params()

search_terms = {}
has_search_terms = False
for category in all_categories:
    if category in params and category not in st.session_state:
        st.session_state[category] = params[category]
    search_terms[category] = st.multiselect(category, all_categories[category], key=category)
    has_search_terms = has_search_terms or bool(search_terms[category])

if all_uncategorized_labels:
    search_terms['uncategorized'] = st.multiselect('uncategorized', all_uncategorized_labels)
    has_search_terms = has_search_terms or bool(search_terms[category])

st.experimental_set_query_params(**{key: value for key, value in search_terms.items() if value})

issue_search = []
for issue in all_issues:
    should_add = True
    for category, terms in search_terms.items():
        if terms:
            formatted_labels = [f"{category}:{term}" if category != "uncategorized" else term for term in terms]
            has_label = False
            for label in issue['labels']:
                if label['name'] in formatted_labels:
                    has_label = True
                    break
            should_add = should_add and has_label
    
    if should_add:
        issue_search.append(issue)

link_qp = [quote("is:open"), quote("is:issue")]
for category, terms in search_terms.items():
    if terms:
        if category == "uncategorized":
            formatted_labels = f'label:"{",".join(terms)}"'
        else:
            formatted_labels = f'label:"{",".join(f"{category}:{term}" for term in terms)}"'

        link_qp.append(quote(formatted_labels))
link_qs = "+".join(link_qp)
link = f"https://github.com/streamlit/streamlit/issues?q={link_qs}"

st.write(f"There are currently **{len(issue_search)} issues found**. [View on GitHub ↗️]({link})")

issue_categories = {}

for issue in issue_search:
    for label in issue['labels']:
        if ":" in label['name']:
            category, name = label['name'].split(":")
        else:
            category = "uncategorized"
            name = label['name']

        if not search_terms[category]:
            issue_categories[category] = issue_categories.get(category, {})
            issue_categories[category][name] = issue_categories[category].get(name, 0) + 1
        

for category, counts in issue_categories.items():
    issue_count = sum(counts.values())
    if issue_count < len(issue_search):
        counts['(not specified)'] = len(issue_search) - issue_count
    cat_df = pd.DataFrame(list(counts.items()), columns=['name', 'count'])
    x = alt.X("count")
    altair_graph = (
        alt.Chart(cat_df, title=category)
        .mark_bar()
        .encode(
            x=x, y=alt.Y("name", sort="-x"), tooltip=["name", "count"]
        )
    )
    st.altair_chart(altair_graph, use_container_width=True)

REACTION_EMOJI = {
    "+1": "👍",
    "-1": "👎",
    "confused": "😕",
    "eyes": "👀",
    "heart": "❤️",
    "hooray": "🎉",
    "laugh": "😄",
    "rocket": "🚀",
}

def reactions_to_str(reactions):
    return " ".join([f"{reactions[name]} {emoji}" for name, emoji in REACTION_EMOJI.items() if reactions[name] > 0])

if st.checkbox("Show all issues"):
    df = pd.DataFrame.from_dict(issue_search)
    df['labels'] = df['labels'].map(lambda x: ",".join([label['name'] for label in x]))
    df['reactions'] = df['reactions'].map(reactions_to_str)
    st.write(df[['title', 'html_url', 'labels', 'reactions', 'created_at', 'updated_at']])
