# Spiral Matrix
## Tag
- [ ] Easy  
- [x] **Medium**  
- [ ] Hard  
  

## Prompt
Given an `m x n` matrix, return all elements of the matrix in **spiral order**.   
  
## Examples

![spiral1](https://user-images.githubusercontent.com/74072261/119233497-0ff94a80-bb47-11eb-8867-2cc566648f43.jpg)
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

![spiral](https://user-images.githubusercontent.com/74072261/119233500-1687c200-bb47-11eb-9548-43a3c4598e7c.jpg)
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```
  
## Constraints
* **m** == matrix.length
* **n** == matrix[0].length
* 1 <= **m, n** <= 10
* -100 <= **matrix[i][j]** <= 100
  
## Complexities
* The **Time Complexity** for the implementation : Quadratic
  * Runtime : **24 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14 mb**
