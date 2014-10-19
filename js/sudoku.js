var Sudoku = (function(){

    /////////////////////
    // Private variables
    /////////////////////
    var board;
    var ROW_COUNT = 9;

    /////////////////////
    // Private methods
    /////////////////////

    /**
     * Re-initialize an empty board
     */
    function boardInit(){
        board = [];
        for(var i=0; i< ROW_COUNT; i++){
            var row = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0);
            board.push(row);
        }
    }

    /**
     * Get random value between 1 and 9
     * @returns {number}
     */
    function getRandomValue(){
        return Math.floor(Math.random()*9) + 1; //0-8 + 1
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
    Sudoku.prototype.randomizeBoard = function(){
        for (var i=0; i<ROW_COUNT; i++){
            for(var j=0; j<ROW_COUNT; j++){
                var rand = getRandomValue();
                board[i][j] = rand;
            }
        }
        return this;
    };

    return Sudoku;
})();