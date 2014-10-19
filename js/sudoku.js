var Sudoku = (function(){

    /**
     * Private variables
     */
    var board = [];
    var ROW_COUNT = 9;

    /**
     * Constructor function, populates board as an empty 2D array to model sudoku board
     * @constructor
     */
    function Sudoku () {
        for(var i=0; i< ROW_COUNT; i++){
            board.push(new Array(0, 0, 0, 0, 0, 0, 0, 0, 0));
        }
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
    }

    return Sudoku;
})();