# Pow(x,n)
## Tag
- [x] **Easy**  
- [ ] Medium  
- [ ] Hard  
  

## Prompt
Given an integer `x`, return `true` if `x` is palindrome integer.  
  
An integer is a palindrome **when it reads the same backward as forward**. For example, **121 is palindrome while 123 is not**.  
      
## Examples
```
Input: x = 121
Output: true
```
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```
```
Input: x = -101
Output: false
```
  
## Constraints
* -2^31 <= `x` <= 2^31 - 1
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **60 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.1 mb**