var Sudoku = require('./Sudoku');
var board = new Sudoku();

function show(boardName){
    console.log(boardName.toString());
}

board.randomize();
//while(!board.checkCell(0,0)){
//    board.randomize();
//}
show(board);
console.log(board.checkCell(0,0));