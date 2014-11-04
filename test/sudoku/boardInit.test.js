var expect = require('chai').expect;
var rewire = require("rewire");
var sinon = require('sinon');
var Sudoku = rewire('../../js/Sudoku');
var boardInit = Sudoku.__get__('boardInit');

describe('getRandomValue', function(){
    it('Should init a blank board when no board template is provided', function(){
        boardInit();
        var board = Sudoku.__get__('board');
        var expectedBoard = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ];
        expect(board.toString()).to.equal(expectedBoard.toString());
    });
    //TODO Add test for a board with a template
});