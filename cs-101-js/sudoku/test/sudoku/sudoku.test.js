var expect = require('chai').expect;
var rewire = require("rewire");
var sinon = require('sinon');
var Sudoku = rewire('../../js/sudoku');

describe('Sudoku', function(){
  describe('boardInit', function(){
    it('Should init a blank board when no board template is provided', function(){
        var testSudoku = new Sudoku();
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
        expect(testSudoku.getBoard()).to.eql(expectedBoard);
    });

    it('Should init a board from template, if provided', function(){
        var potentiallyInvalidBoard = [
            [1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,4,5,6,7,8,9,1],
            [5,6,7,8,9,1,2,3,4],
            [8,9,1,2,3,4,5,6,7],
            [3,4,5,6,7,8,9,1,2],
            [6,6,8,9,1,2,3,4,5], //Two 6s
            [9,1,2,3,4,5,6,7,8]
        ];
        var testSudoku = new Sudoku(potentiallyInvalidBoard);
        expect(testSudoku.getBoard()).to.eql(potentiallyInvalidBoard);
    });
  });
});
