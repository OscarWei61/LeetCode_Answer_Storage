/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    indexNum = 0;
    for (var i = 0; i < nums.length; i++) {
        if (nums[indexNum] != nums[i]) {
            indexNum = indexNum + 1;
            nums[indexNum] = nums[i];
        }
    }

    // indexNum是指index的位置，return時是return長度，因此需要 + 1
    return indexNum + 1;
};