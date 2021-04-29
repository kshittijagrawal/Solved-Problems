# Remove Duplicated from Sorted Array
## Tag
- [x] **Easy**  
- [ ] Medium  
- [ ] Hard
  

## Prompt
Given a sorted array `nums`, remove the duplicates **in-place** such that each element appears **only once** and returns the new length.  
  
Do not allocate extra space for another array, you must do this by **modifying the input array in-place** with `O(1)` extra memory.   
  
**Clarification**:  
Confused why the returned value is an **integer** but your answer is an **array**?  
  
Note that the input array is passed in *by reference*, which means a modification to the input array will be known to the caller as well.  
  
## Examples
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
```
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
```
  
## Constraints
* 0 <= `nums.length` <= 3 * 10^4
* -10^4 <= `nums[i]` <= 10^4
* `nums` is sorted in ascending order.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **84 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **15.6 mb**