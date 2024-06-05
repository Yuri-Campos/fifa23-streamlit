import streamlit as st
import pandas as pd
import os
from helpers.datasets import json_to_list

st.set_page_config(
    layout='wide',
    page_title='Fifa Stats'
)



@st.cache_data
def load_data(dataset):
    df = pd.read_csv(f'data/datasets/{dataset}.csv')
    return df


games = json_to_list()

fifa = st.sidebar.selectbox('Game', games)

df = load_data(fifa)
st.session_state['df_fifa'] = df
df.set_index('Name', inplace = True)

clubs = df['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubs)
df_filtered = df[df['Club'] == club]

players = df_filtered.index
player = st.sidebar.selectbox('Jogador', players)
df_filtered = df[df.index == player]

show_bar = st.checkbox('Show')
if show_bar:
    st.bar_chart(df_filtered['Overall'])
    st.write(fifa)