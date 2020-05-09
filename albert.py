def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new_state = number - action
        if not can_win(new_state):
            return True
        action += 1
    return False




