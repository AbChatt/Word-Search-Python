""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
    if player_one_turn:
        return P1
    else:
        return P2
    # Complete this function.

def get_winner(player_one_score: int, player_two_score: int) -> str:
    """Returns 'player one wins' if player_one_score > player_two_score,
      'player two wins' if player_one_score < player_two score,
       otherwise returns 'tie game'.
    
    >>> get_winner(4, 1)
    'player one wins'
    
    >>> get_winner(2,2)
    'tie game'
    """
    if player_one_score > player_two_score:
        return P1_WINS
    elif player_one_score < player_two_score:
        return P2_WINS
    else:
        return TIE

def reverse(string1: str) -> str:
    """Returns a reversed copy of the string represented by string1
    
    >>> reverse('abc')
    'cba'
    >>> reverse('winter')
    'retniw'
    """
    return string1[-1::-1]

def get_row(puzzle: str, row_num: int) -> str:
    """Returns the letters in the row corresponding to row_num from puzzle
    
    Precondition: 0 <= row_num < number of rows in puzzle
    
    >>> get_row('abcd\n', 0)
    'abcd'
    >>> get_row('efgh\nijkl\n', 1)
    'ijkl'
    """
    char_num = (row_num * (get_row_length(puzzle) + 1))
    return puzzle[char_num : char_num + get_row_length(puzzle)]
# it works!!!

def get_factor(direction1: str) -> int:
    """Returns the multiplicative factor associated with direction1
    
    >>> get_factor('up')
    4
    >>> get_factor('down')
    2
    """
    if direction1 == UP:
        return UP_FACTOR
    elif direction1 == DOWN:
        return DOWN_FACTOR
    elif direction1 == FORWARD:
        return FORWARD_FACTOR
    else:
        return BACKWARD_FACTOR

def get_points(direction1: str, words_left: int) -> int:
    """Returns the points earned if we were to find a word along direction1.
    words_left represents the number of words left to be found before this guess
    
    >>> get_points('backward', 5)
    15
    >>> get_points('up', 2)
    32
    """
    if words_left >= THRESHOLD:
        return get_factor(direction1) * THRESHOLD
    elif 1 < words_left < THRESHOLD:
        return (2 * THRESHOLD - words_left) * get_factor(direction1)
    else:
        return (2 * THRESHOLD - words_left) * get_factor(direction1) + BONUS

def check_guess(puzzle: str, direction1: str, guessed_word: str, 
                row_column_num: int, words_left: int) -> int:
    """Returns the number of points earned if guessed_word is found at
    row_column_num along direction1. If guessed_word is not at row_column_num,
    returns 0
    
    Precondition: 0 <= row_column_num <= number of rows / columns in puzzle
    
    >>> check_guess('abcd\nefgh\nijkl\n', 'up', 'abcd', 2, 7)
    0
    >>> check_guess('abcd\nefgh\nijkl\n', 'down', 'aei', 1, 5)
    10
    """
    
    if contains(get_row(puzzle, row_column_num), guessed_word):
        return get_points(direction1, words_left)
    elif contains(get_column(puzzle, row_column_num), guessed_word):
        return get_points(direction1, words_left)
    elif contains(reverse(get_row(puzzle, row_column_num)), guessed_word):
        return get_points(direction1, words_left)
    elif contains(reverse(get_column(puzzle, row_column_num)), guessed_word):
        return get_points(direction1, words_left)
    else:
        return 0
# perfection!