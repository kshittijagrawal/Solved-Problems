# Rotate List
## Tag
- [ ] Easy  
- [x] **Medium** 
- [ ] Hard  
  

## Prompt
Given the `head` of a linked list, rotate the list to the right **by k places**.   
  
## Examples

![rotate1](https://user-images.githubusercontent.com/74072261/119411106-82188d80-bd07-11eb-99cb-43b6e78ba8a5.jpg)
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

![roate2](https://user-images.githubusercontent.com/74072261/119411117-8644ab00-bd07-11eb-8658-a6e87b5a7e6a.jpg)
```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```
  
## Constraints
* The **number of nodes** in the list is in the range [0, 500].
* -100 <= **Node.val** <= 100
* 0 <= **k** <= 2 * 10<sup>9</sup>
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **40 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.3 mb**
