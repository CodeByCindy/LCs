/**
 * @param {string} s
 * @return {boolean}
 */
// var isPalindrome = function(s) {
//     if (!s.length) return true;

//     const alphaNum = filterAlphaNum(s)
//     const reversed = reverse(alphaNum)

//     return alphaNum === reversed
// };

// const filterAlphaNum = ( s, nonAlphaNum = new RegExp('[^a-z0-9]', 'gi')) => s
//     .toLowerCase()
//     .replace(nonAlphaNum, '')

// const reverse = (s) => s
//     .split('')
//     .reverse('')
//     .join('')var isPalindrome = function (s) {
var isPalindrome = function (s) {
    const isAlphaNumeric = c => (c.toLowerCase() >= 'a' && c.toLowerCase() <= 'z') || c >= '0' && c <= '9'

    let left = 0;
    let right = s.length - 1;
    let skipLeft, skipRight = false;
  while (left < right) {
    skipLeft = !isAlphaNumeric(s.charAt(left))
    if (skipLeft) { left++; continue; }

    skipRight = !isAlphaNumeric(s.charAt(right))
    if (skipRight) { right--; continue; }


    if (! (s.charAt(left).toLowerCase() === s.charAt(right).toLowerCase())) return false

    left++
    right--
  }
  return true
};
