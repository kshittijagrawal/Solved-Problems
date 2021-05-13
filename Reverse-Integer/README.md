# Reverse Integer
## Tag
- [x] **Easy**  
- [ ] Medium  
- [ ] Hard  
  

## Prompt
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range **[-2<sup>31</sup>, 2<sup>31</sup> - 1]**, then return `0`.  

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**
  
## Examples
```
Input: x = 123
Output: 321
```
```
Input: x = -123
Output: -321
```
```
Input: x = 120
Output: 21
```
```
Input: x = 0
Output: 0
```
  
## Constraints
* -2<sup>31</sup> <= **x** <= 2<sup>31</sup> - 1  
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **32 ms**  
* The **Space Complexity** for the implementation : Constant (depends on length of the number to be precise.)
  * Memory : **14.1 mb**
