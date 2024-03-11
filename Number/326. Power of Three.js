/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {

    return findTripleElement(n);

    function findTripleElement(num) {
        if (num == 1) {
            return true;
        }
        guessNum = 1;
        testNum = 1;
        while (testNum <= num) {
            testNum = 1;
            for (var i = 0; i < guessNum; i++) {
                testNum = testNum * 3;
            }

            if (testNum == num) {
                return true;
            }
            guessNum = guessNum + 1
        }
        return false;
    }
};