"""
Solution to the "Wordle" milestone project.
Find the problem at:
https://docs.google.com/presentation/d/1BH-P4RbhZK3YNmhIua4yMPxFEkuDnyXJ89chy7-uTQA/edit#slide=id.g2ebf5832d39_0_0
"""

import re
import shutil
import random

from tabulate import tabulate
from termcolor import colored


RED = "red"
GREEN = "green"
YELLOW = "yellow"
WHITE = "white"


wordle_board = [['', '', '', '', ''] for _ in range(6)]
keyboard = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]


def color_text(text, color, attrs=None):
    """Color text on the CLI."""

    if attrs is None:
        attrs = ["bold"]
    return colored(text, color, attrs=attrs)

def _how_to_play():
    """Return instructions on how to play the game."""

    how_to_play = "Get 6 chances to guess a 5-letter word.\nHow To Play\nGuess the Wordle in 6 tries.\nEach guess must be a valid 5-letter word.\nThe color of the tiles will change to show how close your guess was to the word.\nExamples\n"
    how_to_play += color_text("W", GREEN) + "EARY\n"
    how_to_play += color_text("W", WHITE) + " is in the word and in the correct spot.\n"
    how_to_play += "P" + color_text("I", YELLOW) + "LLS\n"
    how_to_play += color_text("I", WHITE) + " is in the word but in the wrong spot.\n"
    how_to_play += "VAG" + color_text("U", RED) + "E\n"
    how_to_play += color_text("U", WHITE) + " is not in the word in any spot.\n"
    return how_to_play

def _strip_ansi_codes(s):
    """Strip color ansi codes so that length of string can be calculated correctly."""

    return re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K]?', '', s)
def _center_text(text):
    """Center text within the terminal."""

    text_width = len(_strip_ansi_codes(text))
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - text_width) // 2
    return ' ' * padding + text

def print_ui(board):
    """Print the wordle board and the keyboard."""

    print("\n"*2)
    print(_center_text(color_text("WORDLE", WHITE)))

    board_tabulated = tabulate(board, tablefmt="heavy_grid")

    for line in board_tabulated.split('\n'):
        print(_center_text(line))

    print("\n"*2)

    for row in keyboard:
        keyboard_line = tabulate([row], tablefmt="heavy_grid")

        for line in keyboard_line.split('\n'):
            print(_center_text(line))
def main():
    """Entrypoint for running the Wordle game."""

    wordle_bank = ["About", "Alert", "Argue", "Beach", "Above", "Alike", "Arise", "Began", "Abuse", "Alive", "Array", "Begin", "Actor", "Allow", "Aside", "Begun", "Acute", "Alone", "Asset", "Being", "Admit", "Along", "Audio", "Below", "Adopt", "Alter", "Audit", "Bench", "Adult", "Among", "Avoid", "Billy", "After", "Anger", "Award", "Birth", "Again", "Angle", "Aware", "Black", "Agent", "Angry", "Badly", "Blame", "Agree", "Apart", "Baker", "Blind", "Ahead", "Apple", "Bases", "Block", "Alarm", "Apply", "Basic", "Blood", "Album", "Arena", "Basis", "Board", "Boost", "Buyer", "China", "Cover", "Booth", "Cable", "Chose", "Craft", "Bound", "Calif", "Civil", "Crash", "Brain", "Carry", "Claim", "Cream", "Brand", "Catch", "Class", "Crime", "Bread", "Cause", "Clean", "Cross", "Break", "Chain", "Clear", "Crowd", "Breed", "Chair", "Click", "Crown", "Brief", "Chart", "Clock", "Curve", "Bring", "Chase", "Close", "Cycle", "Broad", "Cheap", "Coach", "Daily", "Broke", "Check", "Coast", "Dance", "Brown", "Chest", "Could", "Dated", "Build", "Chief", "Count", "Dealt", "Built", "Child", "Court", "Death", "Debut", "Entry", "Forth", "Group", "Delay", "Equal", "Forty", "Grown", "Depth", "Error", "Forum", "Guard", "Doing", "Event", "Found", "Guess", "Doubt", "Every", "Frame", "Guest", "Dozen", "Exact", "Frank", "Guide", "Draft", "Exist", "Fraud", "Happy", "Drama", "Extra", "Fresh", "Harry", "Drawn", "Faith", "Front", "Heart", "Dream", "False", "Fruit", "Heavy", "Dress", "Fault", "Fully", "Hence", "Drill", "Fibre", "Funny", "Night", "Drink", "Field", "Giant", "Horse", "Drive", "Fifth", "Given", "Hotel", "Drove", "Fifty", "Glass", "House", "Dying", "Fight", "Globe", "Human", "Eager", "Final", "Going", "Ideal", "Early", "First", "Grace", "Image", "Earth", "Fixed", "Grade", "Index", "Eight", "Flash", "Grand", "Inner", "Elite", "Fleet", "Grant", "Input", "Empty", "Floor", "Grass", "Issue", "Enemy", "Fluid", "Great", "Irony", "Enjoy", "Focus", "Green", "Juice", "Enter", "Force", "Gross", "Joint", "Judge", "Metal", "Media", "Newly", "Known", "Local", "Might", "Noise", "Label", "Logic", "Minor", "North", "Large", "Loose", "Minus", "Noted", "Laser", "Lower", "Mixed", "Novel", "Later", "Lucky", "Model", "Nurse", "Laugh", "Lunch", "Money", "Occur", "Layer", "Lying", "Month", "Ocean", "Learn", "Magic", "Moral", "Offer", "Lease", "Major", "Motor", "Often", "Least", "Maker", "Mount", "Order", "Leave", "March", "Mouse", "Other", "Legal", "Music", "Mouth", "Ought", "Level", "Match", "Movie", "Paint", "Light", "Mayor", "Needs", "Paper", "Limit", "Meant", "Never", "Party", "Peace", "Power", "Radio", "Round", "Panel", "Press", "Raise", "Route", "Phase", 
"Price", "Range", "Royal", "Phone", "Pride", "Rapid", "Rural", "Photo", "Prime", "Ratio", "Scale", "Piece", "Print", "Reach", "Scene", "Pilot", "Prior", "Ready", "Scope", "Pitch", "Prize", "Refer", "Score", "Place", "Proof", "Right", "Sense", "Plain", "Proud", "Rival", "Serve", "Plane", "Prove", "River", "Seven", "Plant", "Queen", "Quick", "Shall", "Plate", "Sixth", "Stand", "Shape", "Point", "Quiet", "Roman", "Share", "Pound", "Quite", "Rough", "Sharp", "Sheet", "Spare", "Style", "Times", "Shelf", "Speak", "Sugar", "Tired", "Shell", "Speed", "Suite", "Title", "Shift", "Spend", "Super", "Today", "Shirt", "Spent", "Sweet", "Topic", "Shock", "Split", "Table", "Total", "Shoot", "Spoke", "Taken", "Touch", "Short", "Sport", "Taste", "Tough", "Shown", "Staff", "Taxes", "Tower", "Sight", "Stage", "Teach", "Track", "Since", "Stake", "Teeth", "Trade", "Sixty", "Start", "Texas", "Treat", "Sized", "State", "Thank", "Trend", "Skill", "Steam", "Theft", "Trial", "Sleep", "Steel", "Their", "Tried", "Slide", "Stick", "Theme", "Tries", "Small", "Still", "There", "Truck", "Smart", "Stock", "These", "Truly", "Smile", "Stone", "Thick", "Trust", "Smith", "Stood", "Thing", "Truth", "Smoke", "Store", "Think", "Twice", "Solid", "Storm", "Third", "Under", "Solve", "Story", "Those", "Undue", "Sorry", "Strip", "Three", "Union", "Sound", "Stuck", "Threw", "Unity", "South", "Study", "Throw", "Until", "Space", "Stuff", "Tight", "Upper", "Upset", "Whole", "Waste", "Wound", "Urban", "Whose", "Watch", "Write", "Usage", "Woman", "Water", "Wrong", "Usual", "Train", "Wheel", "Wrote", "Valid", "World", "Where", "Yield", "Value", "Worry", "Which", "Young", "Video", "Worse", "While", "Youth", "Virus", "Worst", "White", "Worth", "Visit", "Would", "Vital", "Voice"]

    wordle = random.choice(wordle_bank).upper()

    print(_how_to_play())
    print_ui(wordle_board)

    letter_count = {}
    for char in wordle:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1

    attempts_left = 6

    while attempts_left != 0:
        letter_count_copy = letter_count.copy()

        guess = input(f"Guess the 5-letter word. You have {attempts_left} attempts left: ").upper()

        if len(guess) != 5:
            print(color_text("Only 5-letter words are allowed", RED))
            continue

        if not guess.isalpha():
            print(color_text("Your guess must contain only letters of the English alphabet", RED))
            continue

        current_board_row = 6 - attempts_left

        colored_text = ''


        for index, char in enumerate(guess):

            # checking if letter_count_copy[char] is not zero ensures it marks a duplicate char
            # in the guess as wrong if it is not also a duplicate in the wordle.
            if char in wordle and letter_count_copy[char]:
                letter_count_copy[char] -= 1
                if wordle[index] == char:
                    colored_text = color_text(char, GREEN)
                else:
                    colored_text = color_text(char, YELLOW)
            else:
                colored_text = color_text(char, RED)

            wordle_board[current_board_row][index] = colored_text

            for i, row in enumerate(keyboard):
                for j, key in enumerate(row):
                    if key.upper() == char:
                        keyboard[i][j] = colored_text


        print_ui(wordle_board)


        if guess == wordle:
            print(color_text(f"Congratulations! You guessed the wordle correctly. You got {attempts_left} points.", GREEN))
            break

        attempts_left -= 1
    else:
        print(color_text(f"Sorry, you lost. You've run out of chances. The wordle was {color_text(wordle, WHITE)}.", RED))


if __name__ == "__main__":
    main()
