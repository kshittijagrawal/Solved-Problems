# Valid Parentheses
## Tag
- [x] **Easy**  
- [ ] Medium  
- [ ] Hard 
  

## Prompt
Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.  
  
An input string is **valid** if:
* Open brackets must be closed by the **same type of brackets**.
* Open brackets must be closed in the **correct order**.
  
## Examples
```
Input: s = "()"
Output: true
```
```
Input: s = "()[]{}"
Output: true
```
```
Input: s = "(]"
Output: false
```
```
Input: s = "([)]"
Output: false
```
```
Input: s = "{[]}"
Output: true
```
  
## Constraints
* 1 <= `s.length` <= 10^4
* `s` consists of parentheses only `'()[]{}'`.
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **44 ms**  
* The **Space Complexity** for the implementation : Constant
  * Memory : **14.2 mb**