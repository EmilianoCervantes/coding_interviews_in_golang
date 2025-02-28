"""
LEETCODE PROBLEM #36

Description Directly from: https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        There are 3 things we need to check
        Let's divide the problem by each scenario
        """

        # Scenario 1) Numbers must not repeat between rows
        for row in board:
            row_set = set()
            for value in row:
                if value != ".":
                    number = int(value)
                    if number in row_set:
                        return False
                    row_set.add(number)
        
        # Scenario 2: numbers must not repeat between columns
        for col in range(9):
            col_set = set()
            for row in board:
                if row[col] != ".":
                    number = int(row[col])
                    if number in col_set:
                        return False
                    col_set.add(number)
    
        # Scenario 3: numbers must not repeat between grids
        grids = [set() for _ in range(9)] # Instead of set0, set1, etc.
        for r, row in enumerate(board):
            for col in range(9):
                if row[col] != ".":
                    # Using // To avoid x.0f and get just get x
                    grid_index = r // 3 * 3 + col // 3

                    if row[col] in grids[grid_index]:
                        return False
                    grids[grid_index].add(row[col])
        return True
s = Solution()

board = [
    ["5","3",".",   ".","7",".",    ".",".","."],
    ["6",".",".",   "1","9","5",    ".",".","."],
    [".","9","8",   ".",".",".",    ".","6","."],

    ["8",".",".",   ".","6",".",    ".",".","3"],
    ["4",".",".",   "8",".","3",    ".",".","1"],
    ["7",".",".",   ".","2",".",    ".",".","6"],

    [".","6",".",   ".",".",".",    "2","8","."],
    [".",".",".",   "4","1","9",    ".",".","5"],
    [".",".",".",   ".","8",".",    ".","7","9"]
    ]
print(f"s.isValidSudoku({board}): {s.isValidSudoku(board)}")

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

print(f"s.isValidSudoku({board}): {s.isValidSudoku(board)}")