""" This is the nine men in a trench puzzle project

This project is an ai to solve the trench puzzle. 
The trench puzzle is a puzzle where you have 9 people in a trench 
with 13 spaces. The goal is to get all 9 people to their numbered 
spaces in the trench. For example, the sergent is number 1 and 
wishes to place himself at point 1.
    
"""

__version__ = '0.1'
__author__ = 'Anthony Mendez'

from collections import deque
import heapq as heap
import time

from node import Node


def main():
    # Declare variables
    puzzle = [[]]
    node = None
    
    # Display the puzzle name and get the heuristic to use
    puzzle_choice = int(input('Welcome to cs205 9-men in a trench'
                              'puzzle solver. Enter (1) to use a default'
                              'puzzle, or (2) to create your own puzzle.'))
    if puzzle_choice == 1:
        puzzle = create_default_puzzle()
    else:
        puzzle = create_custom_puzzle()
    print('The puzzle you entered is:')
    node = Node(puzzle, None, 0, 0)
    node.print_puzzle()
    heuristic = select_heuristic()
    
    # Begin the ai search to solve the puzzle
    print('Beginning puzzle...')
    time1 = time.perf_counter()
    node = uniform_cost_search(puzzle, heuristic)
    time2 = time.perf_counter()
    print('Puzzle solved in:', '{:.3f}'.format(time2 - time1), 'seconds.')


def uniform_cost_search(puzzle: list[list[int]], heuristic: str) -> Node:
    # Declare variables
    goal_state = [[1], [2], [3], [4, 0], [5], [6, 0], [7], [8, 0], [9], [0]]
    starting_node = Node(puzzle, None, 0, 0)
    working_queue = []
    repeated_states = set()
    heap.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states.add(starting_node.get_hash())
    stack_to_print = []
    
    # Search for the puzzle goal state using uniform cost search
    while working_queue:
        max_queue_size = max(max_queue_size, len(working_queue))
        node = heap.heappop(working_queue)
        repeated_states.add(node.get_hash())
        print('The best state to expand with a g(n) =', node.gn, 'and h(n) =',
              node.hn, 'is...')
        node.print_puzzle()
        
        if node.puzzle == goal_state:
            '''while stack_to_print:
                node = stack_to_print.popleft()
                node.print_puzzle()'''
            print('Goal state reached!')
            print('Depth of goal node:', node.gn)
            print('Number of nodes expanded:', num_nodes_expanded)
            print('Max queue size:', max_queue_size)
            return node
        else:
            stack_to_print.append(node)
            num_nodes_expanded += 1
            for child in node.get_children(heuristic):
                if child.get_hash() not in repeated_states:
                    heap.heappush(working_queue, child)

    print('failure')
    return None


def create_default_puzzle() -> list[list[int]]:
    difficulty = int(input('Select difficulty on a scale of 0 to 5: '))
    if difficulty == 0:
        print('Difficulty 0 selected.')
        return [[1], [2], [3], [4, 0], [5], [6, 0], [7], [8, 0], [9], [0]]
    elif difficulty == 1:
        print('Difficulty 1 selected.')
        return [[1], [2], [3], [4, 0], [5], [0, 0], [0], [6, 8], [7], [9]]
    elif difficulty == 2:
        print('Difficulty 2 selected.')
        return [[0], [0], [0], [0, 1], [2], [3, 5], [4], [6, 8], [7], [9]]
    elif difficulty == 3:
        print('Difficulty 3 selected.')
        return [[2], [3], [5], [6, 4], [0], [0, 1], [0], [0, 8], [7], [9]]
    elif difficulty == 4:
        print('Difficulty 4 selected.')
        return [[2], [3], [5], [6, 4], [8], [9, 7], [0], [0, 0], [0], [1]]
    else:
        print('Difficulty 5 selected.')
        return [[0], [2], [3], [4, 0], [5], [6, 0], [7], [8, 0], [9], [1]]


def create_custom_puzzle():
    puzzle = [[], [], [], [], [], [], [], [], [], []]
    for i in range(10):
        if i == 3 or i == 5 or i == 7:
            print('Enter row', i + 1, 'with 2 numbers separated by a space.')
        else:
            print('Enter row', i + 1, 'with 1 number.')
        row = int(input().split())
        for j in range(len(row)):
            puzzle[i].append(int(row[j]))
    return puzzle


def select_heuristic() -> str:
    choice = int(input('Select algorithm.\n(1) Uniform Cost Search,\n'
                          '(2) misplaced tile,\n(3) manhattan distance: '))
    if choice == 1:
        return 'uniform cost search'
    elif choice == 2:
        return 'misplaced tile'
    else:
        return 'manhattan distance'
    

if __name__ == '__main__':
    main()
