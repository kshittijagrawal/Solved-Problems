# Linked List Cycle
## Tag
- [x] **Easy**  
- [ ] Medium 
- [ ] Hard  
  

## Prompt
Given `head`, the **head of a linked list**, determine if the linked list has a *cycle* in it.  
  
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to. **Note that `pos` is not passed as a parameter**.  
  
Return `true` if there is a cycle in the linked list. Otherwise, return `false`.  
  
**Follow up**: Can you solve it using **O(1)** (i.e. constant) **memory**?  
  
## Examples
  
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```
  
## Constraints
* The **number of the nodes** in the list is in the range [0, 10<sup>4</sup>].
* -10<sup>5</sup> <= **Node.val** <= 10<sup>5</sup>
* **pos** is -1 or a valid index in the linked-list.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **50 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **17.2 mb**