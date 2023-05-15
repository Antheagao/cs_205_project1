import copy

class Node:
    def __init__(self, puzzle: list[list[int]], parent, gn: int, hn: int):
        self.puzzle = puzzle
        self.parent = parent
        self.gn = gn
        self.hn = hn
    
    def __lt__(self, other):
        return (self.gn + self.hn) < (other.gn + other.hn)      
    
    def get_hash(self) -> str:
        return str(self.puzzle)
    
    def get_children(self, heuristic) -> list['Node']:
        children = []
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
                if not self.puzzle[row][col]:
                    for operator in ['down', 'up', 'left', 'right']:
                        if self.can_move_blank(row, col, operator):
                            puzzle_copy = copy.deepcopy(self.puzzle)
                            puzzle_copy = self.move_blank(row, col, operator)
                            child = self.create_child(heuristic, puzzle_copy)
                            children.append(child)
        return children
    
    def misplaced_tile_count(self) -> int:
        misplaced_tiles = 0
        goal_state = [[1], [2], [3], [4, 0], [5], [6, 0], [7], [8, 0], [9], [0]]
        
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
                if self.puzzle[row][col] != goal_state[row][col] and\
                   self.puzzle[row][col] != 0:
                    misplaced_tiles += 1
        return misplaced_tiles
    
    def manhattan_distance(self) -> int:
        distance = 0
        goal_tiles = {
            1: (0, 0), 2: (1, 0), 3: (2, 0),
            4: (3, 0), 5: (4, 0), 6: (5, 0),
            7: (6, 0), 8: (7, 0), 9: (8, 0)
        }
        
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
                tile = self.puzzle[row][col]
                if tile != 0:
                    goal_row, goal_col = goal_tiles[tile]
                    distance += abs(row - goal_row) + abs(col - goal_col)
        return distance
    
    def create_child(self, heuristic: str, puzzle_copy) -> 'Node':
        child = Node(puzzle_copy, self, self.gn + 1, 0)
        if heuristic == 'uniform cost search':
            return child
        elif heuristic == 'misplaced tile':
            child.hn = child.misplaced_tile_count()
            return child
        else:
            child.hn = child.manhattan_distance()
            return child
    
    def can_move_blank(self, row: int, col: int, operator: str) -> bool:
        if operator == 'down':
            return row != len(self.puzzle) - 1 and col == 0
        elif operator == 'up':
            return row > 0 and col == 0
        elif operator == 'left':
            return row in {3, 5, 7} and col > 0
        else:
            return row in {3, 5, 7} and col == 0            
    
    def move_blank(self, row: int, col: int, operator: str) -> list[list[int]]:
        puzzle_copy = copy.deepcopy(self.puzzle)
        if operator == 'down':
            puzzle_copy[row][col], puzzle_copy[row + 1][col] =\
                puzzle_copy[row + 1][col], puzzle_copy[row][col]
        elif operator == 'up':
            puzzle_copy[row][col], puzzle_copy[row - 1][col] =\
                puzzle_copy[row - 1][col], puzzle_copy[row][col]
        elif operator == 'left':
            puzzle_copy[row][col], puzzle_copy[row][col - 1] =\
                puzzle_copy[row][col - 1], puzzle_copy[row][col]
        else:
            puzzle_copy[row][col], puzzle_copy[row][col + 1] =\
                puzzle_copy[row][col + 1], puzzle_copy[row][col]
        return puzzle_copy

    def print_puzzle(self):
        print('|---|')
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
                print('|', end=' ')
                if self.puzzle[row][col]:
                    print(self.puzzle[row][col], end=' ')
                else:
                    print(' ', end=' ')
            print('|')
            if row == 2 or row == 4 or row == 6:
                print('|---|----')
            elif row == 3 or row == 5 or row == 7:
                print('|---|----')
            else:
                print('|---|')
