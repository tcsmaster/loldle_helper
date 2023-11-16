from utils import *

class Entropy_maximization():

    def __init__(self,solution):
        self.solution = solution

    def gameplay(
        self,
        starting_champ,
        relations_df
        ):
        color_code = relations_df.loc[
            (relations_df['Guessed_Champion'] == starting_champ)\
            &(relations_df['Actual_Champion'] == self.solution)
        ]['Comparison']
        candidate_champs = get_candidates_for_champ