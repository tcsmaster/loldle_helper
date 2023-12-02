from utils import *
import streamlit as st
with open('/content/loldle_helper/champs_list.txt') as f:
    champs_list = [el.strip("\n") for el in f.readlines()]
relations_df = pd.read_csv('/content/loldle_helper/data/relations_df.csv', index_col = [0])
st.write('Let me help you in your Lolde guesses!')

input_widget = st.selectbox(
    label="The guessed champion",
    key='champ_input',
    index=None,
    placeholder='Select a champion',
    label_visibility='hidden',
    options = champs_list,
    on_change=
)