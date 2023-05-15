import copy


class Node:
    """ Represents a node in the tree for the 9-men in a trench puzzle
    
    Provides methods to create children nodes, get the hash of the puzzle,
    calculate the heuristics for the puzzle, get the children of the node,
    and perform the operators on the puzzle.
    
    Attributes:
        puzzle (list[list[int]]): The 2d list representing the puzzle.
        parent (Node): The parent node of the current node.
        gn (int): The cost of the path from the root node to the current node.
        hn (int): The estimated cost of the cheapest path from the current node
    """
    
    def __init__(self, puzzle: list[list[int]], parent, gn: int, hn: int):
        """ Initialize the node with the given puzzle, parent, gn, and hn.

        Args:
            puzzle (list[list[int]]): The 2d list representing the puzzle.
            parent (_type_): The parent node of the current node.
            gn (int): The cost of the path from the root to the current node.
            hn (int): The estimated cost of the cheapest path from the current
        """
        self.puzzle = puzzle
        self.parent = parent
        self.gn = gn
        self.hn = hn
    
    def __lt__(self, other):
        """ Compare the current node to another node.

        Args:
            other (_type_): The node to compare to the current node.

        Returns:
            _type_: True if the current node is less than the other node.
        """
        return (self.gn + self.hn) < (other.gn + other.hn)      
    
    def get_hash(self) -> str:
        """ Get the hash of the puzzle.

        Returns:
            str: The string representation of the puzzle.
        """
        return str(self.puzzle)
    
    def get_children(self, heuristic) -> list['Node']:
        """ Get the children of the current node by performing operations.

        Returns:
            _type_: A list of the children of the current node.
        """
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
        """ Get the number of misplaced tiles in the puzzle.

        Returns:
            int: The number of misplaced tiles in the puzzle.
        """
        misplaced_tiles = 0
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
                    if row != goal_row or col != goal_col:
                        misplaced_tiles += 1
        return misplaced_tiles
    
    def manhattan_distance(self) -> int:
        """ Calculate the manhattan distance of the misplaced puzzle tiles.

        Returns:
            int: The total distance of all the misplaced tiles from their goal
        """
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
        """ Create a child node of the current node.

        Args:
            heuristic (str): The heuristic to use to calculate the hn.
            puzzle_copy (_type_): The puzzle to create the child node with.

        Returns:
            Node: The child node of the current node.
        """
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
        """ Check if the blank tile can be moved in the given direction.

        Args:
            row (int): The row of the blank tile.
            col (int): The column of the blank tile.
            operator (str): The direction to move the blank tile.

        Returns:
            bool: True if the blank tile can be moved in the given direction.
        """
        if operator == 'down':
            return row != len(self.puzzle) - 1 and col == 0
        elif operator == 'up':
            return row > 0 and col == 0
        elif operator == 'left':
            return row in {3, 5, 7} and col > 0
        else:
            return row in {3, 5, 7} and col == 0            
    
    def move_blank(self, row: int, col: int, operator: str) -> list[list[int]]:
        """ Move the blank tile in the given direction.

        Args:
            row (int): The row of the blank tile.
            col (int): The column of the blank tile.
            operator (str): The direction to move the blank tile.

        Returns:
            list[list[int]]: The new puzzle with the blank tile moved.
        """
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

    def print_puzzle(self) -> None:
        """ Print the puzzle in a readable format. """
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
