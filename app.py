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
    options = champs_list
)
col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1,1,1])

with col1:
    gender = st.selectbox(
        label="The guess' gender color",
        key='gender_input',
        index=None,
        placeholder='Select a color!',
        label_visibility='hidden',
        options = ['Green', 'Red'] 
    )
with col2:
    position = st.selectbox(
        label="The guess' position color",
        key='position_input',
        index=None,
        placeholder='Select a color!',
        label_visibility='hidden',
        options = ['Green', 'Orange','Red'] 
    )
with col3:
    species = st.selectbox(
        label="The guess' species color",
        key='species_input',
        index=None,
        placeholder='Select a color!',
        label_visibility='hidden',
        options = ['Green', 'Orange','Red'] 
    )
with col4:
    resource = st.selectbox(
        label="The guess' resource color",
        key='resource_input',
        index=None,
        placeholder='Select a color!',
        label_visibility='hidden',
        options = ['Green', 'Orange', 'Red'] 
    )
with col5:
    range_type = st.selectbox(
        label="The guess' range_type color",
        key='range_type_input',
        index=None,
        placeholder='Select a color!',
        label_visibility='hidden',
        options = ['Green', 'Orange','Red'] 
    )
with col6:
    region = st.selectbox(
        label="The guess' region color",
        key='region_input',
        index=None,
        placeholder='Select a color!',
        label_visibility='hidden',
        options = ['Green', 'Orange','Red'] 
    )
with col7:
    release_year = st.selectbox(
        label="The guess' gender color",
        key='release_year_input',
        index=None,
        placeholder='Select a color!',
        label_visibility='hidden',
        options = ['Green', 'Red: lower', 'Red:higher'] 
    )
