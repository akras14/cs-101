// Private variables
var board;
var SUDOKU_SIDE = 9;

// Private methods

/**
 * Initialize an empty board or pre-populate board from template
 * @param boardTemplate {Array} optional
 */
function boardInit(boardTemplate){
    if(!boardTemplate){
        board = [];
        for(var i=0; i< SUDOKU_SIDE; i++){
            var row = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0);
            board.push(row);
        }
    } else {
        board = boardTemplate;
    }
}

/**
 * Constructor function, populates board as an empty 2D array to model sudoku board
 * @constructor
 */
function Sudoku (boardTemplate) {
    boardInit(boardTemplate);
    return this;
}

/**
 * Returns current state of the board as a string
 * @returns {string}
 */
Sudoku.prototype.toString = function(){
    var row = "";
    for (var i=0; i < SUDOKU_SIDE; i++){
        for(var j=0; j < SUDOKU_SIDE; j++){
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


module.exports = Sudoku;