# Remove Duplicates from Sorted List II
## Tag
- [ ] Easy  
- [x] **Medium** 
- [ ] Hard  
  

## Prompt
Given the `head` of a *sorted linked list*, delete all nodes that have duplicate numbers, leaving **only distinct numbers** from the original list. Return the linked list sorted as well.    
  
## Examples

![linkedlist1](https://user-images.githubusercontent.com/74072261/119411730-8002fe80-bd08-11eb-905e-ab249496b83f.jpg)
```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

![linkedlist2](https://user-images.githubusercontent.com/74072261/119411749-85604900-bd08-11eb-80ee-b406fae4a352.jpg)
```
Input: head = [1,1,1,2,3]
Output: [2,3]
```
  
## Constraints
* The **number of nodes** in the list is in the range [0, 300].
* -100 <= **Node.val** <= 100
* The list is guaranteed to be sorted in ascending order.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **40 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.3 mb**
