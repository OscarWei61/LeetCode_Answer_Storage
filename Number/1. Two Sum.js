/*

這段程式碼的時間複雜度是 O(n)，其中 n 是 nums 的長度。

*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {

  map = {};
  for (i = 0; i < nums.length; i++) {
      var v = nums[i];
      if (map[target - v] >= 0) {
          return [map[target - v], i];
      } else {
          map[v] = i;
      }
  }
};