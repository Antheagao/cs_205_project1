""" This is the nine men in a trench puzzle project

This project is an ai to solve the trench puzzle. 
The trench puzzle is a puzzle where you have 9 people in a trench 
with 13 spaces. The goal is to get all 9 people to their numbered 
spaces in the trench. For example, the sergent is number 1 and 
wishes to place himself at point 1.
    
"""

__version__ = '0.1'
__author__ = 'Anthony Mendez'

from collections import defaultdict
import heapq as heap

from node import Node


def main():
    initial_state = [[0], [2], [3], [4, 0], [5], [6, 0], [7], [8, 0], [9], [1]]
    heuristic = ''
    print(len(initial_state))
    print(len(initial_state[0]))
    print(len(initial_state[3]))
    print(len(initial_state) - 1)
    #uniform_cost_search(initial_state, heuristic)


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
        if node.puzzle == goal_state:
            while stack_to_print:
                node = stack_to_print.pop()
                node.print_puzzle()
            print('Number of nodes expanded:', num_nodes_expanded)
            print('Max queue size:', max_queue_size)
            return node
        else:
            stack_to_print.append(node.puzzle)
            for child in node.get_children(heuristic):
                if child.get_hash() not in repeated_states:
                    heap.heappush(working_queue, child)

    return None
    

if __name__ == '__main__':
    main()
