/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
    if (s.length == 1) {
        return s;
    }

    for (num = 0; num < (s.length / 2); num++) {
        let temp = s[num];
        s[num] = s[s.length - 1 - num];
        s[s.length - 1 - num] = temp;
    }

    return s;
};