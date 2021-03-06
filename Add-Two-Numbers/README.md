# Add Two Numbers
## Tag
- [ ] Easy  
- [x] **Medium**  
- [ ] Hard
  

## Prompt
You are given two *non-empty* linked lists representing two *non-negative* integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.  
  
You may assume the two numbers **do not contain any leading zero**, except the number 0 itself.  
  
## Examples

![addtwonumber1](https://user-images.githubusercontent.com/74072261/119883926-b4b3c780-bf4d-11eb-851e-026557260075.jpg)
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```
```
Input: l1 = [0], l2 = [0]
Output: [0]
```
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```
  
## Constraints
* The number of nodes in each linked list is in the range **[1, 100]**.
* 0 <= **Node.val** <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **60 ms**  
* The **Space Complexity** for the implementation : Linear
  * Memory : **14.2 mb**
