# Search in Rotated Sorted Array
## Tag
- [ ] Easy  
- [x] **Medium**  
- [ ] Hard  
  

## Prompt
There is an integer array `nums` sorted in ascending order (with **distinct** values).  
  
Prior to being passed to your function, `nums` is **rotated** at an unknown pivot index `k` **(0 <= k < nums.length)** such that the resulting array is `[nums[k]`, `nums[k+1]`, ..., `nums[n-1]`, `nums[0]`, `nums[1]`, ..., `nums[k-1]]` *(0-indexed)*. For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.  
  
Given the array `nums` **after** the rotation and an integer `target`, return the **index of target** if it is in `nums`, or `-1` if it is not in `nums`.  
  
**Follow up**: **Can you achieve this in O(log n) time complexity?**  
  
## Examples
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
```
Input: nums = [1], target = 0
Output: -1
```
  
## Constraints
* 1 <= **nums.length** <= 5000
* -10<sup>4</sup> <= **nums[i]** <= 10<sup>4</sup>
* All values of **nums** are **unique**.
* **nums** is guaranteed to be rotated at some pivot.
* -10<sup>4</sup> <= **target** <= 10<sup>4</sup>
  
## Complexities
* The **Time Complexity** for the implementation : Log(n)
  * Runtime : **40 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.6 mb**