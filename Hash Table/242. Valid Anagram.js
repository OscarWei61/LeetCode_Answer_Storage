/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {

    if (s.length !== t.length) {
        return false;
    }

    const char_freq = {};

    for (let char of s) {
        if (char_freq[char] === undefined) {
            char_freq[char] = 1;
        } else {
            char_freq[char] = char_freq[char] + 1;
        }
    }

    for (let char of t) {
        if (char_freq[char] === undefined || char_freq[char] === 0) {
            return false;
        }
        char_freq[char] = char_freq[char] - 1;
    }

    return true;
};