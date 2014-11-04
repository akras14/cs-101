/////////////////////
// Private variables
/////////////////////
var board;
var ROW_COUNT = 9;

/////////////////////
// Private methods
/////////////////////

/**
 * Initialize an empty board or pre-populate board from template
 * @param boardTemplate {Array} optional
 */
function boardInit(boardTemplate){
    if(!boardTemplate){
        board = [];
        for(var i=0; i< ROW_COUNT; i++){
            var row = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0);
            board.push(row);
        }
    } else {
        board = boardTemplate;
    }
}

/**
 * Get random value between and including min and up to but excluding max
 * @returns {number}
 */
function getRandomValue(min, max){
    return Math.floor(Math.random() * (max-min)) + min;
}

/**
 * Constructor function, populates board as an empty 2D array to model sudoku board
 * @constructor
 */
function Sudoku () {
    boardInit();
    return this;
}

/**
 * Returns current state of the board as a string
 * @returns {string}
 */
Sudoku.prototype.toString = function(){
    var row = "";
    for (var i=0; i < ROW_COUNT; i++){
        for(var j=0; j < ROW_COUNT; j++){
            row += board[i][j] + " ";
        }
        row += "\n";
    }
    return row;
};

/**
 * Clear the board
 */
Sudoku.prototype.clear = function(){
    boardInit();
    return this;
};

/**
 * Populate the board with random values
 */
//TODO factor out into module and test
Sudoku.prototype.randomize = function(){
    for (var i=0; i<ROW_COUNT; i++){
        var randomValue = [1,2,3,4,5,6,7,8,9];
        for(var j=0; j<ROW_COUNT; j++){
            var randomIndex = getRandomValue(0, randomValue.length);
            board[i][j] = randomValue.splice(randomIndex, 1)[0];
        }
    }
    return this;
};


Sudoku.prototype.checkCell = function(cellRow, cellColumn){
    var rowCount = {};
    var columnCount = {};
    var squareCount = {};

    for(var i=0; i<ROW_COUNT; i++){

        var columnValue = board[i][cellColumn];
        var rowValue = board[cellRow][i];

        var xSquare = i % 3;
        var ySquare = Math.floor(i/3);
        var squareValue = board[xSquare][ySquare];

        if(!columnCount[columnValue]) {
            columnCount[columnValue] = 1;
        } else {
            return false;
        }

        if(!rowCount[rowValue]){
            rowCount[rowValue] = 1;
        } else {
            return false;
        }

        //TODO fix square check
        if(!squareCount[squareValue]){
            rowCount[squareValue] = 1;
        } else {
            return false;
        }

    }

    return true;
};


module.exports = Sudoku;