from utils import *

champions_df = pd.read_pickle('champions_df.pkl')
relations_df = pd.read_pickle('relations_df.pkl')

while True:
    first_guess = str(input('Which champion was your first guess today?')).title()
    first_guess_color_scheme = str(
        input('What were the colors for the given guess?')
    ).upper()
    candidate_list = matching_champs(
    first_guess,
    relations_df,
    first_guess_color_scheme
    )
