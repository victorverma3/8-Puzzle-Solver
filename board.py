#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.

        for r in range(3):
            for c in range(3):
                if digitstr[3*r + c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                self.tiles[r][c] = digitstr[3*r + c]
            

    ### Add your other method definitions below. ###
    
    def __repr__(self):
        ''' returns a string representation of a Board object.'''
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    s += '_ '
                else:
                    s += self.tiles[r][c]
                    s += ' '
            s += '\n'
        return s
    
    def move_blank(self, direction):
        ''' takes as input a string direction that specifies the 
            direction in which the blank should move, and that attempts 
            to modify the contents of the called Board object accordingly.
        '''
        if direction == 'up' or direction == 'down' or direction == 'left' or direction == 'right':
            if direction == 'up':
                blank_r = self.blank_r - 1
                blank_c = self.blank_c
                if blank_r in range(3) and blank_c in range(3):
                    self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r - 1][self.blank_c]
                    self.tiles[self.blank_r - 1][self.blank_c] = '0'
                    self.blank_r = blank_r
                    return True
                else:
                    return False
            if direction == 'left':
                blank_r = self.blank_r
                blank_c = self.blank_c - 1
                if blank_r in range(3) and blank_c in range(3):
                    self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c - 1]
                    self.tiles[self.blank_r][self.blank_c - 1] = '0'
                    self.blank_c = blank_c
                    return True
                else:
                    return False
            if direction == 'right':
                blank_r = self.blank_r
                blank_c = self.blank_c + 1
                if blank_r in range(3) and blank_c in range(3):
                    self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c + 1]
                    self.tiles[self.blank_r][self.blank_c + 1] = '0'
                    self.blank_c = blank_c
                    return True
                else:
                    return False
            if direction == 'down':
                blank_r = self.blank_r + 1
                blank_c = self.blank_c
                if blank_r in range(3) and blank_c in range(3):
                    self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r + 1][self.blank_c]
                    self.tiles[self.blank_r + 1][self.blank_c] = '0'
                    self.blank_r = blank_r
                    return True
                else:
                    return False
        else:
            return False
    
    def digit_string(self):
        ''' returns the string of digits that was used when creating 
            the Board.
        '''
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '_':
                    s += '0'
                else:
                    s += str(self.tiles[r][c])
        return s
    
    def copy(self):
        ''' returns a newly-constructed Board object that is a deep 
            copy of the called object
        '''
        digits = self.digit_string()
        new_board = Board(digits)
        return new_board
    
    def num_misplaced(self):
        ''' counts and returns the number of tiles in the called Board 
            object that are not where they should be in the goal state.
        '''
        count = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != '0':
                    if GOAL_TILES[r][c] != self.tiles[r][c]:
                        count += 1
        return count
    
    def __eq__(self, other):
        ''' return True if the called object (self) and the argument (other)
            have the same values for the tiles attribute, and False otherwise.
        '''
        if self.tiles == other.tiles:
            return True
        else:
            return False