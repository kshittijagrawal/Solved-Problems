# Insert Interval
## Tag
- [ ] Easy
- [x] **Medium**  
- [ ] Hard 
  

## Prompt
Given a set of *non-overlapping* `intervals`, insert a **new interval** into the `intervals` *(merge if necessary)*.  
  
You may assume that the `intervals` were initially **sorted** according to their start times.
  
## Examples
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```
```
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
```
```
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
```
```
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
```
  
## Constraints
* 0 <= **intervals.length** <= 10<sup>4</sup>
* **intervals[i].length** == 2
* 0 <= **intervals[i][0]** <= **intervals[i][1]** <= 10<sup>5</sup>
* **intervals** is sorted by **intervals[i][0]** in ascending order.
* **newInterval.length** == 2
* 0 <= **newInterval[0]** <= **newInterval[1]** <= 10<sup>5</sup>
  
## Complexities
* The **Time Complexity** for the implementation : Linear
  * Runtime : **80 ms**  
* The **Space Complexity** for the implementation : Linear
  * Memory : **17.4 mb**