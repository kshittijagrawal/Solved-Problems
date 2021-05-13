# Search a 2D Matrix
## Tag
- [ ] Easy
- [x] **Medium**  
- [ ] Hard
  

## Prompt
Write an efficient algorithm that searches for a value in an `m x n` matrix. This matrix has the following properties:  
  
* Integers in each row are **sorted** from **left to right**.
* The first integer of each row is **greater** than the last integer of the previous row.  
  
## Examples
![mat1](https://user-images.githubusercontent.com/74072261/118129792-3ec24300-b41a-11eb-864d-26c245407e88.jpg)
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```
  
![mat2](https://user-images.githubusercontent.com/74072261/118129817-48e44180-b41a-11eb-916f-0e13df70b682.jpg)
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```
  
## Constraints
* **m** == matrix.length
* **n** == matrix[i].length
* 1 <= **m, n** <= 100
* -10<sup>4</sup> <= **matrix[i][j], target** <= 10<sup>4</sup>.
  
## Complexities
* The **Time Complexity** for the implementation : nLogn
  * Runtime : **40 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.7 mb**
