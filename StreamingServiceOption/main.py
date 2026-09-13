#pip install streamlit
#pip install requests

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
import base64
import streamlit as st
import random


def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


background_image = get_base64_image("Stars.png")
st.markdown(
    f"""
    <style>

    /* =====================================================
       PAGE BACKGROUND - STAR IMAGE
       ===================================================== */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.20),
                rgba(0, 0, 0, 0.20)
            ),
            url("data:image/png;base64,{background_image}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}


    /* =====================================================
       MAIN CENTER PANEL
       ===================================================== */

    .block-container {{
        max-width: 1200px;

        padding-top: 2rem;
        padding-bottom: 4rem;
        padding-left: 3rem;
        padding-right: 3rem;

        background: rgba(9, 5, 20, 0.94);

        border: 1px solid rgba(139, 92, 246, 0.35);

        border-radius: 22px;

        box-shadow:
            0 15px 50px rgba(0, 0, 0, 0.70),
            0 0 35px rgba(109, 40, 217, 0.12);
    }}


    /* =====================================================
       MAIN PAGE TITLES
       IMPORTANT: scoped to .block-container
       ===================================================== */

    .block-container h1 {{
        color: #FFFFFF !important;
        font-size: 46px !important;
        font-weight: 800 !important;
        letter-spacing: -1px;

        text-shadow:
            0 0 15px rgba(139, 92, 246, 0.35);
    }}

    .block-container h2 {{
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }}

    .block-container h3 {{
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }}


    /* =====================================================
       MAIN PAGE NORMAL TEXT
       IMPORTANT: scoped to .block-container
       ===================================================== */

    .block-container p {{
        color: #E8E7EF !important;
        font-size: 17px !important;
    }}

    .block-container div[data-testid="stMarkdownContainer"] {{
        color: #E8E7EF !important;
    }}

    .block-container div[data-testid="stMarkdownContainer"] p {{
        color: #E8E7EF !important;
    }}


    /* =====================================================
       SELECTBOX LABELS
       ===================================================== */

    .block-container div[data-testid="stSelectbox"] label {{
        color: #FFFFFF !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }}

    .block-container div[data-testid="stSelectbox"] label p {{
        color: #FFFFFF !important;
    }}


    /* =====================================================
       SELECTBOX
       ===================================================== */

    div[data-baseweb="select"] > div {{
        background: rgba(27, 18, 47, 0.98) !important;

        border:
            1px solid rgba(139, 92, 246, 0.55) !important;

        border-radius: 10px !important;

        min-height: 50px;

        color: #FFFFFF !important;

        box-shadow:
            0 3px 10px rgba(0, 0, 0, 0.30);
    }}

    div[data-baseweb="select"] span {{
        color: #FFFFFF !important;
        font-size: 16px !important;
    }}

    div[data-baseweb="select"] div {{
        color: #D1D5DB !important;
    }}

    div[data-baseweb="select"] svg {{
        fill: #FFFFFF !important;
        color: #FFFFFF !important;
    }}


    /* =====================================================
       SELECTBOX DROPDOWN
       ===================================================== */

    div[data-baseweb="popover"] {{
        background-color: #160D28 !important;
    }}

    ul[data-baseweb="menu"] {{
        background-color: #160D28 !important;
    }}

    li[role="option"] {{
        background-color: #160D28 !important;
        color: #FFFFFF !important;
    }}

    li[role="option"]:hover {{
        background-color: #4C1D95 !important;
        color: #FFFFFF !important;
    }}


    /* =====================================================
       BUTTONS
       ===================================================== */

    div.stButton > button {{
        width: 100%;
        height: 52px;

        border-radius: 11px;

        border:
            1px solid rgba(167, 139, 250, 0.40) !important;

        background:
            linear-gradient(
                90deg,
                #3B0764,
                #6D28D9
            ) !important;

        color: #FFFFFF !important;

        font-size: 17px;
        font-weight: 700;

        box-shadow:
            0 5px 18px rgba(76, 29, 149, 0.45);

        transition: 0.2s;
    }}

    div.stButton > button p {{
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }}

    div.stButton > button:hover {{
        background:
            linear-gradient(
                90deg,
                #581C87,
                #7C3AED
            ) !important;

        border:
            1px solid #A78BFA !important;

        transform:
            translateY(-2px);

        box-shadow:
            0 8px 24px rgba(109, 40, 217, 0.55);

        color: #FFFFFF !important;
    }}


    /* =====================================================
       TABS
       ===================================================== */

    div[data-baseweb="tab-list"] {{
        gap: 8px;

        border-bottom:
            1px solid rgba(255, 255, 255, 0.12);
    }}

    div[data-baseweb="tab-list"] button {{
        background:
            rgba(24, 17, 42, 0.85);

        border:
            1px solid rgba(139, 92, 246, 0.25);

        border-radius:
            10px 10px 0 0;

        padding:
            10px 18px;

        color:
            #D8D4E8 !important;

        font-weight:
            700 !important;
    }}

    div[data-baseweb="tab-list"] button * {{
        color: #D8D4E8 !important;
        font-weight: 700 !important;
    }}

    div[data-baseweb="tab-list"]
    button[aria-selected="true"] {{
        background:
            linear-gradient(
                90deg,
                #3B0764,
                #6D28D9
            ) !important;

        border:
            1px solid #8B5CF6 !important;

        color:
            #FFFFFF !important;
    }}

    div[data-baseweb="tab-list"]
    button[aria-selected="true"] * {{
        color: #FFFFFF !important;
    }}


    /* =====================================================
       DATAFRAME
       ===================================================== */

    div[data-testid="stDataFrame"] {{
        border-radius: 12px;

        overflow: hidden;

        border:
            1px solid rgba(139, 92, 246, 0.40);

        background: #110B20;
    }}


    /* =====================================================
       CONTAINERS / CARDS
       ===================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background:
            rgba(20, 13, 35, 0.90);

        border:
            1px solid rgba(139, 92, 246, 0.35) !important;

        border-radius:
            15px !important;

        box-shadow:
            0 6px 20px rgba(0, 0, 0, 0.30);
    }}


    /* =====================================================
       TITLE DETAILS DIALOG
       WHITE BACKGROUND + DARK TEXT
       ===================================================== */

    div[data-testid="stDialog"] div[role="dialog"],
    div[role="dialog"] {{
        background: #FFFFFF !important;

        color: #111827 !important;

        border:
            1px solid #D1D5DB !important;

        border-radius:
            20px !important;

        box-shadow:
            0 25px 70px rgba(0, 0, 0, 0.60) !important;
    }}


    /* Dialog content */

    div[role="dialog"] [data-testid="stDialogContent"] {{
        background: #FFFFFF !important;
        color: #111827 !important;
    }}


    /* Dialog title */

    div[role="dialog"] h1,
    div[role="dialog"] h2,
    div[role="dialog"] h3 {{
        color: #111827 !important;
        text-shadow: none !important;
    }}


    /* Dialog paragraphs */

    div[role="dialog"] p {{
        color: #111827 !important;
    }}


    /* Dialog markdown */

    div[role="dialog"]
    div[data-testid="stMarkdownContainer"] {{
        color: #111827 !important;
    }}

    div[role="dialog"]
    div[data-testid="stMarkdownContainer"] p {{
        color: #111827 !important;
    }}


    /* Dialog bold text */

    div[role="dialog"] strong {{
        color: #111827 !important;
        font-weight: 800 !important;
    }}


    /* Dialog values such as year / rating */

    div[role="dialog"] code {{
        color: #047857 !important;

        background-color:
            #F3F4F6 !important;

        border-radius:
            5px !important;

        padding:
            2px 5px !important;
    }}


    /* Dialog close X */

    div[role="dialog"] button {{
        color: #111827 !important;
    }}

    div[role="dialog"] button svg {{
        color: #111827 !important;
        fill: #111827 !important;
    }}


    /* =====================================================
       IMPORTANT OVERRIDE

       Streamlit places dialogs through a portal. These rules
       ensure the main page's white-text theme does NOT win
       inside the dialog.
       ===================================================== */

    body div[role="dialog"] p,
    body div[role="dialog"] span,
    body div[role="dialog"] label {{
        color: #111827 !important;
    }}

    body div[role="dialog"] h1,
    body div[role="dialog"] h2,
    body div[role="dialog"] h3 {{
        color: #111827 !important;
    }}

    body div[role="dialog"] strong {{
        color: #111827 !important;
    }}

    body div[role="dialog"] code {{
        color: #047857 !important;
    }}


    /* =====================================================
       ALERT / ERROR BOXES
       ===================================================== */

    div[data-testid="stAlert"] {{
        border-radius: 10px;
        color: #FFFFFF !important;
    }}


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {{
        border-color:
            rgba(255, 255, 255, 0.15) !important;
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

#get movie and tv show details#/
def get_title_details(title_id):

    url = f"https://api.watchmode.com/v1/title/{title_id}/details/"
    response = requests.get(
        url,
        headers=headers
    )
    response.raise_for_status()
    return response.json()

@st.dialog("Streaming Content Comparison", width="large")
def show_statistics_plot(content_counts):

    if content_counts.empty:
        st.warning("No statistics data was found.")
        return

    # Fixed color for each country
    country_colors = {
        "USA": "#2305e8",
        "Spain": "#e80505",
        "Israel": "#05bee8"
    }

    services = content_counts["Service"].unique()

    for i in range(0, len(services), 3):

        columns = st.columns(3)

        for j in range(3):

            if i + j < len(services):

                service_name = services[i + j]

                service_data = content_counts[
                    content_counts["Service"] == service_name
                ]

                fig = px.pie(
                    data_frame=service_data,
                    names="Country",
                    values="Content",
                    color="Country",
                    color_discrete_map=country_colors,
                    title=service_name,
                    hole=0.35
                )

                fig.update_traces(
                    textinfo="value",
                    textposition="inside"
                )

                with columns[j]:
                    st.plotly_chart(
                        fig.to_dict(),
                        use_container_width=True,
                        key=f"pie_{i}_{j}_{service_name}"
                    )

#*Function to get the episodes that have the title - then we can return the full list of episodes, their length and more*
#*add a validation with the API that the title is a tv show*#
def GetTVShowsEpisodes(title_id):
    url = f"https://api.watchmode.com/v1/title/{title_id}/episodes"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    episodes_data = response.json()

    return episodes_data

def show_genre_plot(fig):

    @st.dialog("Your Genre Comparison", width="large")
    def dialog():

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    dialog()

country_codes = {
    "USA": "US",
    "Spain": "ES",
    "Israel": "IL"
}

MediaTypes = {
    "Movie": "movie",
    "TV Series": "tv_series",
}
#Genre ID Converter
genres = pd.read_csv("generes.csv")
genre_dict = dict(zip(genres["id"], genres["name"]))

@st.dialog("Title Details", width="medium")
def show_title_details(title_id):

    details = get_title_details(title_id)

    st.subheader(
        details.get("title", "Title")
    )

    col1, col2 = st.columns([1, 2])

    with col1:

        if details.get("poster"):
            st.image(
                details["poster"],
                width=220
            )

    with col2:

        st.write(
            "**Year:**",
            details.get("year", "N/A")
        )

        st.write(
            "**Genres:**",
            ", ".join(
                details.get("genre_names", [])
            )
        )

        st.write(
            "**User Rating:**",
            details.get("user_rating", "N/A")
        )

        st.write(
            "**Critic Score:**",
            details.get("critic_score", "N/A")
        )

        st.write(
            "**Runtime:**",
            details.get("runtime_minutes", "N/A"),
            "minutes"
        )

    st.write("### Plot")

    st.write(
        details.get(
            "plot_overview",
            "No plot information available."
        )
    )

@st.dialog("🎬 Here is a Movie You might like:", width="large")
def show_random_movie(movie):

    st.title(movie.get("title", "Unknown Title"))

    poster_col, details_col = st.columns([1, 2])

    with poster_col:

        poster = movie.get("posterLarge")

        if not poster:
            poster = movie.get("poster")

        if poster:
            st.image(
                poster,
                use_container_width=True
            )

    with details_col:

        st.subheader("Movie Details")

        st.write(
            "**Year:**",
            movie.get("year", "N/A")
        )

        genre_names = movie.get("genre_names", [])

        if genre_names:
            st.write(
                "**Genres:**",
                ", ".join(genre_names)
            )

        runtime = movie.get("runtime_minutes")

        st.write(
            "**Runtime:**",
            f"{runtime} minutes" if runtime else "N/A"
        )

        st.write(
            "**User Rating:**",
            movie.get("user_rating", "N/A")
        )

        st.write(
            "**Critic Score:**",
            movie.get("critic_score", "N/A")
        )

        st.write(
            "**US Rating:**",
            movie.get("us_rating", "N/A")
        )

        st.write(
            "**Original Language:**",
            movie.get("original_language", "N/A")
        )

    st.subheader("Overview")

    overview = movie.get("plot_overview")

    if overview:
        st.write(overview)
    else:
        st.write("No overview available.")


API_KEY = "mjzfRQYZZq9fMx2RM3c77FX7ncNvgwjtA2Ky3f7q"
urltitles = "https://api.watchmode.com/v1/list-titles"

License = "Proprietary"
headers = {"X-API-Key": API_KEY}


sources = pd.read_csv("sources.csv")

common_services = sources[
    sources["regions"].str.contains("US", na=False) &
    sources["regions"].str.contains("ES", na=False) &
    sources["regions"].str.contains("IL", na=False)
    ]

##Website Section#

st.set_page_config(page_title="Streamer Guide",page_icon="📺",layout="centered")
st.title("▶️Streaming Watch Guide", wrap=True)
st.caption("Find what to watch. Know where to watch it.")

import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs([
    "🍿 AVAILABLE IN MY SERVICE",
    "📺 TV SHOW EPISODE GUIDE",
    "🎬 FIND ME A MOVIE TO WATCH",
    "📊 STATISTICS"
])

with tab1:
        st.header("Content in your service")
        st.write("Choose your country and the service you want to know the content about")

        region1 = st.selectbox(
            "Choose your country of viewing:",
            ["Israel", "USA", "Spain"],
            index=None,
            placeholder="Select an option",
            key="Region Select 1"
        )

        service1 = None
        MediaSelect = None

        if region1 is not None:

            country1 = country_codes[region1]

            services1 = sources[
                sources["regions"].str.contains(country1, na=False)
            ]

            service1 = st.selectbox(
                "Choose your streaming service",
                services1["name"],
                index=None,
                placeholder="Select an option",
                key="Service Select 1"
            )

            if service1 is not None:
                MediaSelect = st.selectbox(
                    "You're looking for a Movie or a TV Show?",
                    ["Movie", "TV Series"],
                    index=None,
                    placeholder="Select type of media",
                    key="Media Select 1"
                )

        if st.button("🔎 Search", use_container_width=True):

            if region1 is None or service1 is None or MediaSelect is None:
                st.error("Please select a country, streaming service and Media Type")

            else:
                with st.spinner("Loading..."):
                    Media_Type = MediaTypes[MediaSelect]

                    source_id1 = services1.loc[
                        services1["name"] == service1,
                        "id"
                    ].iloc[0]

                    params = {
                        "regions": country1,
                        "source_ids": source_id1,
                        "types": Media_Type,
                        "limit": 250
                    }

                    response = requests.get(
                        urltitles,
                        headers=headers,
                        params=params
                    )

                    response.raise_for_status()

                    data = response.json()

                    titles = pd.DataFrame(data["titles"])

                    titles = titles[
                        ["id", "title", "year", "popularity_percentile"]
                    ]

                    titles = titles.sort_values(
                        by="title"
                    ).reset_index(drop=True)

                    st.session_state["titles_results"] = titles

            if "titles_results" in st.session_state:

                titles = st.session_state["titles_results"]

                st.divider()
                st.subheader("Available Titles - Click Box left of the title for more details")

                event = st.dataframe(titles,column_order=["title","year","popularity_percentile"],
                                column_config={
                                "title": "Title",
                                "year": "Year",
                                "popularity_percentile": "Popularity"
                        },

                        hide_index=True,
                        use_container_width=True,

                        selection_mode="single-row",
                        on_select="rerun",

                        key="titles_table_tab1"
                        )

                if event.selection.rows:
                        selected_row = event.selection.rows[0]

                        selected_title_id = int(
                            titles.iloc[selected_row]["id"]
                            )

                        st.session_state["selected_title_id"] = selected_title_id

                        show_title_details(selected_title_id)

with tab2:
    st.header("📺 TV Show Episode Guide")
    st.write("Choose your country and the Service you're using")
    region2 = st.selectbox(
        "Choose your country of viewing:",
        ["Israel", "USA", "Spain"],
        index=None,
        placeholder="Select an option",
        key="Region Select 2"
    )

    service2 = None
    MediaSelect = None

    if region2 is not None:

        country2 = country_codes[region2]

        services2 = sources[
            sources["regions"].str.contains(country2, na=False)
        ]

        service2 = st.selectbox(
            "Choose your streaming service",
            services2["name"],
            index=None,
            placeholder="Select an option",
            key="Service Select 2"
        )

        if service2 is not None:
            user_choices2 = {
                "Country": country2,
                "service": service2,
            }

            source_id2 = services2.loc[
                services2["name"] == user_choices2["service"],
                "id"
            ].iloc[0]

            params = {
                "regions": country2,
                "source_ids": source_id2,
                "types": "tv_series",
                "limit": 250
            }

            response = requests.get(
                urltitles,
                headers=headers,
                params=params
            )

            response.raise_for_status()

            data = response.json()

            titles2 = pd.DataFrame(data["titles"])
            titles2 = titles2.sort_values(by="title")
            TVShowSelect = st.selectbox(label="Select the TV Show", options=titles2["title"], index=None,placeholder="Select TV Show",key="TV Show Select 2")

            user_choices2 = {
                "Country": country2,
                "service": service2,
                "TV_Show": TVShowSelect
        }
            if TVShowSelect is not None:

                title_id2 = titles2.loc[
                    titles2["title"] == user_choices2["TV_Show"],
                    "id"
                ].iloc[0]
                if st.button("🗒️ Show Episode List", use_container_width=True):
                    # Get episode data
                    with st.spinner("Loading..."):
                        episodes_data = GetTVShowsEpisodes(title_id2)

                        episodes = pd.DataFrame(episodes_data)

                        episodes = episodes[
                            [
                                "season_number",
                                "episode_number",
                                "name",
                                "release_date",
                                "runtime_minutes",
                                "overview"
                            ]
                        ]

                        episodes = episodes.rename(columns={
                            "season_number": "Season",
                            "episode_number": "Episode",
                            "name": "Episode Name",
                            "release_date": "Release Date",
                            "runtime_minutes": "Runtime (min)",
                            "overview": "Overview"
                        })

                        episodes = episodes.sort_values(
                            by=["Season", "Episode"]
                        ).reset_index(drop=True)

                        # Get TV show details for poster
                        show_details = get_title_details(title_id2)

                        poster_url = show_details.get("poster")

                        # Create two columns
                        poster_col, table_col = st.columns([1, 4])

                        # LEFT SIDE - POSTER
                        with poster_col:

                            st.subheader(TVShowSelect)

                            if poster_url:
                                st.image(
                                    poster_url,
                                    use_container_width=True
                                )

                        # RIGHT SIDE - EPISODE TABLE
                        with table_col:

                            st.subheader("Episodes")

                            st.dataframe(
                                episodes,

                                column_config={
                                    "Season": st.column_config.NumberColumn(
                                        "Season",
                                        width="small"
                                    ),

                                    "Episode": st.column_config.NumberColumn(
                                        "Episode",
                                        width="small"
                                    ),

                                    "Episode Name": st.column_config.TextColumn(
                                        "Episode Name",
                                        width="medium"
                                    ),

                                    "Release Date": st.column_config.TextColumn(
                                        "Release Date",
                                        width="medium"
                                    ),

                                    "Runtime (min)": st.column_config.NumberColumn(
                                        "Runtime (min)",
                                        width="small"
                                    ),

                                    "Overview": st.column_config.TextColumn(
                                        "Overview",
                                        width="large"
                                    )
                                },

                                row_height=100,
                                use_container_width=True,
                                hide_index=True
                            )

with tab3:

        st.header("Random Movie Recommendation")

        st.write(
            "Choose a release year range and genre, "
            "and we'll pick a random movie for you to watch"
        )

        # Create the genre list from your existing genres DataFrame
        genre_list = genres["name"].tolist()

        # -------------------------
        # YEAR RANGE
        # -------------------------

        year_range = st.slider(
            "Choose release year range:",
            min_value=1950,
            max_value=2026,
            value=(2000, 2026),
            key="random_movie_years"
        )

        start_year = year_range[0]
        end_year = year_range[1]

        # -------------------------
        # GENRE
        # -------------------------

        selected_genre = st.selectbox(
            "Choose genre:",
            genre_list,
            index=None,
            placeholder="Select genre",
            key="random_movie_genre"
        )

        # -------------------------
        # RANDOM MOVIE BUTTON
        # -------------------------

        if st.button(
                "🎲 Pick a Random Movie",
                use_container_width=True,
                key="random_movie_button"
        ):

            if selected_genre is None:

                st.error("Please select a genre.")

            else:

                with st.spinner("Finding a movie..."):

                    genre_id = int(
                        genres.loc[
                            genres["name"] == selected_genre,
                            "id"
                        ].iloc[0]
                    )

                    params = {
                        "types": "movie",
                        "genres": genre_id,
                        "release_date_start": f"{start_year}-01-01",
                        "release_date_end": f"{end_year}-12-31",
                        "limit": 250
                    }

                    response = requests.get(
                        urltitles,
                        headers=headers,
                        params=params
                    )

                    if response.status_code == 200:

                        data = response.json()

                        movies = data.get("titles", [])

                        if len(movies) == 0:

                            st.warning(
                                "No movies were found for these filters."
                            )

                        else:

                            previous_movie_id = st.session_state.get(
                                "previous_random_movie_id"
                            )

                            available_movies = [
                                movie
                                for movie in movies
                                if movie["id"] != previous_movie_id
                            ]

                            if available_movies:

                                random_movie = random.choice(
                                    available_movies
                                )

                            else:

                                random_movie = random.choice(
                                    movies
                                )

                            movie_id = random_movie["id"]

                            st.session_state[
                                "previous_random_movie_id"
                            ] = movie_id

                            details_url = (
                                f"https://api.watchmode.com/v1/"
                                f"title/{movie_id}/details/"
                            )

                            details_response = requests.get(
                                details_url,
                                headers=headers
                            )

                            if details_response.status_code == 200:

                                movie = details_response.json()

                                show_random_movie(movie)

                            else:

                                st.error(
                                    "Could not load the movie details."
                                )

                                st.write(
                                    "Status code:",
                                    details_response.status_code
                                )

                                st.write(
                                    details_response.text
                                )

                    else:

                        st.error(
                            "Could not get movies from Watchmode."
                        )

                        st.write(
                            "Status code:",
                            response.status_code
                        )

                        st.write(
                            "API response:",
                            response.text
                        )
with tab4:
    st.header("Some Information that will help you decide the service best for you")

#/Plot of Streaming Service Content#/
    st.subheader("Amount of Content each streaming service has:")
    if st.button(
            "Show Content Comparison",
            key="show_stats"
    ):
        with st.spinner("Loading..."):

            results = []

            for _, service_row in common_services.iterrows():

                source_id = service_row["id"]
                service_name = service_row["name"]

                for country_name, country_code in country_codes.items():

                    params = {
                        "regions": country_code,
                        "source_ids": source_id,
                        "types": "movie,tv_series",
                        "limit": 1
                    }

                    response = requests.get(
                        urltitles,
                        headers=headers,
                        params=params
                    )

                    if response.status_code == 200:

                        data = response.json()

                        results.append({
                            "Service": service_name,
                            "Country": country_name,
                            "Content": data["total_results"]
                        })

                    else:
                        st.warning(
                            f"Failed: {service_name} - {country_name}"
                        )

            content_counts = pd.DataFrame(results)

            show_statistics_plot(content_counts)

#/Plot of Selected Genres in each service#/
#/
    st.subheader("Choose the Genres that interest you:")
    genres_df = pd.read_csv("generes.csv")

    genre_list = genres_df["name"].tolist()

    country_genre = st.radio(
        "Choose a country:",
        ["Israel", "USA", "Spain"],
        horizontal=True,
        index=None,
        format_func=lambda x: {
            "Israel": "Israel",
            "USA": "USA",
            "Spain": "Spain"
        }[x]
    )

    if country_genre is not None:
        selected_region = country_codes[country_genre]

    col1, col2, col3, col4, col5 = st.columns(5)

    genre1 = None
    genre2 = None
    genre3 = None
    genre4 = None
    genre5 = None

    with col1:
        genre1 = st.selectbox(
            "Genre 1",
            genre_list,
            index=None,
            placeholder="Select genre"
        )
    if genre1 is not None:
        with col2:
            options2 = [g for g in genre_list if g != genre1]

            genre2 = st.selectbox(
                "Genre 2",
                options2,
                index=None,
                placeholder="Select genre"
            )
        if genre2 is not None:
            with col3:
                options3 = [g for g in genre_list if g not in [genre1, genre2]]

                genre3 = st.selectbox(
                    "Genre 3",
                    options3,
                    index=None,
                    placeholder="Select genre"
                )
            if genre3 is not None:
                with col4:
                    options4 = [g for g in genre_list if g not in [genre1, genre2, genre3]]

                    genre4 = st.selectbox(
                        "Genre 4",
                        options4,
                        index=None,
                        placeholder="Select genre"
                    )
                if genre4 is not None:
                    with col5:
                        options5 = [g for g in genre_list if g not in [genre1, genre2, genre3, genre4]]

                        genre5 = st.selectbox(
                            "Genre 5",
                            options5,
                            index=None,
                            placeholder="Select genre"
                        )
    if st.button(
            "Show Services with these genres",
            key="show_genre_stats"
    ):


        if None in [
            genre1,
            genre2,
            genre3,
            genre4,
            genre5
        ]:

            st.error("Please select all 5 genres.")

        else:

            with st.spinner("Loading your genre data..."):

                selected_genres = [
                    genre1,
                    genre2,
                    genre3,
                    genre4,
                    genre5
                ]

                genre_dict = dict(
                    zip(genres_df["name"], genres_df["id"])
                )
                results = []

                for _, service_row in common_services.iterrows():

                    source_id = service_row["id"]
                    service_name = service_row["name"]

                        # Check every selected genre
                    for genre_name in selected_genres:

                        genre_id = genre_dict[genre_name]

                        params = {
                                "regions": selected_region,
                                "source_ids": source_id,
                                "genres": genre_id,
                                "types": "movie,tv_series",
                                "limit": 1
                        }

                        response = requests.get(
                                urltitles,
                                headers=headers,
                                params=params
                            )

                        if response.status_code == 200:

                            data = response.json()

                            results.append({
                                    "Service": service_name,
                                    "Country": country_genre,
                                    "Genre": genre_name,
                                    "Titles": data["total_results"]
                                })

                        else:

                                st.warning(
                                    f"Could not get "
                                    f"{genre_name} data for "
                                    f"{service_name} in "
                                    f"{country_genre}"
                                )

                genre_counts = pd.DataFrame(results)

                genre_counts = genre_counts[genre_counts["Titles"] >= 30]

                figGenres = px.bar(
                    genre_counts,
                    x="Service",
                    y="Titles",
                    color="Service",
                    facet_col="Genre",
                    facet_col_wrap=3,
                    title=f"Genre Availability by Streaming Service - {country_genre}",
                    labels={
                        "Titles": "Number of Titles",
                        "Service": "Streaming Service"
                    }
                )

                show_genre_plot(figGenres)
