/**
 * Get random value between and including min and up to but excluding max
 * @returns {number}
 */
function getRandomValue(min, max){
    return Math.floor(Math.random() * (max-min)) + min;
}

module.exports = exports = getRandomValue;