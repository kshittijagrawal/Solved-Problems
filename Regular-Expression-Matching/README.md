# Regular Expression Matching
## Tag
- [ ] Easy  
- [ ] Medium  
- [x] **Hard**  
  

## Prompt
Given an input string `(s)` and a pattern `(p)`, implement regular expression matching with support for `'.'` and `'*'` where:  
* `'.'` Matches any **single character**.​​​​
* `'*'` Matches **zero or more of the preceding element**.  
 
The matching **should cover the entire input string** (not partial).  
  
## Examples
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```
```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```
```
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
```
```
Input: s = "mississippi", p = "mis*is*p*."
Output: false
```
  
## Constraints
* 0 <= **s.length** <= 20
* 0 <= **p.length** <= 30
* s contains **only lowercase** English letters.
* p contains **only lowercase** English letters, **'.'**, and **'*'**.
* It is guaranteed for each appearance of the character **'*'**, **there will be a previous valid character to match**.
  
## Complexities
* The **Time Complexity** for the implementation : Unbound (since here we're using **regex**)
  * Runtime : **60 ms**  
* The **Space Complexity** for the implementation : Linear
  * Memory : **14.2 mb**
