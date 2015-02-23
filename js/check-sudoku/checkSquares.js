"use strict";
var checkRows = require('./checkRows');

function checkSquares(board){
  var validSquare, testRow;
  for(var i = 0; i < board.length; i++){
    testRow = convertSquareToRow(i, board);
    validSquare = checkRows.isRowValid(testRow);
    if(!validSquare){
      return false;
    }
  }
  return true;
}

function convertSquareToRow(i, board){
  var row = [];
  var xOffset = Math.floor(i/3);
  var yOffset = i % 3;
  for(var j = 0; j < 3; j++){
    for(var k = 0; k < 3; k++){
      var x = xOffset*3 + k;
      var y = yOffset*3 + j;
      row.push(board[x][y]);
    }
  }
  return row;
}
exports.check = checkSquares;