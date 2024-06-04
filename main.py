import streamlit as st
import pandas as pd
import os


st.set_page_config(
    layout='wide',
    page_title='Fifa Stats'
)


@st.cache_data
def load_data(dataset):
    df = pd.read_csv(f'data/{dataset}.csv')
    return df


st.selectbox('Game', )