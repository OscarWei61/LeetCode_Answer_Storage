/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    let totalSum = 0;
    for(var i = 0; i < columnTitle.length; i++){
        totalSum = totalSum + parseInt(pow(columnTitle.length - i - 1) * (columnTitle.charCodeAt(i) - "A".charCodeAt(0) + 1));
    }

    return totalSum;

    function pow(num){
        let plus = 1;
        if (num == 0) {
            return 1;
        }
        while(num > 0) {
            plus = plus * 26;
            num = num - 1;
        }
        return plus;
    }
};