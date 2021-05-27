# Intersection of Two Linked List
## Tag
- [x] **Easy**  
- [ ] Medium 
- [ ] Hard  
  

## Prompt
Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the **two lists intersect**. If the two linked lists have no intersection at all, *return null*.  
  
For example, the following two linked lists begin to intersect at node c1:  
![160_statement](https://user-images.githubusercontent.com/74072261/119881932-7917fe00-bf4b-11eb-851b-010f37fe1ab0.png)
  
It is **guaranteed** that there are no cycles anywhere in the entire linked structure.  
  
Note that the linked lists **must retain their original structure** after the function returns.  
  
**Follow up**: Could you write a solution that runs in **O(n) time** and use only **O(1) memory**?  
  
## Examples

![160_example_1_1](https://user-images.githubusercontent.com/74072261/119881968-8339fc80-bf4b-11eb-83d6-3d13bf171318.png)
```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
```

![160_example_2](https://user-images.githubusercontent.com/74072261/119881993-89c87400-bf4b-11eb-94ff-3d05d32a2791.png)
```
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
```

![160_example_3](https://user-images.githubusercontent.com/74072261/119882014-8e8d2800-bf4b-11eb-8b59-8441d4dd7071.png)
```
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
```
  
## Constraints
* The number of nodes of **listA** is in the **m**.
* The number of nodes of **listB** is in the **n**.
* 0 <= **m, n** <= 3 * 10<sup>4</sup>
* 1 <= **Node.val** <= 10<sup>5</sup>
* 0 <= **skipA** <= m
* 0 <= **skipB** <= n
* **intersectVal** is 0 if **listA** and **listB** do not intersect.
* **intersectVal** == **listA[skipA + 1]** == **listB[skipB + 1]** if **listA** and **listB** intersect.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **156 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **29.5 mb**
