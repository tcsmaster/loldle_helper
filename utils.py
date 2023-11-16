import numpy as np
import pandas as pd

from itertools import product
from pydantic import BaseModel
from typing import List
from scipy.stats import entropy

class Champion(BaseModel):
        Name:str
        Gender: str
        Position: str|List[str]
        Species: str|List[str]
        Resource: str
        Range_type: str|List[str]
        Region: str|List[str]
        Release_year:int

class Guess():
    def __init__(self,champion, color_code):
        self.champion = champion
        self.color_code = color_code

    def get_all_possible_matches(self,
        champions:List,
        df:pd.DataFrame
        ) -> pd.DataFrame:
        possible_matches = df.loc[
        (df['Guessed_Champion'].isin(champions))\
        &(df['Actual_Champion'].isin(champions))
        ]
        return possible_matches

    def match_candidates_for_champ(self,df:pd.DataFrame) -> list:
        return_list = df.loc[
            (df['Guessed_Champion'] == self.champion)\
            & (df['Comparison'] == self.color_code)
        ]['Actual_Champion'].to_list()
        return set(return_list)


def next_best_guess(candidates_list,df) -> str:
    entropy_dict = {el:champ_entropy(el,df) for el in candidates_list}
    sorted_entropy = sorted(
        entropy_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_entropy
 
def champ_entropy(champion,df:pd.DataFrame) -> float:
        champ_probs = (
            df.loc[(df['Guessed_Champion'] == champion)]['Comparison']\
        .value_counts()
        ).to_numpy()
        return entropy(pk=champ_probs)

def get_comparison_from_champs(df):
    a = [Champion(**df.iloc[i, :]) for i in range(df.shape[0])]
    combi = product(a, repeat=2)
    relations_df = pd.DataFrame(
        columns = [
            'Guessed_Champion',
            'Actual_Champion',
            'Comparison'
    ])
    for el in combi:
        relations_df = pd.concat(
            [
                relations_df,
                pd.DataFrame(
                    [
                        {
                            'Guessed_Champion':el[0].Name,
                            'Actual_Champion':el[1].Name,
                            'Comparison':get_comparison_from_champs(el[0], el[1])

                        }
                    ]
                )
            ]
        )
    return relations_df

def get_result_of_comparison(guessed_champion:Champion, candidate_champion:Champion) -> str:
    result = ''
    for (attr, val1), (_, val2) in zip(vars(guessed_champion).items(), vars(candidate_champion).items()):
        if attr == 'Name':
            pass
        elif val1 == val2:
            result += 'G'
        elif attr == 'Release_year':
            res = 'G' if val1 == val2 else 'R'
            result += res
        else:
            both_string = 0
            if isinstance(val1, str):
                val1 = set([val1])
                both_string += 1
            
            if isinstance(val2, str):
                val2= set([val2])
                both_string += 1

            set1 = set(val1)
            set2 = set(val2)
            overlap = bool(set1.intersection(set2))
            if both_string < 2:
                if overlap:
                    result += 'O'
                else:
                    result += 'R'
            else:
                if overlap:
                    result += 'G'
                else:
                    result += 'R'
    return result

def sanitised_input(prompt, question, type_ = str,champs_list=None):
    while True:
        ui = input(prompt)
        try:
            ui = type_(ui)
        except ValueError as e:
            print('Ligma balls!')
        if question == 'champion':
            ui = ui.title()
            if ui not in champs_list:
                print('Please provide an existing League of Legends champion!')
            else:
                return ui
        elif question == 'color_answer':
            ui = ui.upper()
            print(ui)
            if len(ui) != 7:
                print('The answer is not the correct length! Either you missed a letter, or you typed too many!')
                continue
            if not all(c in "ROG" for c in ui):
                print('The color code can only contain r, o or g!')
                continue
            return ui
        else:
            print('This type of question has not been implemented!')
            return