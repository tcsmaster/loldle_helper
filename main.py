from utils import *

champions_df = pd.read_pickle('champions_df.pkl')
relations_df = pd.read_pickle('relations_df.pkl')

guess_champ = str(input('Which champion was your first guess today?')).title()
guess_color_scheme = str(
    input('What were the colors for the given guess?')
).upper()
guess = Guess(guess_champ, guess_color_scheme)
next_best_guess = guess.best_guess(relations_df)
