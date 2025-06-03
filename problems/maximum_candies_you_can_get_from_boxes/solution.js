/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
var maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    let totalCandies = 0;
    const queue = [...initialBoxes];
    const owned = new Set(initialBoxes);
    const opened = new Set();
    const hasKey = new Set();

    // To prevent infinite loop on unopenable boxes
    const waitingBoxes = new Set();

    while (queue.length > 0) {
        const box = queue.shift();

        if (opened.has(box)) continue;

        if (status[box] === 1 || hasKey.has(box)) {
            totalCandies += candies[box];
            opened.add(box);

            // Collect keys
            for (let key of keys[box]) {
                if (!hasKey.has(key)) {
                    hasKey.add(key);
                    if (waitingBoxes.has(key)) {
                        queue.push(key);
                        waitingBoxes.delete(key);
                    }
                }
            }

            // Collect contained boxes
            for (let contained of containedBoxes[box]) {
                if (!owned.has(contained)) {
                    owned.add(contained);
                    queue.push(contained);
                } else if ((status[contained] === 1 || hasKey.has(contained)) && !opened.has(contained)) {
                    queue.push(contained);
                } else if (!opened.has(contained)) {
                    waitingBoxes.add(contained);
                }
            }
        } else {
            waitingBoxes.add(box); // wait until we find a key
        }
    }

    return totalCandies;
};
