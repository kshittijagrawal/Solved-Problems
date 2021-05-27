# Remove Linked List Elements
## Tag
- [x] **Easy**  
- [ ] Medium  
- [ ] Hard
  

## Prompt
Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has **Node.val == val**, and return the new head.  
  
## Examples

![removelinked-list](https://user-images.githubusercontent.com/74072261/119882937-9b5e4b80-bf4c-11eb-8837-eb4eed60e197.jpg)
```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```
```
Input: head = [], val = 1
Output: []
```
```
Input: head = [7,7,7,7], val = 7
Output: []
```
  
## Constraints
* The number of nodes in the list is in the range **[0, 10<sup>4</sup>]**.
* 1 <= **Node.val** <= 50
* 0 <= **k** <= 50
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **68 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **17.2 mb**
