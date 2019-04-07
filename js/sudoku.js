"use strict";
// Private variables
var SUDOKU_SIDE = 9;

// Private methods

// Initialize an empty board or pre-populate board from template
// @param boardTemplate {Array} optional
function boardInit(){
  var board = [];
  for(var i=0; i< SUDOKU_SIDE; i++){
      var row = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0);
      board.push(row);
  }
  return board;
}

// Constructor function, populates board as an empty 2D array to model sudoku board
// @constructor
function Sudoku (boardTemplate) {
  if(!boardTemplate){
      this.board = boardInit();
  } else {
      this.board = boardTemplate;
  }
  return this;
}


// Returns current board
Sudoku.prototype.getBoard = function(){
  return this.board;
};

// Returns current state of the board as a string
// @returns {string}
Sudoku.prototype.toString = function(){
  var row = "";
  for (var i=0; i < SUDOKU_SIDE; i++){
      for(var j=0; j < SUDOKU_SIDE; j++){
          row += this.board[i][j] + " ";
      }
      row += "\n";
  }
  return row;
};


// Clear the board
Sudoku.prototype.clear = function(){
  this.board = boardInit();
  return this;
};


module.exports = Sudoku;