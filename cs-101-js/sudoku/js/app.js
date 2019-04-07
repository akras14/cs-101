"use strict";
var Sudoku = require('./sudoku');
var board = new Sudoku();

function show(boardName){
    console.log(boardName.toString());
}

show(board);
