import streamlit as st

st.set_page_config(
    page_title="Clubs",
    page_icon="♣️",
    layout="wide",
    initial_sidebar_state="expanded",
)

if 'data' not in st.session_state:
    st.write('No dataset found: Please, go to settings and import a dataset')
else:
    df = st.session_state['data']
    clubs = df['Club'].value_counts().index
    club = st.sidebar.selectbox('Clubs', clubs)
    df_filtered = df[(df['Club'] == club)].set_index('Name')

    st.image(df_filtered.iloc[0]['Club Logo'])
    st.markdown(f"## {club}")

    columns = ['Age', 'Photo', 'Flag', 'Overall', 'Value(£)','Wage(£)', 'Joined', 'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']


    st.dataframe(df_filtered[columns], 
                 column_config={
                     'Overall': st.column_config.ProgressColumn(
                         'Overall', min_value=0, max_value=100, format='%d'
                     ),
                     'Wage(£)': st.column_config.ProgressColumn(
                         'Weekly Age', min_value=0, max_value=df_filtered['Wage(£)'].max(), format='£%f'
                     ),
                     'Photo': st.column_config.ImageColumn(),
                     'Flag': st.column_config.ImageColumn('Country Flag')
                 })