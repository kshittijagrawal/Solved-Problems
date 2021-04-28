# Find First and Last Position of an Element in Sorted Array
## Tag
- [ ] Easy  
- [x] **Medium**  
- [ ] Hard
  

## Prompt
Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.  
  
If `target` is not found in the array, return `[-1, -1]`.  
  
**Follow up: Could you write an algorithm with `O(log n)` runtime complexity?**  
  
## Examples
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
```
Input: nums = [], target = 0
Output: [-1,-1]
```
  
## Constraints
* 0 <= `nums.length` <= 10^5
* -10^9 <= `nums[i]` <= 10^9
* `nums` is a non-decreasing array.
* -10^9 <= `target` <= 10^9
  
## Complexities
* The **Time Complexity** for the implementation : Log(n)
  * Runtime : **80 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **15.5 mb**