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

    clubs = df['Club'].value_counts().index
    club = st.sidebar.selectbox('Clubs', clubs)
    
    df_players = df[(df['Club'] == club)]
    players = df_players['Name'].value_counts().index
    player = st.sidebar.selectbox('Player', players)
    

    player_stats = df[df['Name'] == player].iloc[0]

    st.image(player_stats['Photo'])
    st.title(player_stats['Name'])

    st.markdown(f'**Club:** {player_stats["Club"]}')
    st.markdown(f'**Position:** {player_stats["Position"]}')

    col1,col2,col3,col4 = st.columns(4)

    col1.markdown(f'**Age:** {player_stats["Age"]}')
    col2.markdown(f'**Height:** {player_stats["Height(cm.)"] / 100}')
    col3.markdown(f'**Weight:** {player_stats["Weight(lbs.)"] * 0.453:.2f}')
    st.divider()

    st.subheader(f'**Overall:** {player_stats["Overall"]}')
    st.progress(int(player_stats['Overall']))
   
    col1,col2,col3,col4 = st.columns(4)

    col1.metric(label = 'Market Value', value = f'£ {player_stats['Value(£)']:,}')
    col2.metric(label = 'Weekly Wage', value = f'£ {player_stats['Wage(£)']:,}')
    col3.metric(label = 'Release Clause', value = f'£ {player_stats['Release Clause(£)']:,}')

