# Search Insert Position
## Tag
- [x] **Easy**  
- [ ] Medium  
- [ ] Hard  
  

## Prompt
Given a sorted array of distinct integers and a target value, return the index if the `target` is found. If not, return the index where it would be if it were inserted in order.  
  
## Examples
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```
```
Input: nums = [1,3,5,6], target = 0
Output: 0
```
```
Input: nums = [1], target = 0
Output: 0
```
  
## Constraints
* 1 <= `nums.length` <= 10^4
* -10^4 <= `nums[i]` <= 10^4
* `nums` contains distinct values sorted in ascending order.
* -10^4 <= `target` <= 10^4
  
## Complexities
* The **Time Complexity** for the implementation : Log(n)
  * Runtime : **45 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.6 mb**
