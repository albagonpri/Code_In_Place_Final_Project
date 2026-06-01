# Python Mystery Word

## Project Description

Python Mystery Word is a word guessing game created as a final Python project. The player has to guess a hidden word related to Python programming by entering one letter at a time or trying to guess the full word.

The game includes different difficulty levels, hints, a score system, and words loaded from an external file.

## How to Play

When the game starts, the player chooses a difficulty level:

- Easy: 10 guesses
- Medium: 8 guesses
- Hard: 6 guesses

After that, the game shows a hidden word using dashes. The player can:

- Type a single letter
- Try to guess the full word
- Type `HINT` to receive a clue

The objective is to guess the word before running out of guesses.

## Features

- Python-themed words
- Difficulty levels
- Hints for each word
- Score system
- File reading using `words.txt`
- Random word selection
- Option to play again

## Python Concepts Used

This project uses several basic Python concepts:

- Variables
- Strings
- Lists
- Functions
- Loops
- Conditionals
- User input
- File reading
- The `random` module

## Files

This project contains two main files:

- `main.py`: contains the main game code
- `words.txt`: contains the words, categories, and hints used in the game

## How to Run the Project

Make sure both `main.py` and `words.txt` are in the same folder.

Then run the program using:

```bash
python3 main.py
