import numpy as np
import pandas as pd
from scipy.stats import entropy

def matching_champs(
    guessed_champ:str,
    relations_df:pd.DataFrame,
    color_code:str
    ) -> list:
    return_list = relations_df.loc[
        (relations_df['Guessed Champion'] == guessed_champ)\
        & (relations_df['Comparison'] == color_code)
    ]['Candidate Champions'].to_list()
    return return_list

def champ_entropy(champ:str, df:pd.DataFrame) -> float:
    champ_probs = (
        df.loc[df['Guessed Champion'] == champ]['Comparison']\
    .value_counts()
    ).to_numpy()
    return entropy(pk=champ_probs)

def best_guess(
    candidates_list:list,
    relations_df:pd.DataFrame
    ) -> str:
    entropy_dict = {el:champ_entropy(el, relations_df) for el in candidates_list}
    sorted_entropy = sorted(
        entropy_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_entropy[0][0]

def create_relations(champions_df:pd.DataFrame) -> pd.DataFrame:
