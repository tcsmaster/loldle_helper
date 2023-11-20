from utils import *

def Entropy_maximization(
    champ,
    solution_champ,
    champs_list,
    relations_df
    ):
    color_code = relations_df.loc[
            (relations_df['Guessed_Champion'] == starter_champ)\
            &(relations_df['Actual_Champion'] == solution_champ)
        ]['Comparison']
    while color_code != 'GGGGGGG':
        current_guess = Guess(champ)
        candidate_champs = get_candidates_for_champ