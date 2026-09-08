#pip install streamlit
#pip install requests

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
import streamlit as st

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







##Website Section#

#st.set_page_config(page_title="Streamer Guide",page_icon="📺",layout="centered")
#st.title("Streaming Watch Guide", wrap=True)

#name = st.text_input('Enter your name', '')
#if name:
#    st.write(f'Hello {name}, Looking for something to watch?!')
#choice = st.selectbox(label="Choose your country of viewing:",options=["Israel", "USA", "Spain"],index=0,placeholder="Select an option...")


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
