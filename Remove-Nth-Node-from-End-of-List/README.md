# Remove Nth Node from the End of List
## Tag
- [ ] Easy  
- [x] **Medium** 
- [ ] Hard  
  

## Prompt
Given the `head` of a linked list, remove the **nth node from the end** of the list and return its head.  
  
**Follow up**: Could you do this in one pass?  
  
## Examples

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

```
Input: head = [1], n = 1
Output: []
```
```
Input: head = [1,2], n = 1
Output: [1]
```
  
## Constraints
* The number of nodes in the list is **sz**.
* 1 <= **sz** <= 30
* 0 <= **Node.val** <= 100
* 1 <= **n** <= **sz**
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **36 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.2 mb**