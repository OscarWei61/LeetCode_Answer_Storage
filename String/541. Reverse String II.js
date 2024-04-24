/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {

    const chars = s.split(''); 
    // Convert string to array of characters
    
    for (let i = 0; i < chars.length; i += 2 * k) {
        let start = i;
        let end = Math.min(i + k - 1, chars.length - 1);
        while (start < end) {
            // Swap characters
            const temp = chars[start];
            chars[start] = chars[end];
            chars[end] = temp;
            start = start + 1;
            end = end - 1;
        }
    }

    return chars.join(''); // Convert array back to string
};
