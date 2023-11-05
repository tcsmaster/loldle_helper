import numpy as np
import pandas as pd
from scipy.stats import entropy

class Guess():

    def __init__(self, champion, color_answer):
        self.champion = champion
        self.color_answer = color_answer
    
    def matching_champs(
        self,
        relations_df:pd.DataFrame
        ) -> list:
        return_list = relations_df.loc[
            (relations_df['Guessed Champion'] == self.champ)\
            & (relations_df['Comparison'] == self.color_answer)
        ]['Candidate Champions'].to_list()
        return return_list

    def champ_entropy(self, df:pd.DataFrame) -> float:
        champ_probs = (
            df.loc[df['Guessed Champion'] == self.champion]['Comparison']\
        .value_counts()
        ).to_numpy()
        return entropy(pk=champ_probs)

    def best_guess(
        self,
        relations_df:pd.DataFrame
        ) -> str:
        candidates_list = self.matching_champs(relations_df=relations_df)
        entropy_dict = {el:self.champ_entropy(el, relations_df) for el in candidates_list}
        sorted_entropy = sorted(
            entropy_dict.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return sorted_entropy[0][0]