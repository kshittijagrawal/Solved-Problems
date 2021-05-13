# Remove Duplicated from Sorted Array II
## Tag
- [ ] Easy  
- [x] **Medium**  
- [ ] Hard
  

## Prompt
Given a sorted array `nums`, remove the duplicates **in-place** such that duplicates appeared **at most twice** and return the new length.  
  
Do not allocate extra space for another array; you must do this by **modifying the input array in-place** with `O(1)` extra memory.   
  
**Clarification**:  
Confused why the returned value is an **integer** but your answer is an **array**?  
  
Note that the input array is passed in *by reference*, which means a modification to the input array will be known to the caller as well.  
  
## Examples
```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.
```
```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
Explanation: Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond the returned length.
```
  
## Constraints
* 1 <= **nums.length** <= 3 * 10<sup>4</sup>
* -10<sup>4</sup> <= **nums[i]** <= 10<sup>4</sup>
* **nums** is sorted in ascending order.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **60 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.3 mb**