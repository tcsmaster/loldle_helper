from utils import *
def main():
    champions_df = pd.read_pickle('champions_df.pkl')
    relations_df = pd.read_csv('relations_df.csv')

    guess_champ = str(input('Which champion was your first guess today?')).title()
    guess_color_scheme = str(
        input('What were the colors for the guess?')
    ).upper()
    guest_list = match_candidates_for_champ(champions_df)
    next_best_guess = guess.next_best_guess(guest_list,guess.get_all_possible_matches(guest_list, champions_df))
    print(f"Based on the color scheme,there are {len(guest_list)} possible champions left:")
    print(guest_list)
    print(f'The champion with the largest information gain is {next_best_guess}')

    while len(guess.match_candidates_for_champ()) > 1:
        guess_champ = str(input('Which champion was your next guess?')).title()
        guess_color_scheme = str(
            input('What were the colors for the guess?')
        ).upper()
        guess = Guess(guess_champ, guess_color_scheme)
        guest_list = guess.match_candidates_for_champ()
        next_best_guess = guess.next_best_guess(guest_list,guess.get_all_possible_matches(guest_list, champions_df))
        print(f"Based on the color scheme,there are {len(guest_list)} possible champions left:")
        print(guest_list)
        print(f'The champion with the largest information gain is {next_best_guess}')



if __name__ == '__main__':
    main()
