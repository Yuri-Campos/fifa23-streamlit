import streamlit as st

st.set_page_config(
    page_title="Fifa Stats",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="expanded",
)


if 'data' not in st.session_state:
    st.write('No dataset found: Please, go to settings and import a dataset')
else:
    df = st.session_state['data']
    st.write(df)