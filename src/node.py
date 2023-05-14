import copy

class Node:
    def __init__(self, puzzle: list[list[int]], parent, gn: int, hn: int):
        self.puzzle = puzzle
        self.parent = parent
        self.gn = gn
        self.hn = hn
        self.operators = ['up', 'down', 'left', 'right']
    
    def __lt__(self, other):
        return (self.gn + self.hn) < (other.gn + other.hn)      
    
    def get_hash(self) -> str:
        return str(self.puzzle)
    
    def get_children(self, heuristic) -> list['Node']:
        children = []
        if heuristic == 'uniform cost search':
            for row in range(len(self.puzzle)):
                for col in range(len(self.puzzle[row])):
                    if not self.puzzle[row][col]:
                        # Check if blank can move down
                        if self.can_move_blank_down(row, col):
                            puzzle_copy = copy.deepcopy(self.puzzle)
                            puzzle_copy[row][col] = puzzle_copy[row + 1][col]
                            puzzle_copy[row + 1][col] = 0
                            child = Node(puzzle_copy, self, self.gn + 1, 0)
                            children.append(child)
                        # Check if blank can move up
                        elif self.can_move_blank_up(row, col):
                            puzzle_copy = copy.deepcopy(self.puzzle)
                            puzzle_copy[row][col] = puzzle_copy[row - 1][col]
                            puzzle_copy[row - 1][col] = 0
                            child = Node(puzzle_copy, self, self.gn + 1, 0)
                            children.append(child)
                        # Check if blank can move left
                        elif self.can_move_blank_left(row, col):
                            puzzle_copy = copy.deepcopy(self.puzzle)
                            puzzle_copy[row][col] = puzzle_copy[row][col - 1]
                            puzzle_copy[row][col - 1] = 0
                            child = Node(puzzle_copy, self, self.gn + 1, 0)
                            children.append(child)
                        # Check if blank can move right
                        elif self.can_move_blank_right(row, col):
                            puzzle_copy = copy.deepcopy(self.puzzle)
                            puzzle_copy[row][col] = puzzle_copy[row][col + 1]
                            puzzle_copy[row][col + 1] = 0
                            child = Node(puzzle_copy, self, self.gn + 1, 0)
                            children.append(child)                    
        elif heuristic == 'misplaced tile':
            dum1 = None
        else:
            dum2 = None
        
        return children
    
    def can_move_blank_down(self, row: int, col: int) -> bool:
        return (row >= 0) and (col == 0) and\
               (row < len(self.puzzle) - 1) and\
               (self.puzzle[row + 1][col])
               
    def can_move_blank_up(self, row: int, col: int) -> bool:
        return (row > 0) and (row <= len(self.puzzle) - 1) and\
               (col == 0) and (self.puzzle[row - 1][col])
       
    def can_move_blank_left(self, row: int, col: int) -> bool:
        return (row == 3 or row == 5 or row == 7) and\
               (col > 0) and (self.puzzle[row][col - 1]) 
                 
    def can_move_blank_right(self, row: int, col: int) -> bool:
        return (row == 3 or row == 5 or row == 7) and\
               (col == 0) and (self.puzzle[row][col + 1])   

    def print_puzzle(self):
        print('|---|')
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
                print('|', end=' ')
                if len(self.puzzle[row]) == 1 and self.puzzle[row][col] :
                    print(self.puzzle[row][0], '|')
                    if row == 2 or row == 4 or row == 6:
                        print('|---|----')
                    else:
                        print('|---|')
                elif len(self.puzzle[row]) == 1 and not self.puzzle[row][col]:
                    print(' ', '|')
                    print('|---|')
                elif len(self.puzzle[row]) > 1 and self.puzzle[row][col]:
                    print(self.puzzle[row][col], end=' ')
                    if col == len(self.puzzle[row]) - 1:
                        print('|')
                        if row == 3 or row == 5 or row == 7:
                            print('|---|----')
                        else:
                            print('|---|')
                else:
                    print(' ', end=' ')
                    if col == len(self.puzzle[row]) - 1:
                        print('|')
                        if row == 3 or row == 5 or row == 7:
                            print('|---|----')
                        else:
                            print('|---|')
        