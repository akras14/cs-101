var checkRows = require('./checkRows');

function checkColumn(board){
  var testStatus, testRow;
  for(var i = 0; i < board.length; i++){
    testRow = getRow(i, board);
    validColumn = checkRows.isRowValid(testRow);
    if(!validColumn){
      return false;
    }
  }
  return true;
}

function getRow(j, board){
  var testRow = [];
  for(var i = 0; i < board.length; i++){
    testRow.push(board[i][j]);
  }
  return testRow;
}

exports.check = checkColumn;