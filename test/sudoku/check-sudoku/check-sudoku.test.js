var expect = require('chai').expect;
var rewire = require("rewire");
var sinon = require('sinon');
var checkSudoku = rewire('../../../js/check-sudoku');

describe("check-sudoku", function(){
  it('should return true if sudoku puzzle is valid', function(){
    var testSudoku = [
      [2,6,7,3,4,5,1,9,8],
      [1,8,3,2,9,6,7,4,5],
      [4,5,9,8,7,1,6,3,2],
      [5,7,2,9,6,4,3,8,1],
      [8,4,6,1,3,2,9,5,7],
      [9,3,1,5,8,7,4,2,6],
      [6,1,5,4,2,9,8,7,3],
      [7,9,8,6,5,3,2,1,4],
      [3,2,4,7,1,8,5,6,9]
    ];
    expect(checkSudoku.check(testSudoku)).to.equal(true);
  });

  it('should return false if sudoku puzzle has an invalid row', function(){
    var testSudoku = [
      [2,6,7,2,4,5,1,9,8], //Two 2s
      [1,8,3,2,9,6,7,4,5],
      [4,5,9,8,7,1,6,3,2],
      [5,7,2,9,6,4,3,8,1],
      [8,4,6,1,3,2,9,5,7],
      [9,3,1,5,8,7,4,2,6],
      [6,1,5,4,2,9,8,7,3],
      [7,9,8,6,5,3,2,1,4],
      [3,2,4,7,1,8,5,6,9]
    ];
    expect(checkSudoku.check(testSudoku)).to.equal(false);
  });

  it('should return false if sudoku puzzle has an invalid column', function(){
    var testSudoku = [
      [2,6,7,3,4,5,1,9,8], 
      [1,8,3,2,9,6,7,4,5],
      [4,5,9,8,7,1,6,3,2], //Two
      [5,7,2,8,6,4,3,8,1], //8s
      [8,4,6,1,3,2,9,5,7],
      [9,3,1,5,8,7,4,2,6],
      [6,1,5,4,2,9,8,7,3],
      [7,9,8,6,5,3,2,1,4],
      [3,2,4,7,1,8,5,6,9]
    ];
    expect(checkSudoku.check(testSudoku)).to.equal(false);
  });

  it('should return false if sudoku puzzle has an invalid square', function(){
    var testSudoku = [
      [2,6,7,3,4,5,1,9,8], 
      [1,8,3,2,9,6,7,4,5], //Two 1s
      [4,5,1,8,7,1,6,3,2], //in first square
      [5,7,2,9,6,4,3,8,1], 
      [8,4,6,1,3,2,9,5,7],
      [9,3,0,5,8,7,4,2,6], //0 here, to replace 1
      [6,1,5,4,2,9,8,7,3],
      [7,9,8,6,5,3,2,1,4],
      [3,2,4,7,1,8,5,6,9]
    ];
    expect(checkSudoku.check(testSudoku)).to.equal(false);
  });
});