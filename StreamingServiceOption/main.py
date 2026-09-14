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
from difflib import SequenceMatcher

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

#*Function to get the services that have the title - then we use the Source_id and Region from what we get to tell where the title is available*
def GetTitleAvailabel(title_id):

    url = f"https://api.watchmode.com/v1/title/{title_id}/sources"

    response = watchmode_request(url)

    return response.json()

#*get movie and tv show details#/
def get_title_details(title_id):

    url = f"https://api.watchmode.com/v1/title/{title_id}/details/"

    response = watchmode_request(url)

    return response.json()

#*popup for plot of content available in every streaming service*#
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
def GetTVShowsEpisodes(title_id):

    url = f"https://api.watchmode.com/v1/title/{title_id}/episodes"

    response = watchmode_request(url)

    return response.json()

#function to show each of the 3 plots available for Genres*#
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

language_codes = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "he": "Hebrew",
    "ar": "Arabic",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese",
    "ru": "Russian",
    "hi": "Hindi",
    "nl": "Dutch",
    "sv": "Swedish",
    "da": "Danish",
    "no": "Norwegian",
    "fi": "Finnish",
    "pl": "Polish",
    "tr": "Turkish"
}


#popup that extract the details for a specific title#
@st.dialog("Title Details", width="medium")
def show_title_details(title_id):

    details = get_title_details(title_id)

    st.subheader(details.get("title", "Title"))

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

#pop up to show available services for the selected title
@st.dialog("📺 Where Can I Watch This?", width="medium")
def show_watch_options(title_info, sources, country_name):

    st.markdown(
        f"## {title_info.get('name', 'Unknown Title')}"
    )

    year = title_info.get("year")
    media_type = title_info.get("type", "")

    if media_type == "movie":
        type_text = "🎬 Movie"
    elif media_type == "tv_series":
        type_text = "📺 TV Series"
    else:
        type_text = media_type

    info_col1, info_col2 = st.columns(2)

    with info_col1:
        st.caption(type_text)

    with info_col2:
        if year:
            st.caption(f"📅 {year}")

    st.divider()

    st.markdown(
        f"### 🇮🇱 Available in {country_name}"
        if country_name == "Israel"
        else f"### Available in {country_name}"
    )

    if not sources:

        st.info(
            "No streaming options were found "
            f"in {country_name}."
        )

        return

    subscription = []
    free_sources = []
    rent_sources = []
    buy_sources = []

    for source in sources:

        source_type = source.get("type")

        if source_type == "sub":
            subscription.append(source)

        elif source_type == "free":
            free_sources.append(source)

        elif source_type == "rent":
            rent_sources.append(source)

        elif source_type == "buy":
            buy_sources.append(source)

    if subscription:

        st.markdown("#### 🍿 Subscription")

        for source in subscription:

            source_name = source.get(
                "name",
                "Unknown Service"
            )

            st.success(
                f"📺 {source_name}"
            )

    if free_sources:

        st.markdown("#### 🆓 Free")

        for source in free_sources:

            source_name = source.get(
                "name",
                "Unknown Service"
            )

            st.info(
                f"▶️ {source_name}"
            )

    if rent_sources:

        st.markdown("#### 💳 Rent")

        for source in rent_sources:

            source_name = source.get(
                "name",
                "Unknown Service"
            )

            price = source.get("price")

            if price:
                st.write(
                    f"🎞️ **{source_name}** — {price}"
                )
            else:
                st.write(
                    f"🎞️ **{source_name}**"
                )

    if buy_sources:

        st.markdown("#### 🛒 Buy")

        for source in buy_sources:

            source_name = source.get(
                "name",
                "Unknown Service"
            )

            price = source.get("price")

            if price:
                st.write(
                    f"🛍️ **{source_name}** — {price}"
                )
            else:
                st.write(
                    f"🛍️ **{source_name}**"
                )

#Movie Suggestion - Random#
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
#/Converts languge code to be more understandable#/
        original_language = movie.get("original_language")

        language_name = language_codes.get(
            original_language,
            original_language
        )

        st.write(
            "**Original Language:**",
            language_name if language_name else "N/A"
        )

    st.subheader("Overview")

    overview = movie.get("plot_overview")

    if overview:
        st.write(overview)
    else:
        st.write("No overview available.")

#to prevent repeated recommendations#
if "recommended_titles" not in st.session_state:
    st.session_state.recommended_titles = []

API_KEYS = [
    st.secrets["API_KEY_1"],
    st.secrets["API_KEY_2"]
]

urltitles = "https://api.watchmode.com/v1/list-titles"

License = "Proprietary"

sources = pd.read_csv("sources.csv")

common_services = sources[
    sources["regions"].str.contains("US", na=False) &
    sources["regions"].str.contains("ES", na=False) &
    sources["regions"].str.contains("IL", na=False)
    ]

#TITLE PAGE#
st.set_page_config(page_title="Streamer Guide",page_icon="▶️",layout="centered")
st.title("▶️Streaming Watch Guide", wrap=True)
st.caption("Find what to watch. Know where to watch it.")

#Access to the API, using 2 Keys and checking we didn't exceed the 250 calls we have#
def watchmode_request(url, params=None):

    for api_key in API_KEYS:

        headers = {
            "X-API-Key": api_key
        }

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )

        # This key still works
        if response.status_code == 200:
            return response

        # This key has hit a rate/quota limit
        elif response.status_code == 429:
            continue

        # Some other API error
        else:
            response.raise_for_status()

    raise Exception("No Watchmode API keys are currently available.")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🍿 AVAILABLE IN MY SERVICE",
    "📺 TV SHOW EPISODE GUIDE",
    "🎯 FIND ME SOMETHING TO WATCH",
    "🔎 WHERE IS THIS SHOW/MOVIE?",
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

                    response = watchmode_request(
                        urltitles,
                        params
                    )

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

                # Only open the popup if this is a NEW selection
                if (
                        st.session_state.get("last_opened_title_id")
                        != selected_title_id
                ):
                    st.session_state["last_opened_title_id"] = (
                        selected_title_id
                    )

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
            with st.spinner("Loading TV Shows..."):
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

                response = watchmode_request(
                    urltitles,
                    params
                )

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
    st.header("What Should I Watch?")

    st.write(
        "Tell us what you're in the mood for, "
        "and we'll recommend something for you!"
    )

    media_select3 = st.radio(
        "What would you like to watch?",
        list(MediaTypes.keys()),
        horizontal=True,
        index=None,
        key="recommend_media_type"
    )

    country3 = st.radio(
        "Where are you watching from?",
        list(country_codes.keys()),
        horizontal=True,
        index=None,
        format_func=lambda x: {
            "Israel": "Israel",
            "USA": "USA",
            "Spain": "Spain"
        }[x],
        key="recommend_country"
    )

    genre3 = st.selectbox(
        "What genre are you in the mood for?",
        genres["name"].tolist(),
        index=None,
        placeholder="Choose a genre",
        key="recommend_genre"
    )

    year_range3 = st.slider(
        "Choose a release year range:",
        min_value=1950,
        max_value=2026,
        value=(2000, 2026),
        key="recommend_year"
    )

    service3 = None
    services3 = None
    country_code3 = None

    if country3 is not None:
        country_code3 = country_codes[country3]

        sources3 = pd.read_csv("sources.csv")

        services3 = sources3[
            sources3["regions"].str.contains(
                country_code3,
                na=False
            )
        ]

        service3 = st.selectbox(
            "Choose your streaming service:",
            services3["name"].unique(),
            index=None,
            placeholder="Choose a streaming service",
            key="recommend_service"
        )

    if st.button(
            "🎯 Find Something For Me",
            type="primary",
            use_container_width=True,
            key="recommend_button"
    ):

#Checking the User entred all the required data#
        if media_select3 is None:

            st.warning(
                "Please choose Movie or TV Series."
            )

        elif country3 is None:

            st.warning(
                "Please choose a country."
            )

        elif genre3 is None:

            st.warning(
                "Please choose a genre."
            )

        elif service3 is None:

            st.warning(
                "Please choose a streaming service."
            )

        else:

            with st.spinner(
                    "🍿 Searching for something you might like..."
            ):

                try:

                    #converting the Media Type to proper media code

                    media_type3 = MediaTypes[
                        media_select3
                    ]
                    #getting Genre ID
                    genre_id3 = genres.loc[
                        genres["name"] == genre3,
                        "id"
                    ].iloc[0]

                   #getting service id

                    source_id3 = services3.loc[
                        services3["name"] == service3,
                        "id"
                    ].iloc[0]

                    url3 = (
                        "https://api.watchmode.com/"
                        "v1/list-titles/"
                    )
                    #getting the matching title
                    params3 = {
                        "types": media_type3,
                        "regions": country_code3,
                        "source_ids": source_id3,
                        "genres": genre_id3,
                        "release_date_start": int(
                            f"{year_range3[0]}0101"
                        ),
                        "release_date_end": int(
                            f"{year_range3[1]}1231"
                        ),
                        "sort_by": "popularity_desc",
                        "limit": 250
                    }

                    response3 = watchmode_request(
                        url3,
                        params3
                    )
                    if response3 is not None:
                        data3 = response3.json()

                    titles3 = data3.get(
                        "titles",
                        []
                    )


                    if len(titles3) == 0:

                        st.warning(
                            "No titles were found with "
                            "those preferences. Try changing "
                            "the genre, years, or service."
                        )

                    else:

                        #function chooses from 50 titles collected

                        candidate_titles3 = titles3[:50]

                        # REMOVE ALREADY RECOMMENDED TITLES

                        available_titles3 = [
                            title for title in candidate_titles3
                            if title["id"] not in st.session_state.recommended_titles
                        ]

                        #If all recommended already shown, reset

                        if len(available_titles3) == 0:
                            st.session_state.recommended_titles = []
                            available_titles3 = candidate_titles3

                        selected_title3 = random.choice(
                            available_titles3
                        )

                        title_id3 = selected_title3["id"]

                        # Remember this recommendation
                        st.session_state.recommended_titles.append(
                            title_id3
                        )

                        title_id3 = selected_title3[
                            "id"
                        ]

                        details_url3 = (
                            "https://api.watchmode.com/"
                            f"v1/title/{title_id3}/details/"
                        )

                        details_response3 = watchmode_request(
                            details_url3,
                        )
                        if details_response3 is not None:
                            title_details3 = details_response3.json()

                        show_random_movie(
                            title_details3
                        )

                except requests.exceptions.Timeout:

                    st.error(
                        "The Watchmode API took too long "
                        "to respond. Please try again."
                    )

                except requests.exceptions.ConnectionError:

                    st.error(
                        "Could not connect to Watchmode. "
                        "Please check your internet or "
                        "DNS connection."
                    )

                except requests.exceptions.HTTPError as e:

                    st.error(
                        f"Watchmode API error: {e}"
                    )

                except Exception as e:

                    st.error(
                        f"Something went wrong: {e}"
                    )

with tab4:

    st.header("Where Can I Watch This?")

    st.write(
        "Search for a movie or TV series and find out "
        "where it's available to watch."
    )

    st.divider()
#storing my search
    if "watch_results4" not in st.session_state:
        st.session_state.watch_results4 = []

    if "watch_search4" not in st.session_state:
        st.session_state.watch_search4 = ""

    if "watch_media4" not in st.session_state:
        st.session_state.watch_media4 = None

    search_title4 = st.text_input(
        "🎬 Movie or TV Show Name",
        placeholder="Example: Twilight",
        key="watch_search_title"
    )

    media_select4 = st.radio(
        "What are you looking for?",
        list(MediaTypes.keys()),
        horizontal=True,
        index=None,
        key="watch_media_type"
    )

    country4 = st.radio(
        "Where are you watching from?",
        list(country_codes.keys()),
        horizontal=True,
        index=None,
        format_func=lambda x: {
            "Israel": "🇮🇱 Israel",
            "USA": "🇺🇸 USA",
            "Spain": "🇪🇸 Spain"
        }[x],
        key="watch_country"
    )

    st.write("")


    search_button4 = st.button(
        "🔎 Search For Title",
        type="primary",
        use_container_width=True,
        key="watch_search_button"
    )

    if search_button4:

        if not search_title4.strip():

            st.warning(
                "Please enter a movie or TV show name."
            )

        elif media_select4 is None:

            st.warning(
                "Please choose Movie or TV Series."
            )

        else:

            with st.spinner(
                    "🔎 Searching for matching titles..."
            ):

                try:

                    #SEARCH TYPES
                    #3 = Movies only
                    #4 = TV shows only

                    if media_select4 == "Movie":
                        search_type4 = 3
                    else:
                        search_type4 = 4

                    autocomplete_url4 = (
                        "https://api.watchmode.com/"
                        "v1/autocomplete-search/"
                    )

                    autocomplete_params4 = {
                        "search_value": search_title4.strip(),
                        "search_type": search_type4
                    }

                    autocomplete_response4 = watchmode_request(
                        autocomplete_url4,
                        autocomplete_params4
                    )

                    autocomplete_data4 = (
                        autocomplete_response4.json()
                    )

                    results4 = autocomplete_data4.get(
                        "results",
                        []
                    )


                    results4 = [
                        result
                        for result in results4
                        if result.get("result_type") == "title"
                    ]

                    original_search4 = (
                        search_title4.strip().lower()
                    )

                    best_similarity4 = 0

                    for result in results4:

                        result_name4 = (
                            result.get("name", "")
                            .lower()
                        )

                        similarity4 = SequenceMatcher(
                            None,
                            original_search4,
                            result_name4
                        ).ratio()

                        if similarity4 > best_similarity4:
                            best_similarity4 = similarity4

                    #Typo Handeling

                    if (
                            len(results4) == 0
                            or best_similarity4 < 0.55
                    ):

                        cleaned_search4 = (
                            search_title4
                            .strip()
                        )

                        # Use first 3-4 characters
                        # for fallback autocomplete

                        if len(cleaned_search4) >= 4:
                            fallback_search4 = (
                                cleaned_search4[:4]
                            )

                        else:
                            fallback_search4 = (
                                cleaned_search4
                            )

                        fallback_params4 = {
                            "search_value": fallback_search4,
                            "search_type": search_type4
                        }

                        #incase of misspelling

                        fallback_response4 = watchmode_request(
                            autocomplete_url4,
                            fallback_params4
                        )

                        fallback_data4 = (
                            fallback_response4.json()
                        )

                        fallback_results4 = (
                            fallback_data4.get(
                                "results",
                                []
                            )
                        )

                        fallback_results4 = [
                            result
                            for result
                            in fallback_results4
                            if result.get(
                                "result_type"
                            ) == "title"
                        ]

                        # Add fallback results to original results

                        results4.extend(
                            fallback_results4
                        )

                    unique_results4 = {}

                    for result in results4:

                        result_id4 = result.get("id")

                        if result_id4 is not None:
                            unique_results4[
                                result_id4
                            ] = result

                    results4 = list(
                        unique_results4.values()
                    )

                    # FUZZY MATCH SCORE - Compare user's text to each title

                    for result in results4:
                        result_name4 = (
                            result.get(
                                "name",
                                ""
                            ).lower()
                        )

                        fuzzy_score4 = SequenceMatcher(
                            None,
                            original_search4,
                            result_name4
                        ).ratio()

                        result[
                            "fuzzy_score"
                        ] = fuzzy_score4

                    #sorting best matches

                    results4 = sorted(
                        results4,
                        key=lambda x: (
                            x.get(
                                "fuzzy_score",
                                0
                            ),
                            x.get(
                                "relevance",
                                0
                            )
                        ),
                        reverse=True
                    )

                    # Keep a reasonable amount of suggestions

                    results4 = results4[:10]

                    #saving results

                    st.session_state.watch_results4 = (
                        results4
                    )

                    st.session_state.watch_search4 = (
                        search_title4
                    )

                    st.session_state.watch_media4 = (
                        media_select4
                    )

                    if len(results4) == 0:
                        st.warning(
                            "We couldn't find anything "
                            "similar to that title. "
                            "Try another spelling or "
                            "a shorter version of the name."
                        )

                except requests.exceptions.Timeout:

                    st.error(
                        "The Watchmode API took too long "
                        "to respond. Please try again."
                    )

                except requests.exceptions.ConnectionError:

                    st.error(
                        "Could not connect to Watchmode. "
                        "Please check your internet or "
                        "DNS connection."
                    )

                except requests.exceptions.HTTPError as e:

                    st.error(
                        f"Watchmode API error: {e}"
                    )

                except Exception as e:

                    st.error(
                        f"Something went wrong: {e}"
                    )

    #Showing Results

    if st.session_state.watch_results4:

        # Only show old results if search text and media type have not changed

        if (
                search_title4
                == st.session_state.watch_search4
                and media_select4
                == st.session_state.watch_media4
        ):

            st.divider()

            st.subheader(
                "🎬 Which title did you mean?"
            )

            st.caption(
                "Choose the correct title from the "
                "matching results below."
            )

            results4 = (
                st.session_state.watch_results4
            )

            def format_title4(result):

                name4 = result.get(
                    "name",
                    "Unknown Title"
                )

                year4 = result.get(
                    "year"
                )

                result_type4 = result.get(
                    "type",
                    ""
                )

                if result_type4 == "movie":
                    icon4 = "🎬"

                elif result_type4 == "tv_series":
                    icon4 = "📺"

                else:
                    icon4 = "🎞️"

                if year4:
                    return (
                        f"{icon4} "
                        f"{name4} ({year4})"
                    )

                return (
                    f"{icon4} {name4}"
                )


            selected_title4 = st.selectbox(
                "Select a title:",
                results4,
                format_func=format_title4,
                index=None,
                placeholder="Choose the correct title",
                key="selected_watch_title4"
            )

            if selected_title4 is not None:

                title_id4 = selected_title4["id"]

                #Check if details were loaded

                if "title_details4" not in st.session_state:
                    st.session_state.title_details4 = None

                if "title_details_id4" not in st.session_state:
                    st.session_state.title_details_id4 = None

                #Call again to api for different title

                if st.session_state.title_details_id4 != title_id4:

                    with st.spinner(
                            "🎬 Loading title details..."
                    ):

                        try:

                            details_url4 = (
                                "https://api.watchmode.com/"
                                f"v1/title/{title_id4}/details/"
                            )

                            details_response4 = watchmode_request(
                                details_url4
                            )

                            st.session_state.title_details4 = (
                                details_response4.json()
                            )

                            st.session_state.title_details_id4 = (
                                title_id4
                            )

                        except requests.exceptions.Timeout:

                            st.error(
                                "The title details took too long "
                                "to load."
                            )

                        except requests.exceptions.ConnectionError:

                            st.error(
                                "Could not connect to Watchmode."
                            )

                        except requests.exceptions.HTTPError as e:

                            st.error(
                                f"Watchmode API error: {e}"
                            )

                        except Exception as e:

                            st.error(
                                f"Something went wrong: {e}"
                            )

                #display details

                movie_details4 = (
                    st.session_state.title_details4
                )

                if movie_details4:

                    st.divider()

                    poster_col4, details_col4 = (
                        st.columns([1, 2])
                    )

                    # ------------------------------------
                    # POSTER
                    # ------------------------------------

                    with poster_col4:

                        poster4 = movie_details4.get(
                            "posterLarge"
                        )

                        if not poster4:
                            poster4 = movie_details4.get(
                                "poster"
                            )

                        # fallback to autocomplete image

                        if not poster4:
                            poster4 = selected_title4.get(
                                "image_url"
                            )

                        if poster4:
                            st.image(
                                poster4,
                                use_container_width=True
                            )

                    with details_col4:

                        st.subheader(
                            movie_details4.get(
                                "title",
                                selected_title4.get(
                                    "name",
                                    "Unknown Title"
                                )
                            )
                        )

                        year4 = movie_details4.get(
                            "year"
                        )

                        runtime4 = movie_details4.get(
                            "runtime_minutes"
                        )

                        user_rating4 = movie_details4.get(
                            "user_rating"
                        )

                        critic_score4 = movie_details4.get(
                            "critic_score"
                        )

                        genre_names4 = movie_details4.get(
                            "genre_names",
                            []
                        )

                        st.write(
                            "**📅 Year:**",
                            year4 if year4 else "N/A"
                        )

                        if genre_names4:
                            st.write(
                                "**🎭 Genres:**",
                                ", ".join(genre_names4)
                            )

                        st.write(
                            "**⏱️ Runtime:**",
                            (
                                f"{runtime4} minutes"
                                if runtime4
                                else "N/A"
                            )
                        )

                        st.write(
                            "**⭐ User Rating:**",
                            (
                                user_rating4
                                if user_rating4
                                else "N/A"
                            )
                        )

                        st.write(
                            "**🍅 Critic Score:**",
                            (
                                critic_score4
                                if critic_score4
                                else "N/A"
                            )
                        )

                    st.subheader("📖 Overview")

                    overview4 = movie_details4.get(
                        "plot_overview"
                    )

                    if overview4:

                        st.write(
                            overview4
                        )

                    else:

                        st.write(
                            "No overview available."
                        )

                    st.write("")

                    find_sources_button4 = st.button(
                        "📺 Find Where To Watch",
                        type="primary",
                        use_container_width=True,
                        key="find_sources_button4"
                    )

                    if find_sources_button4:

                        if country4 is None:

                            st.warning(
                                "Please choose a country."
                            )

                        else:

                            with st.spinner(
                                    "🍿 Finding streaming services..."
                            ):

                                try:

                                    country_code4 = (
                                        country_codes[
                                            country4
                                        ]
                                    )

                                    # ----------------------------
                                    # SOURCES API CALL
                                    # ----------------------------

                                    sources_url4 = (
                                        "https://api.watchmode.com/"
                                        f"v1/title/{title_id4}/"
                                        "sources/"
                                    )

                                    sources_params4 = {
                                        "regions":
                                            country_code4
                                    }

                                    sources_response4 = watchmode_request(
                                        sources_url4,
                                        sources_params4
                                    )

                                    watch_sources4 = (
                                        sources_response4.json()
                                    )

                                    # ----------------------------
                                    # FILTER COUNTRY
                                    # ----------------------------

                                    watch_sources4 = [
                                        source
                                        for source
                                        in watch_sources4
                                        if source.get(
                                            "region"
                                        ) == country_code4
                                    ]

                                    # ----------------------------
                                    # POPUP
                                    # ----------------------------

                                    show_watch_options(
                                        selected_title4,
                                        watch_sources4,
                                        country4
                                    )

                                except requests.exceptions.Timeout:

                                    st.error(
                                        "The Watchmode API took "
                                        "too long to respond."
                                    )

                                except requests.exceptions.ConnectionError:

                                    st.error(
                                        "Could not connect to "
                                        "Watchmode. Please check "
                                        "your internet or DNS."
                                    )

                                except requests.exceptions.HTTPError as e:

                                    st.error(
                                        f"Watchmode API error: {e}"
                                    )

                                except Exception as e:

                                    st.error(
                                        f"Something went wrong: {e}"
                                    )

with tab5:
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

                    response = watchmode_request(
                        urltitles,
                        params
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

    st.subheader("Choose the Genres that interest you (Max. 5):")
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

        button_col1, button_col2, button_col3 = st.columns(3)

        with button_col1:
            show_services = st.button(
                "📊 Compare Services",
                key="show_genre_Services",
                use_container_width=True
            )

        with button_col2:
            show_content_years = st.button(
                "📈 Content Over the Years",
                key="show_content_years",
                use_container_width=True
            )

        with button_col3:
            show_popularity = st.button(
                "⭐ Popularity Over the Years",
                key="show_popularity_years",
                use_container_width=True
            )

        selected_genres = [
            genre
            for genre in [
                genre1,
                genre2,
                genre3,
                genre4,
                genre5
            ]
            if genre is not None
        ]

        genre_dict = dict(
            zip(genres_df["name"], genres_df["id"])
        )

        # BUTTON 1:COMPARE THE 5 GENRES BETWEEN 3 MAJOR SERVICES

        if show_services:

            if country_genre is None:
                st.error("Please select a country.")


            elif len(selected_genres) == 0:
                st.error("Please select at least one genre.")

            else:

                with st.spinner("Loading your genre data..."):

                    results = []

                    major_services = common_services[
                        common_services["name"].str.contains(
                            r"Netflix|Prime Video|Amazon Prime|Disney\+",
                            case=False,
                            na=False,
                            regex=True
                        )
                    ].copy()

                    #Prevent accidentally getting several versions of the same service
                    major_services = major_services.drop_duplicates(
                        subset="name"
                    )

                    for _, service_row in major_services.iterrows():

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

                            response = watchmode_request(
                                urltitles,
                                params
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

                    if genre_counts.empty:

                        st.warning("No genre statistics were found.")

                    else:

                        genre_counts = genre_counts[
                            genre_counts["Titles"] >= 30
                            ]

                        figGenres = px.bar(
                            genre_counts,
                            x="Service",
                            y="Titles",
                            color="Service",
                            facet_col="Genre",
                            facet_col_wrap=3,
                            title=(
                                f"Genre Availability by Streaming Service "
                                f"- {country_genre}"
                            ),
                            labels={
                                "Titles": "Number of Titles",
                                "Service": "Streaming Service"
                            }
                        )

                        show_genre_plot(figGenres)

        #CREATE/SAVE DATA FOR THE TWO YEAR-BASED GRAPHS

        if show_content_years or show_popularity:

            if country_genre is None:
                st.error("Please select a country.")


            elif len(selected_genres) == 0:
                st.error("Please select at least one genre.")

            else:

                #This key represents the user's current selections
                #If the country or genres change, new API data is required
                current_stats_key = (
                    country_genre,
                    tuple(selected_genres)
                )

                #Check whether we already downloaded this exact data
                if (
                        "genre_year_data" not in st.session_state
                        or "genre_year_key" not in st.session_state
                        or st.session_state["genre_year_key"] != current_stats_key
                ):

                    with st.spinner("Loading genre history..."):

                        year_results = []

                        for genre_name in selected_genres:

                            genre_id = genre_dict[genre_name]

                            params = {
                                "regions": selected_region,
                                "genres": genre_id,
                                "types": "movie,tv_series",
                                "limit": 250
                            }

                            try:

                                response = watchmode_request(
                                    urltitles,
                                    params
                                )

                                response.raise_for_status()

                                data = response.json()

                                titles = data.get("titles", [])

                                for title in titles:

                                    year = title.get("year")

                                    popularity = title.get(
                                        "popularity_percentile"
                                    )

                                    if year is not None:
                                        year_results.append({
                                            "Genre": genre_name,
                                            "Year": year,
                                            "Popularity": popularity
                                        })

                            except requests.exceptions.RequestException as error:

                                st.warning(
                                    f"Could not load "
                                    f"{genre_name}: {error}"
                                )

                        genre_year_data = pd.DataFrame(year_results)

                        #Save it so the second graph doesnt request the same API data again
                        st.session_state["genre_year_data"] = genre_year_data
                        st.session_state["genre_year_key"] = current_stats_key

                else:

                    # Use data already downloaded
                    genre_year_data = st.session_state[
                        "genre_year_data"
                    ]

                #Button 2:CONTENT COUNT OVER THE YEARS

                if show_content_years:

                    if genre_year_data.empty:

                        st.warning(
                            "No historical genre data was found."
                        )

                    else:

                        content_over_years = (
                            genre_year_data
                            .groupby(
                                ["Year", "Genre"]
                            )
                            .size()
                            .reset_index(
                                name="Titles"
                            )
                        )

                        content_over_years = (
                            content_over_years
                            .sort_values("Year")
                        )

                        figYears = px.line(
                            content_over_years,
                            x="Year",
                            y="Titles",
                            color="Genre",
                            markers=True,
                            title=(
                                f"Content Released Over the Years "
                                f"- {country_genre}"
                            ),
                            labels={
                                "Titles": "Number of Titles",
                                "Year": "Release Year"
                            }
                        )

                        show_genre_plot(figYears)

                #BUTTON 3: POPULARITY OVER THE YEARS

                if show_popularity:

                    if genre_year_data.empty:

                        st.warning(
                            "No historical genre data was found."
                        )

                    else:

                        # provide a popularity value
                        popularity_data = genre_year_data.dropna(
                            subset=["Popularity"]
                        )

                        if popularity_data.empty:

                            st.warning(
                                "No popularity data was available."
                            )

                        else:

                            popularity_over_years = (
                                popularity_data
                                .groupby(
                                    ["Year", "Genre"],
                                    as_index=False
                                )["Popularity"]
                                .mean()
                            )

                            popularity_over_years = (
                                popularity_over_years
                                .sort_values("Year")
                            )

                            figPopularity = px.line(
                                popularity_over_years,
                                x="Year",
                                y="Popularity",
                                color="Genre",
                                markers=True,
                                title=(
                                    f"Genre Popularity Over the Years "
                                    f"- {country_genre}"
                                ),
                                labels={
                                    "Popularity":
                                        "Average Popularity Percentile",
                                    "Year":
                                        "Release Year"
                                }
                            )

                            show_genre_plot(figPopularity)
