class Node:
    def __init__(self, puzzle: list[list[int]], parent=None):
        self.puzzle = puzzle
        self.parent = parent
    
    def get_hash(self) -> str:
        return str(self.puzzle)

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
    