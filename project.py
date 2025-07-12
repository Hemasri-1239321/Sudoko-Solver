import copy
import numpy as np
from random import choice, randint

def main():
    original_puzzle=create_board()
    puzzle=copy.deepcopy(original_puzzle)
    print(np.matrix(puzzle))
    while not solved(puzzle):
        while True:
            row=input("Enter the row number: ")
            if not validate_input(row, "coord"):
                print("Invalid input")
                continue
            col = input("Enter column number: ")
            if not validate_input(col, "coord"):
                print("Invalid input")
                continue
            if original_puzzle[int(row) - 1][int(col) - 1] !=0:
                print("Value can't be changed")
                continue
            break
        while True:
            val = input("Enter value: ")
            if not validate_input(val, "value"):
                print("Invalid input")
                continue
            break
        puzzle[int(row)-1][int(col)-1]=int(val)
        print(np.matrix(puzzle))
    if correct(puzzle):
        print("You solved it!")
    else:
        print("Incorrect Solution. Nice try, maybe next time!")
        solution = input("Would you like to see the solution?(y/n)")
        if solution.lower() == "y" or solution.lower() == "yes":
            print(np.matrix(fill_grid(original_puzzle)))

def create_board():
    numlist=[1,2,3,4,5,6,7,8,9]
    grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    for i in range(0,3):
        possible_nums=numlist.copy()
        start = i*3;
        end = start+3
        for row in range(start,end):
            for col in range(start,end):
                num=choice(possible_nums)
                grid[row][col]=num
                possible_nums.remove(num)
        grid = fill_grid(grid)

        removed_square=randint(40,55)
        for i in range(0, removed_square):
            while True:
                row=randint(0,8)
                col=randint(0,8)
                if grid[row][col] != 0:
                    grid[row][col] = 0
                    break
        return grid
    
def fill_grid(grid):
    row,col = find_next_empty(grid)
    for i in range (1,10):
        if possible(row,col,i,grid):
            grid[row][col] = i
            if solve(grid):
                return grid
        grid[row][col] = 0
    return None

def solve(grid):
    row , col= find_next_empty(grid)
    if row is None and col is None:
        return True
    
    for i in range(1,10):
        if possible(row,col,i,grid):
            grid[row][col] = i
            if solve(grid):
                return True
        grid[row][col] = 0
    return False

def possible(row,column,num,grid):
    for i in range(0,9):
        if grid[row][i] == num:
            return False
        
    for i in range(0,9):
        if grid[i][column] == num:
            return False
        
    x0 = (column//3) * 3
    y0 = (row//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == num:
                return False
    return True

def find_next_empty(grid):
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                return (row,column)
    return (None,None)

def validate_input(input,type):
    try:
        input=int(input)
    except ValueError:
        return False
    if type== "coord":
        if input<1 or input>9:
            return False
    elif type=="value":
        if input<1 or input>9:
            return False
    else:
        return False
    return True

def correct(grid):
    for row in grid:
        check_row = set(row)
        if len(check_row)!=9:
            return False
        
    for col in range(0,9):
        check_col=[]
        for row in range(0,9):
            check_col.append(grid[row][col])
        check_col=set(check_col)
        if len(check_col) !=9:
            return False
        
    for i in range(0,9,3):
        check_square=[]
        for i in range(0,3):
            for j in range(0,3):
                check_square.append(grid[i][j])
        check_square = set(check_square)
        if len(check_square) !=9:
            return False
    return True

def solved(grid):
    row,col=find_next_empty(grid)
    if row is None and col is None:
        return True
    return False

if __name__ == "__main__":
    main()
            
            
        


