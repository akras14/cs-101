var board = new Sudoku();

function show(boardName){
    console.log(boardName.toString());
}

show(board);
board.randomizeBoard();
show(board);
board.clear().randomizeBoard();
show(board);
board.clear();
show(board);