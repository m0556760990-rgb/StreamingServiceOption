#pip install streamlit
#pip install requests

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
import streamlit as st
df = pd.read_csv("israel_animation.csv")
print(df.head())
print(df.columns)
titles_df = pd.read_csv("USTitles.csv")
print(len(titles_df))

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

API_KEY = st.secrets["api_key"]
urltitles = "https://api.watchmode.com/v1/list-titles"

License = "Proprietary"
headers = {"X-API-Key": API_KEY}

#ShowGenres(API_KEY)

##getting titles table
params = {"types": "movie,tv_series","regions": "US","genres":"33,40,2,1,11","page": 1,"limit": 250}
#df = pd.read_csv("israel_animation.csv")
#
# response = requests.get(urltitles,headers=headers,params=params)
# response.raise_for_status()
# data = response.json()
# pd.set_option("display.max_columns", None)
# df = pd.DataFrame(data["titles"])



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

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
