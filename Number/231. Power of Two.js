/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function (n) {

    if (n == 1) {
        return true;
    }

    if (n == 0 || n < 0) {
        return false;
    }

    while (n > 3) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            return false;
        }
    }

    if (n % 2 == 0) {
        return true;
    } else {
        return false;
    }
};