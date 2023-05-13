""" This is the nine men in a trench puzzle project

This project is an ai to solve the trench puzzle. 
The trench puzzle is a puzzle where you have 9 people in a trench 
with 13 spaces. The goal is to get all 9 people to their numbered 
spaces in the trench. For example, the sergent is number 1 and 
wishes to place himself at point 1.
    
"""

__version__ = '0.1'
__author__ = 'Anthony Mendez'

import heapq as heap




def main():
    initial_state = [[0], [2], [3], [4, 0], [5], [6, 0], [7], [8, 0], [9], [1]]
    goal_state = [[1], [2], [3], [4, 0], [5], [6, 0], [7], [8, 0], [9], [0]]
    
    


if __name__ == '__main__':
    main()
