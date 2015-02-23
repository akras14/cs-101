var SUDOKU_SIDE = 9;
var validValues = {
    1: true,
    2: true,
    3: true,
    4: true,
    5: true,
    6: true,
    7: true,
    8: true,
    9: true
};
//Check every row in the board to see if it is valid
function checkRows(board){
    var rowCount = {};
    var currentRowValid;

    for(var i=0; i<SUDOKU_SIDE; i++){
        currentRowValid = isRowValid(board[i]);
        if(!currentRowValid){
            return false;
        }
    }
    //All rows has passed
    return true;
}

function isRowValid(row){
    var valueHit = {};
    for(var i=0; i<SUDOKU_SIDE; i++){
        var testValue = row[i];

        if(!validValues[testValue] && testValue !== 0){ //Value is not valid and not empty
            return false;
        }

        if(valueHit[testValue]){
            return false; //Should only hit each value once
        } else {
            if(testValue !== 0){
                valueHit[testValue] = true; //Store the hit
            }
        }
    }
    return true;
}

exports.check = checkRows;
exports.isRowValid = isRowValid;