/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    const n = s.length;
    const diff = new Array(n + 1).fill(0); // +1 for easier prefix sum

    // Apply shift directions as difference array
    for (const [start, end, dir] of shifts) {
        const delta = dir === 1 ? 1 : -1;
        diff[start] += delta;
        diff[end + 1] -= delta;
    }

    // Compute prefix sum to get net shifts
    const netShifts = new Array(n);
    let currShift = 0;

    for (let i = 0; i < n; i++) {
        currShift += diff[i];
        // Normalize shift in range [0, 26)
        netShifts[i] = ((currShift % 26) + 26) % 26;
    }

    // Apply shifts to the original string
    let result = "";

    for (let i = 0; i < n; i++) {
        const originalCharCode = s.charCodeAt(i) - 97;
        const shiftedCode = (originalCharCode + netShifts[i]) % 26;
        result += String.fromCharCode(shiftedCode + 97);
    }

    return result;
};
