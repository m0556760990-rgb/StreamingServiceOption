#pip install streamlit
#pip install requests

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
import streamlit as st

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


background_image = get_base64_image("Stars.png")


st.markdown(
    f"""
    <style>

    /* ==============================
       MAIN PAGE + FILM BACKGROUND
       ============================== */

    .stApp {{
        background-image:
            url("data:image/png;base64,{background_image}");

        background-size: 100% 100%;
        background-position: center top;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}


    /* ==============================
       CENTER CONTENT AREA
       ============================== */

    .block-container {{
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 4rem;
        padding-left: 3rem;
        padding-right: 3rem;

        background: rgba(255, 255, 255, 0.94);

        border-radius: 18px;

        box-shadow:
            0px 8px 30px rgba(0, 0, 0, 0.08);
    }}


    /* ==============================
       MAIN TITLE
       ============================== */

    h1 {{
        color: #0F2454 !important;
        font-size: 46px !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }}


    /* ==============================
       HEADERS
       ============================== */

    h2 {{
        color: #102552 !important;
        font-weight: 800 !important;
    }}

    h3 {{
        color: #17376E !important;
        font-weight: 700 !important;
    }}


    /* ==============================
       NORMAL TEXT
       ============================== */

    p {{
        color: #52627A !important;
        font-size: 17px !important;
    }}


    /* ==============================
       SELECTBOX LABELS
       ============================== */

    div[data-testid="stSelectbox"] label {{
        color: #102552 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }}


    /* ==============================
       SELECTBOX
       ============================== */

    div[data-baseweb="select"] > div {{
        background-color: #abaff5 !important;

        border:
            1px solid #CBD5E1 !important;

        border-radius:
            10px !important;

        min-height:
            48px;

        box-shadow:
            0 2px 5px rgba(0,0,0,0.04);
    }}


    /* Selectbox text */

    div[data-baseweb="select"] span {{
        color: #1F2937 !important;
        font-size: 16px !important;
    }}


    /* ==============================
       BUTTONS
       ============================== */

    div.stButton > button {{
        width: 100%;

        height: 50px;

        border-radius: 10px;

        border: none;

        background:
            linear-gradient(
                90deg,
                #1677F0,
                #246BDF
            );

        color: white;

        font-size: 17px;

        font-weight: 700;

        box-shadow:
            0 4px 12px rgba(30, 100, 220, 0.25);

        transition:
            0.2s;
    }}


    /* Button hover */

    div.stButton > button:hover {{

        transform:
            translateY(-1px);

        box-shadow:
            0 6px 16px rgba(30, 100, 220, 0.35);

        color:
            white;

    }}


    /* ==============================
       TABS
       ============================== */

    div[data-baseweb="tab-list"] {{
        gap: 8px;
    }}


    div[data-baseweb="tab-list"] button {{

        background-color:
            #F7F9FC;

        border:
            1px solid #DCE3ED;

        border-radius:
            10px;

        padding:
            10px 18px;

        font-weight:
            700 !important;

    }}


    /* Selected tab */

    div[data-baseweb="tab-list"]
    button[aria-selected="true"] {{

        background:
            #1677F0 !important;

        color:
            white !important;

    }}


    /* ==============================
       DATAFRAME
       ============================== */

    div[data-testid="stDataFrame"] {{

        border-radius:
            12px;

        overflow:
            hidden;

        border:
            1px solid #E1E7EF;

    }}


    /* ==============================
       CONTAINERS / CARDS
       ============================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {{

        background:
            rgba(255,255,255,0.96);

        border:
            1px solid #E1E7EF !important;

        border-radius:
            14px !important;

        box-shadow:
            0px 4px 15px rgba(0,0,0,0.05);

    }}


    /* ==============================
       ALERT / ERROR BOXES
       ============================== */

    div[data-testid="stAlert"] {{

        border-radius:
            10px;

    }}


    </style>
    """,

    unsafe_allow_html=True
)


#*Function to print all the genres from the API*
def ShowGenres(API_KEY):
    headers = {"X-API-Key": API_KEY}
    urlgenres = "https://api.watchmode.com/v1/genres"
    response = requests.get(urlgenres, headers=headers)
    response.raise_for_status()
    genres = response.json()
    for genre in genres:
        print(genre["id"], "-", genre["name"])

#*Function to get the services that have the title - then we use the Source_id and Region from what we get to tell where the title is available*
def GetTitleAvailabel(title_id):
    url = f"https://api.watchmode.com/v1/title/{title_id}/sources"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    title_sources = response.json()
    return(title_sources)

country_codes = {
    "USA": "US",
    "Spain": "ES",
    "Israel": "IL"
}

MediaTypes = {
    "Movie": "movie",
    "TV Show": "tv_series",
}

#Genre ID Converter
genres = pd.read_csv("generes.csv")
genre_dict = dict(zip(genres["id"], genres["name"]))

def show_titles(titles,MediaName):
    @st.dialog(f"Available {MediaName}", width="large")
    def dialog():
        st.dataframe(titles, use_container_width=True)
    dialog()

@st.dialog("Streaming Content Comparison", width="large")
def show_statistics_plot(fig):
    st.plotly_chart(fig, use_container_width=True)
    
API_KEY = st.secrets["api_key"]
urltitles = "https://api.watchmode.com/v1/list-titles"

License = "Proprietary"
headers = {"X-API-Key": API_KEY}



#sources = GetTitleAvailabel(3213685)

# for source in sources:
   # print(source["name"], "-", source["region"])



##Website Section#

st.set_page_config(page_title="Streamer Guide",page_icon="📺",layout="centered")
st.title("Streaming Watch Guide", wrap=True)

#name = st.text_input('Enter your name', '')
#if name:
#    st.write(f'Hello {name}, Looking for something to watch?!')
choice = st.selectbox(label="Choose your country of viewing:",options=["Israel", "USA", "Spain"],index=0,placeholder="Select an option...")
sources_df = pd.read_csv("Sources.csv")

country_codes = {
    "Israel": "IL",
    "USA": "US",
    "Spain": "ES"
}

country_code = country_codes[choice]

filtered_sources = sources_df[
    sources_df["regions"].str.contains(country_code, na=False)
]

service = st.selectbox(
    label="Choose your streaming service:",
    options=filtered_sources["name"]
)

selected_source = filtered_sources[
    filtered_sources["name"] == service
]

source_id = int(selected_source["id"].iloc[0])

genres_df = pd.read_csv("generes.csv")

genre = st.selectbox(
    "Choose genre:",
    ["All"] + genres_df["name"].tolist()
)

search_params = {
    "types": "movie,tv_series",
    "regions": country_code,
    "source_ids": source_id,
    "page": 1,
    "limit": 20
}

if genre != "All":
    selected_genre = genres_df[
        genres_df["name"] == genre
    ]

    genre_id = int(selected_genre["id"].iloc[0])

    search_params["genres"] = genre_id


if "titles_df" not in st.session_state:
    st.session_state["titles_df"] = None
if "search_info" not in st.session_state:
    st.session_state["search_info"] = None


if st.button("Show titles"):
    response = requests.get(
        urltitles,
        headers=headers,
        params=search_params
    )

    response.raise_for_status()
    data = response.json()

    st.session_state["titles_df"] = pd.DataFrame(data["titles"])
    st.session_state["search_info"] = {
        "country": choice,
        "service": service,
        "genre": genre
    }


if (
    st.session_state["titles_df"] is not None
    and st.session_state["search_info"] is not None
):

    titles_df = st.session_state["titles_df"]

    content_type = st.selectbox(
        "Choose content type:",
        ["All", "Movies", "TV Series"]
    )

    if content_type == "Movies":
        titles_df = titles_df[titles_df["type"] == "movie"]

    elif content_type == "TV Series":
        titles_df = titles_df[titles_df["type"] == "tv_series"]

    search_info = st.session_state["search_info"]
    if service != search_info["service"] or choice != search_info["country"] or genre != search_info["genre"]:
        st.info("Selections changed. Click 'Show titles' to update the results.")

    st.subheader(
        f"Available on {search_info['service']} in {search_info['country']}"
    )

    for index, row in titles_df.iterrows():
        title_type = "Movie" if row["type"] == "movie" else "TV Series"
        st.write(f"{row['title']} ({row['year']}) - {title_type}")



#2
st.divider()

st.header("Find Episodes")

episode_country = st.selectbox(
    "Choose a country for the series:",
    ["Israel", "USA", "Spain"],
    key="episode_country"
)
series_name = st.text_input(
    "Enter the series name:",
    key="series_name"
)
if "episodes_data" not in st.session_state:
    st.session_state["episodes_data"] = None

if "episode_search_info" not in st.session_state:
    st.session_state["episode_search_info"] = None

if st.button("Show episodes"):

    same_search = (
        st.session_state["episode_search_info"] is not None
        and st.session_state["episode_search_info"]["country"] == episode_country
        and st.session_state["episode_search_info"]["series"] == series_name
    )

    if same_search:
        st.info("These results are already saved.")

    elif series_name:
        series_params = {
            "search_field": "name",
            "search_value": series_name,
            "types": "tv_series"
        }

        response = requests.get(
            urltitles,
            headers=headers,
            params=series_params
        )

        response.raise_for_status()
        series_data = response.json()

        if len(series_data["titles"]) > 0:
            series_id = series_data["titles"][0]["id"]
            episode_country_code = country_codes[episode_country]

            episodes_url = f"https://api.watchmode.com/v1/title/{series_id}/episodes"

            episodes_response = requests.get(
                episodes_url,
                headers=headers,
                params={"regions": episode_country_code}
            )

            episodes_response.raise_for_status()
            episodes_data = episodes_response.json()

            st.session_state["episodes_data"] = episodes_data

            st.session_state["episode_search_info"] = {
                "country": episode_country,
                "series": series_name
            }

        else:
            st.write("Series not found")
if st.session_state["episodes_data"] is not None:
    episodes_data = st.session_state["episodes_data"]
    episode_search_info = st.session_state["episode_search_info"]
    if (
        episode_country != episode_search_info["country"]
        or series_name != episode_search_info["series"]
    ):
        st.info("Selections changed. Click 'Show episodes' to update the results.")

    st.subheader(
        f"Episodes of {episode_search_info['series']} in {episode_search_info['country']}"
    )

    if len(episodes_data) > 0:
        for episode in episodes_data:
            st.write(
                f"Season {episode['season_number']}, "
                f"Episode {episode['episode_number']} - "
                f"{episode['name']}"
            )
    else:
        st.write("No episodes found")
#3
#3
st.divider()

st.header("Find Titles by Year and Genre")

selected_year = st.selectbox(
    "Choose a year:",
    list(range(2026, 1999, -1))
)

selected_genre = st.selectbox(
    "Choose a genre:",
    genres_df["name"].tolist(),
    key="year_genre"
)
selected_genre_row = genres_df[
    genres_df["name"] == selected_genre
]

selected_genre_id = int(selected_genre_row["id"].iloc[0])

year_genre_params = {
    "types": "movie,tv_series",
    "genres": selected_genre_id,
    "release_date_start": selected_year * 10000 + 101,
"release_date_end": selected_year * 10000 + 1231,
    "page": 1,
    "limit": 20
}
if "year_genre_titles" not in st.session_state:
    st.session_state["year_genre_titles"] = None

if "year_genre_search_info" not in st.session_state:
    st.session_state["year_genre_search_info"] = None
if st.button("Show titles by year and genre"):

    response = requests.get(
        urltitles,
        headers=headers,
        params=year_genre_params
    )

    response.raise_for_status()
    year_genre_data = response.json()

    st.session_state["year_genre_titles"] = pd.DataFrame(
        year_genre_data["titles"]
    )

    st.session_state["year_genre_search_info"] = {
        "year": selected_year,
        "genre": selected_genre
    }
if st.session_state["year_genre_titles"] is not None:

    year_genre_titles = st.session_state["year_genre_titles"]
    year_genre_search_info = st.session_state["year_genre_search_info"]

    if (
        selected_year != year_genre_search_info["year"]
        or selected_genre != year_genre_search_info["genre"]
    ):
        st.info(
            "Selections changed. Click 'Show titles by year and genre' to update the results."
        )

    st.subheader(
        f"{year_genre_search_info['genre']} titles from {year_genre_search_info['year']}"
    )

    if len(year_genre_titles) > 0:
        for index, row in year_genre_titles.iterrows():
            title_type = "Movie" if row["type"] == "movie" else "TV Series"

            st.write(
                f"{row['title']} ({row['year']}) - {title_type}"
            )
    else:
        st.write("No titles found")

