# 📺 Streaming Watch Guide

A Streamlit web application for discovering movies and TV shows, checking streaming availability, exploring TV episode information, receiving personalized recommendations, and comparing streaming-service content.

The application uses the **Watchmode API** for movie, TV, streaming-source, title-detail, and episode data.

---

## ✨ Features

The application contains five main tabs:

### 1. 🍿 Available in My Service

Find movies or TV series available on a selected streaming service.

The user can:

- Choose a country:
  - Israel
  - USA
  - Spain
- Choose a streaming service available in that country.
- Choose between **Movie** and **TV Series**.
- Search the service's available titles.
- View title, release year, and popularity information.
- Select a title from the results table to open a details window.

The title-details window can display information such as:

- Poster
- Release year
- Genres
- User rating
- Critic score
- Runtime
- Plot overview

---

### 2. 📺 TV Show Episode Guide

Browse episode information for TV shows available on a selected streaming service.

The user can:

1. Choose a country.
2. Choose a streaming service.
3. Select a TV show.
4. Click **Show Episode List**.

The application displays the show's poster together with an episode table containing information such as:

- Season number
- Episode number
- Episode name
- Release date
- Runtime
- Episode overview

---

### 3. 🎯 Find Me Something to Watch

Get a movie or TV recommendation based on your preferences.

The user can select:

- Movie or TV Series
- Country
- Genre
- Release-year range
- Streaming service

The application searches matching Watchmode titles and randomly selects a recommendation from the most popular results.

Previously recommended titles are temporarily remembered during the current Streamlit session to reduce repeated recommendations.

The recommendation window may display:

- Poster
- Title
- Year
- Genres
- Runtime
- User rating
- Critic score
- US content rating
- Original language
- Plot overview

---

### 4. 🔎 Where Is This Show/Movie?

Search for a specific movie or TV show and check where it can be watched.

The application uses Watchmode's autocomplete search to locate matching titles.

The user can:

1. Enter a movie or TV-show name.
2. Choose Movie or TV Series.
3. Choose a country.
4. Select the correct title from the search results.
5. View title information.
6. Click **Find Where To Watch** to check streaming availability.

The application can display availability such as:

- Subscription services
- Free streaming sources
- Rental options
- Purchase options

---

### 5. 📊 Statistics

Provides information that can help compare streaming services.

The application can compare the amount of content available on streaming services across the supported countries.

It also contains genre-comparison functionality using the local genre data.

---

# 🗂️ Project Files

The project expects the following files:

```text
StreamingServiceOption/
│
├── main.py
├── sources.csv
├── generes.csv
├── Stars.png
│
└── .streamlit/
    └── secrets.toml
```

### `main.py`

This is the **main application file** and the file that must be executed with Streamlit.

### `sources.csv`

Contains streaming-service/source information used by the application, including service IDs and supported regions.

### `generes.csv`

Contains Watchmode genre IDs and genre names.

> **Important:** The project currently uses the filename `generes.csv`, with this exact spelling.  
> Do not rename it to `genres.csv` unless you also update the filename inside `main.py`.

### `Stars.png`

Background image used by the Streamlit interface.

### `.streamlit/secrets.toml`

Stores the Watchmode API keys securely so that the keys do not need to be written directly inside `main.py`.

---

# ⚙️ Requirements

The project requires Python and the following Python packages:

```text
streamlit
requests
pandas
plotly
matplotlib
seaborn
```

The application also uses Python standard-library modules including:

```text
base64
random
difflib
```

---

# 📦 Installation

## 1. Download or clone the project

Place all project files inside the same project directory.

For example:

```text
C:\Users\<username>\PycharmProjects\StreamingServiceOption
```

---

## 2. Create or activate a Python virtual environment

Using a virtual environment is recommended.

In PyCharm, the project's configured interpreter/virtual environment can be used.

From a Windows terminal, an existing virtual environment can normally be activated with:

```bash
.venv\Scripts\activate
```

---

## 3. Install the required packages

Run:

```bash
pip install streamlit requests pandas plotly matplotlib seaborn
```

If `pip` is associated with a different Python installation, you can instead use:

```bash
python -m pip install streamlit requests pandas plotly matplotlib seaborn
```

---

# 🔑 Watchmode API Configuration

The application requires Watchmode API keys.

The keys are intentionally loaded with Streamlit's `st.secrets` system instead of being stored directly in the Python source code.

## 1. Create the `.streamlit` directory

Inside the project directory, create a folder named:

```text
.streamlit
```

Your project should then look like:

```text
StreamingServiceOption/
├── main.py
├── sources.csv
├── generes.csv
├── Stars.png
└── .streamlit/
```

## 2. Create `secrets.toml`

Inside `.streamlit`, create:

```text
secrets.toml
```

## 3. Add the API keys

Add the following to `secrets.toml`:

```toml
API_KEY_1 = "YOUR_WATCHMODE_API_KEY_1"
API_KEY_2 = "YOUR_WATCHMODE_API_KEY_2"
```

Replace the example values with your real Watchmode API keys.

The application is currently designed to try the available API keys and move to another key when a key reaches a rate/quota limit.

> **Security:** Do not upload your real `secrets.toml` file to a public GitHub repository.

If the project is stored in Git, it is recommended to add this line to `.gitignore`:

```gitignore
.streamlit/secrets.toml
```

---

# ▶️ How to Run the Project

## Main file to execute

The application entry point is:

```text
main.py
```

Because this is a **Streamlit application**, do not normally run it with:

```bash
python main.py
```

Instead, open a terminal in the project directory and run:

```bash
streamlit run main.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run main.py
```

Streamlit should start a local web server and open the application in your browser.

A local address will normally be shown in the terminal, such as:

```text
http://localhost:8501
```

---

# 🧭 How to Use the Application

After starting the application, use the tabs at the top of the page.

## Find content on a streaming service

Open:

```text
🍿 AVAILABLE IN MY SERVICE
```

Then:

1. Select your country.
2. Select a streaming service.
3. Select Movie or TV Series.
4. Click **Search**.
5. Browse the returned table.
6. Select a row to view more information about the title.

---

## View TV-show episodes

Open:

```text
📺 TV SHOW EPISODE GUIDE
```

Then:

1. Select your country.
2. Select a streaming service.
3. Select a TV show.
4. Click **Show Episode List**.
5. Browse the episode information.

---

## Get a recommendation

Open:

```text
🎯 FIND ME SOMETHING TO WATCH
```

Then:

1. Select Movie or TV Series.
2. Select your country.
3. Choose a genre.
4. Select a release-year range.
5. Select a streaming service.
6. Click **Find Something For Me**.

The application will choose a matching recommendation and display its details.

---

## Find where a specific title is streaming

Open:

```text
🔎 WHERE IS THIS SHOW/MOVIE?
```

Then:

1. Enter the name of a movie or TV show.
2. Select Movie or TV Series.
3. Select your country.
4. Click the search button.
5. Choose the correct title from the results.
6. Review the title information.
7. Click **Find Where To Watch**.

---

## Compare services

Open:

```text
📊 STATISTICS
```

Use the available comparison controls to view statistics about streaming-service content and genres.

---

# 🌍 Supported Countries

The current application interface supports:

| Country | Watchmode Region Code |
|---|---|
| Israel | `IL` |
| USA | `US` |
| Spain | `ES` |

Streaming-service availability may differ between countries.

---

# 🌐 External API

This project uses the **Watchmode API**.

The application uses Watchmode data for functionality including:

- Listing titles
- Searching titles
- Retrieving title details
- Retrieving streaming sources
- Retrieving TV episodes
- Retrieving genre-related information

Because the application depends on an external API:

- An internet connection is required.
- A valid Watchmode API key is required.
- Results depend on the data returned by Watchmode.
- API request limits or quotas may apply.

---

# 🛠️ Troubleshooting

## `StreamlitSecretNotFoundError` or missing API key

Make sure this file exists:

```text
.streamlit/secrets.toml
```

and contains:

```toml
API_KEY_1 = "your_key"
API_KEY_2 = "your_second_key"
```

Also make sure `.streamlit` is inside the same project directory from which Streamlit is being launched.

---

## `FileNotFoundError: Stars.png`

Make sure:

```text
Stars.png
```

is located in the project directory beside `main.py`.

---

## `FileNotFoundError: sources.csv`

Make sure:

```text
sources.csv
```

is located beside `main.py`.

---

## `FileNotFoundError: generes.csv`

Make sure the file is named exactly:

```text
generes.csv
```

The current Python code uses this spelling.

---

## `streamlit` is not recognized

Try:

```bash
python -m streamlit run main.py
```

If Streamlit is not installed, run:

```bash
python -m pip install streamlit
```

---

## Watchmode connection, DNS, SSL, or timeout errors

The application requires an active internet connection to communicate with the Watchmode API.

Connection problems may be caused by:

- Internet connectivity
- DNS configuration
- SSL/certificate configuration
- Firewall or proxy settings
- Watchmode service availability

---

## API quota/rate-limit errors

Watchmode accounts can have request limits depending on the API plan.

This project supports two configured API keys and attempts to move to another configured key when one returns a rate-limit response.

---

# 🔒 Security

API keys should never be committed directly to public source control.

Keep:

```text
.streamlit/secrets.toml
```

private.

A recommended `.gitignore` entry is:

```gitignore
.streamlit/secrets.toml
```

---

# 🧰 Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Requests**
- **Plotly**
- **Matplotlib**
- **Seaborn**
- **Watchmode API**
- **HTML/CSS embedded in Streamlit**

---

# 📌 Entry Point Summary

To start the application:

```bash
streamlit run main.py
```

or:

```bash
python -m streamlit run main.py
```

The file that should be executed is:

```text
main.py
```

---

## 📄 License

The project source currently identifies the application's license as:

```text
Proprietary
```
