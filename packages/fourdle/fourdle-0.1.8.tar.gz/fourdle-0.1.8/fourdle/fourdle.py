import random
import random

class Fourdle:
    def __init__(self, word_list):
        self.word_list = word_list
        self.target_word = ""
        self.state = None
        self.guesses = 0
        self.max_guesses = 10  # e.g., maximum 10 guesses allowed, can adjust as required

    def reset(self):
        self.target_word = random.choice(self.word_list)
        self.state = self._get_initial_state()
        self.guesses = 0
        return self.state

    def step(self, action):
        self.guesses += 1
        hint = self.validate_word(action)
        reward = self._get_reward(hint)

        done = False
        if ''.join(hint) == 'GGGG' or self.guesses >= self.max_guesses:
            done = True

        self.state = hint

        return self.state, reward, done

    def _get_initial_state(self):
        # Represent initial state, e.g., 'WWWW' for a 4-letter word
        return ['W', 'W', 'W', 'W']
    
    def validate_word(self, guess: str):
            guess = guess.upper()
            hint = ''
            target_word_list = list(self.target_word)
            
            # First pass: Check for letters in the correct positions ('G')
            for g, t in zip(guess, target_word_list):
                if g == t:
                    hint += 'G'
                    target_word_list[target_word_list.index(g)] = None  # Mark as used
                else:
                    hint += 'X'  # Placeholder
            
            # Second pass: Check for correct letters in the wrong positions ('Y')
            for i, (g, h) in enumerate(zip(guess, hint)):
                if h == 'X':  # Only check the letters that were not already marked 'G'
                    if g in target_word_list:
                        hint = hint[:i] + 'Y' + hint[i+1:]
                        target_word_list[target_word_list.index(g)] = None  # Mark as used

            # Replace remaining 'X' placeholders with 'W'
            hint = hint.replace('X', 'W')

            return hint

    def _get_reward(self, hint):
        if ''.join(hint) == 'GGGG':
            return 1000  # guessed correctly
        elif 'G' in hint:
            return 50  # partial correct
        elif 'Y' in hint:
            return 25  # right letter, wrong position
        else:
            return -10  # no letters matched

    def render(self):
        # For this text-based game, we can simply print the current state
        print(f"Current Hint: {''.join(self.state)}, Guesses left: {self.max_guesses - self.guesses}")
    
    def set_random_word(self):
        self.target_word = random.choice(self.word_list)

    def set_target_word(self, word: str):
        self.target_word = word


    @staticmethod
    def load_words_from_file(file_path: str) -> list:
        with open(file_path, 'r') as f:
            return f.read().splitlines()

def main():
    word_path = "fourdle/data/words.txt"
    word_list = Fourdle.load_words_from_file(word_path)
    word_list = [word.upper() for word in word_list]
    game = Fourdle(word_list)

    nbr_games = 10
    # Simulate a few steps (replacing 'BOLT' with agent's action)
    for iteration in range(nbr_games):
        initial_state = game.reset()
        done = False
        while not done:
            guess = random.choice(game.word_list)
            state, reward, done = game.step(guess)
            print(f"State: {state}, Reward: {reward}, Done: {done}, Guess {guess}, Target {game.target_word}")



    game.render()
    


if __name__=="__main__":
    main()