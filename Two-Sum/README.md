# Two Sum
## Tag
- [x] **Easy**  
- [ ] Medium  
- [ ] Hard  
  

## Prompt
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.  

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice.  

You can return the answer **in any order**.  
  
## Examples
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
  
## Constraints
* 2 <= `nums.length` <= 103
* -109 <= `nums[i]` <= 109
* -109 <= `target` <= 1098
* **Only one valid answer exists**.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **40 ms**  
* The **Space Complexity** for the implementation : Linear
  * Memory : **14.3 mb**
