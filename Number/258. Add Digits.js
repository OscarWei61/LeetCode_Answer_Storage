/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function (num) {
    let numString = num.toString();
    if (numString.length == 1) {
        return num;
    }
    let totalSum = 0;
    while (numString.length > 1) {
        totalSum = 0;
        for (var i = 0; i < numString.length; i++) {
            totalSum = totalSum + parseInt(numString[i]);
        }
        numString = totalSum.toString();
    }

    return totalSum;
};