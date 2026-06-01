import random

def load_words(filename):
    words = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line != "":
                parts = line.split(",")

                category = parts[0]
                word = parts[1].upper()
                hint = parts[2]

                words.append([category, word, hint])

    return words


def choose_difficulty():
    print("Choose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        return 10
    elif choice == "2":
        return 8
    elif choice == "3":
        return 6
    else:
        print("Invalid choice. Medium difficulty selected.")
        return 8


def create_hidden_word(word, guessed_letters):
    hidden = ""

    for letter in word:
        if letter in guessed_letters:
            hidden += letter
        else:
            hidden += "-"

    return hidden


def calculate_score(guesses_left, hints_used):
    score = guesses_left * 10
    score -= hints_used * 5

    if score < 0:
        score = 0

    return score


def play_game():
    print("Welcome to Python Mystery Word!")
    print()

    words = load_words("words.txt")
    secret_item = random.choice(words)

    category = secret_item[0]
    secret_word = secret_item[1]
    hint = secret_item[2]

    guesses_left = choose_difficulty()
    guessed_letters = []
    hints_used = 0

    print()
    print("Category:", category.capitalize())

    game_over = False

    while not game_over:
        current_word = create_hidden_word(secret_word, guessed_letters)

        print()
        print("The word now looks like this:", current_word)
        print("You have", guesses_left, "guesses left.")
        print("Guessed letters:", guessed_letters)

        guess = input("Type a letter, the full word, or HINT: ")
        guess = guess.upper()

        if guess == "HINT":
            print("Hint:", hint)
            hints_used += 1
            guesses_left -= 1

        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")

            else:
                guessed_letters.append(guess)

                if guess in secret_word:
                    print("That guess is correct.")
                else:
                    print("That guess is incorrect.")
                    guesses_left -= 1

        elif guess == secret_word:
            print()
            print("Correct! You guessed the full word.")
            game_over = True

        else:
            print("That is not the correct word.")
            guesses_left -= 1

        current_word = create_hidden_word(secret_word, guessed_letters)

        if current_word == secret_word:
            print()
            print("Congratulations! You guessed the word:", secret_word)
            game_over = True

        elif guesses_left <= 0:
            print()
            print("Game over!")
            print("The secret word was:", secret_word)
            game_over = True

    score = calculate_score(guesses_left, hints_used)
    print("Your final score is:", score)


def main():
    play_again = "YES"

    while play_again == "YES":
        play_game()
        print()
        play_again = input("Do you want to play again? YES or NO: ")
        play_again = play_again.upper()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()