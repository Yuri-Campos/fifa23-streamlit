import streamlit as st
import pandas as pd
from helpers.datasets import json_to_list

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_data(dataset):
    df = pd.read_csv(f'data/datasets/{dataset}.csv')
    return df


games = json_to_list()
game = st.selectbox('Game', games)
btn = st.button('Import')
if btn:
    df = load_data(game)
    #df.set_index('Name', inplace = True)
    if not df.empty:
        st.write('Dataset imported!')
        df.sort_values(by='Overall', ascending=False, inplace=True)
        df = df[df['Value(£)'] > 0]
        df.drop(['ID', 'Unnamed: 0'], axis= 1, inplace=True)
        df.set_index('Name')
        st.session_state['data'] = df
    else:
        st.write('Failed to import dataset!')