/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    const first = new Array(26).fill(-1);
    const last = new Array(26).fill(-1);
    const aCode = 'a'.charCodeAt(0);
    
    // First and last occurrence of each character
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - aCode;
        if (first[idx] === -1) first[idx] = i;
        last[idx] = i;
    }
    
    let count = 0;
    
    // For each possible middle character, check unique left-right palindromes
    for (let c = 0; c < 26; c++) {
        const left = first[c];
        const right = last[c];
        
        if (left !== -1 && right - left > 1) {
            const seen = new Set();
            for (let i = left + 1; i < right; i++) {
                seen.add(s[i]);
            }
            count += seen.size;
        }
    }

    return count;
};
