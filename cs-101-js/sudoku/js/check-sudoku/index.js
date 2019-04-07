"use strict";
var checkRows = require('./checkRows');
var checkColumns = require('./checkColumns');
var checkSquares = require('./checkSquares');

function checkSudoku(board){
  if(checkRows.check(board)){
    if(checkColumns.check(board)){
      if(checkSquares.check(board)){
        return true;
      }
    }
  }
  return false;
}

exports.check = checkSudoku;