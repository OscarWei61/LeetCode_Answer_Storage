/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
    var indexNum = 0
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] != val) {
            nums[indexNum] = nums[i];
            indexNum = indexNum + 1;
        }
    }

    for (var i = indexNum; i < nums.length; i++) {
        nums[i] = '_';
    }

    return indexNum
};