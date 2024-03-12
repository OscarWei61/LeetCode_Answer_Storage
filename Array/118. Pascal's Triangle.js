/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {

    if (numRows == 0) {
        return [];
    }

    rootRows = [[1]];
    for (var i = 1; i < numRows; i++) {
        prevRow = rootRows[i - 1]
        currentRow = [1];

        for (var ii = 1; ii <= i; ii++) {
            // 每一列的第n個值都是 前一列[n-1] + [n]
            var pre_item = prevRow[ii - 1];
            var cur_item = prevRow[ii] ? prevRow[ii] : 0;
            currentRow.push(pre_item + cur_item);
        }
        rootRows.push(currentRow)
    }

    return rootRows;
};