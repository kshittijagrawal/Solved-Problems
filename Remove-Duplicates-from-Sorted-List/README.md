# Remove Duplicates from Sorted List
## Tag
- [x] **Easy**  
- [ ] Medium 
- [ ] Hard  
  

## Prompt
Given the `head` of a sorted **linked list**, delete all duplicates such that each element **appears only once**. *Return the linked list sorted as well*.  
      
## Examples

![list1](https://user-images.githubusercontent.com/74072261/119388956-95683080-bce8-11eb-9bef-bead94e6a05b.jpg)
```
Input: head = [1,1,2]
Output: [1,2]
```

![list2](https://user-images.githubusercontent.com/74072261/119388970-9ac57b00-bce8-11eb-9180-b4d852476c64.jpg)
```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```
  
## Constraints
* The **number of nodes** in the list is in the range [0, 300].
* -100 <= **Node.val** <= 100
* The list is guaranteed to be sorted in ascending order.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **36 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.2 mb**
