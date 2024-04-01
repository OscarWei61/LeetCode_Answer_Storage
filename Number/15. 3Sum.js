/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {

    // only three nums input
    if (nums.length == 3) {
        if ((nums[0] + nums[1] + nums[2]) != 0) {
            return [];
        } else {
            return [nums];
        }
    }

    // more than three numbers input
    nums.sort((a, b) => a - b); // Sort the array in ascending order
    const result = [];

    for (i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        } else {
            let pointer_left = i + 1;
            let pointer_right = nums.length - 1;
            while (pointer_left < pointer_right) {
                if (nums[i] + nums[pointer_left] + nums[pointer_right] == 0) {
                    result.push([nums[i], nums[pointer_left], nums[pointer_right]]);
                    while (true) {
                        if ((nums[pointer_left] == nums[pointer_left + 1]) && pointer_left < pointer_right) {
                            pointer_left = pointer_left + 1;
                        } else {
                            break;
                        }
                    }

                    while (true) {
                        if ((nums[pointer_right] == nums[pointer_right - 1]) && pointer_left < pointer_right) {
                            pointer_right = pointer_right - 1;
                        } else {
                            break;
                        }
                    }

                    pointer_left = pointer_left + 1;
                    pointer_right = pointer_right - 1;

                } else {
                    if ((nums[i] + nums[pointer_left] + nums[pointer_right]) < 0) {
                        pointer_left = pointer_left + 1;
                    } else {
                        pointer_right = pointer_right - 1;
                    }
                }

            }
        }
    }

    return result;
};