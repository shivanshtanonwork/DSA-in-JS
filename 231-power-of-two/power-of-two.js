/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    // using recursion
    // if(n == 1) return true;
    // else if(n < 1 || n % 2 != 0) return false

    // return isPowerOfTwo(n/2)

    // using bitwise AND
    return n > 0 && (n & (n - 1)) === 0
};
