from utils import *
import streamlit as st
champions_df = pd.read_pickle('/content/loldle_helper/data/champions_df.pickle')
relations_df = pd.read_csv('/content/loldle_helper/data/relations_df.csv', index_col = [0])
st.write('Let me help you in your Lolde guesses!')

input_widget = st.selectbox(
    label="The guessed champion",
    key='champ_input',
    index=None,
    placeholder='Select a champion',
    label_visibility='hidden',
    
)