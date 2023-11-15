from utils import *
def main():
    champions_df = pd.read_pickle('champions_df.pkl')
    relations_df = pd.read_csv('relations_df.csv')

    candidate_champs = set(champions_df['Name'].to_list())
    while True:
        guess_champ = sanitised_input(
            prompt='Which champion was your guess? ',
            type_='champion',
            champs_list = champions_df['Name'].to_list()
            )
        guess_color_scheme = sanitised_input(
            prompt='What were the colors for the guess? ',
            type_ = 'color_answer'
        )
        guess = Guess(guess_champ, guess_color_scheme)
        candidate_champs = candidate_champs.intersection(
            guess.match_candidates_for_champ(
                relations_df
            )
        )
        next_champ_guess = next_best_guess(
            candidate_champs,
            guess.get_all_possible_matches(
                candidate_champs,
                relations_df
            )
        )
        
        print(f"Based on the color scheme,there are {len(candidate_champs)} possible champions left:\n")
        print(candidate_champs)
        print(f'The champion with the largest information gain is {next_champ_guess}\n')

    print(f"There is only one champion left: {candidate_champs}")
if __name__ == '__main__':
    main()
