# Set Matrix Zeroes
## Tag
- [ ] Easy  
- [x] **Medium**  
- [ ] Hard  
  

## Prompt
Given an `m x n` matrix. If an element is `0`, set its *entire row and column to 0*. **Do it in-place**.  

**Follow up:**  
* A straight forward solution using *O(mn)* space is probably a bad idea.
* A simple improvement uses *O(m + n)* space, but still not the best solution.
* Could you devise a *constant space* solution?  
  
## Examples
![mat1](https://user-images.githubusercontent.com/74072261/117971280-4cf35f00-b347-11eb-8d85-2d9845542538.jpg)
```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```
  
![mat2](https://user-images.githubusercontent.com/74072261/117971315-57adf400-b347-11eb-9ef7-797541a537ab.jpg)
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```
  
## Constraints
* **m** == matrix.length
* **n** == matrix[0].length
* 1 <= **m, n** <= 200
* -2<sup>31</sup> <= **matrix[i][j]** <= 2<sup>31</sup> - 1 
  
## Complexities
* The **Time Complexity** for the implementation : Quadratic
  * Runtime : **196 ms**  
* The **Space Complexity** for the implementation : Linear
  * Memory : **15 mb**
