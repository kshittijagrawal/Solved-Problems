# Rotate Image
## Tag
- [ ] Easy  
- [x] **Medium**  
- [ ] Hard  
  

## Prompt
You are given an `n x n` *2D matrix* representing an image, rotate the image by 90 degrees (clockwise).  

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.  
  
## Examples
![mat1](https://user-images.githubusercontent.com/74072261/116137490-3d420c80-a6f1-11eb-9737-cd40882bde6d.jpg)
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```
  
![mat2](https://user-images.githubusercontent.com/74072261/116137530-4c28bf00-a6f1-11eb-85de-e5439c6eb6a7.jpg)
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```
```
Input: matrix = [[1]]
Output: [[1]]
```
```
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
```
  
## Constraints
* `matrix.length` == `n`
* `matrix[i].length` == `n`
* 1 <= `n` <= 20
* -1000 <= `matrix[i][j]` <= 1000 
  
## Complexities
* The **Time Complexity** for the implementation : Quadratic
  * Runtime : **32 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.2 mb**
