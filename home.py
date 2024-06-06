import streamlit as st
import pandas as pd
import os
import webbrowser
from helpers.datasets import json_to_list



st.set_page_config(
    page_title="Fifa Stats",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

#@st.cache_data



st.markdown('# FIFA DATASET! ⚽')
st.sidebar.markdown('Made by [Yuri Campos](https://github.com/Yuri-Campos)')


btn = st.button('Kaggle Dataset')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    '''
    ### Objective

    The primary goal of this project is to analyze players and teams from FIFA 17 to FIFA 23, enabling more efficient decision-making for career mode transfers. By leveraging visual analytics, this project aims to provide deep insights into player performance, team dynamics, and market trends.
    ### Overview

    This project focuses on creating an interactive and comprehensive visualization tool that captures essential data about players and teams over multiple FIFA game editions. By examining historical and current data, users can make informed transfer decisions, optimize team compositions, and anticipate player development trajectories.
    '''
)