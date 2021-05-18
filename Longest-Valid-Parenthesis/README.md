# Longest Valid Parenthesis
## Tag
- [ ] Easy
- [ ] Medium  
- [x] **Hard** 
  

## Prompt
Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (**well-formed**) parentheses substring.
  
## Examples
```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```
```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```
```
Input: s = ""
Output: 0
```
  
## Constraints
* 0 <= **s.length** <= 3 * 10<sup>4</sup>
* **s[i]** is **'('**, or **')'**.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **44 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.3 mb**