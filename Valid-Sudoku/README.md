# Valid Sudoku
## Tag
- [ ] Easy
- [x] **Medium**  
- [ ] Hard 
  

## Prompt
Determine if a **9 x 9** Sudoku board is valid. Only the filled cells need to be validated according to the following rules:  
  
* Each **row** must contain the digits 1-9 *without repetition*.
* Each **column** must contain the digits 1-9 *without repetition*.
* Each of the **nine 3 x 3 sub-boxes** of the grid must contain the digits 1-9 *without repetition*.
  
**Note**:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.
  
## Examples
  
![250px-Sudoku-by-L2G-20050714 svg](https://user-images.githubusercontent.com/74072261/118373718-dddf6a00-b5d5-11eb-838f-076a3e4a8349.png)

```
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
```
```
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
```
  
## Constraints
* **board.length** == 9
* **board[i].length** == 9
* **board[i][j]** is a digit or '.'
  
## Complexities
* The **Time Complexity** for the implementation : Ouadratic
  * Runtime : **100 ms**  
* The **Space Complexity** for the implementation : Linear
  * Memory : **14.3 mb**
