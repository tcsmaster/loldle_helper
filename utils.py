import numpy as np
import pandas as pd

from itertools import combinations
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

    def __init__(
        self,
        champion,
        color_answer
        ):
        self.champion = champion
        self.color_answer = color_answer
    
    def get_all_possible_matches(
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
            & (df['Comparison'] == self.color_answer)
        ]['Actual_Champion'].to_list()
        return return_list

    def champ_entropy(self,df:pd.DataFrame) -> float:
        champ_probs = (
            df.loc[(df['Guessed_Champion'] == self.champion)\
            |(df['Actual_Champion'] == self.champion)]['Comparison']\
        .value_counts()
        ).to_numpy()
        return entropy(pk=champ_probs)

    def next_best_guess(self,df:pd.DataFrame) -> str:
        candidates_list = self.match_candidates_for_champ(df=df)
        entropy_dict = {el:self.champ_entropy(df) for el in candidates_list}
        sorted_entropy = sorted(
            entropy_dict.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return sorted_entropy

def get_comparison_from_champs(df):
    a = [Champion(**df.iloc[i, :]) for i in range(df.shape[0])]
    combi = combinations(a, 2)

    df = pd.DataFrame(columns = ['Guessed_Champion', 'Actual_Champion', 'Comparison'])
    for el in combi:
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    [
                        {
                            'Guessed_Champion':el[0].Name,
                            'Actual_Champion':el[1].Name,
                            'Comparison':get_result_of_comparison(*el)
                        }
                    ]
                )
            ]
        )
    return df

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