var expect = require('chai').expect;
var rewire = require("rewire");
var sinon = require('sinon');
var checkColumn = rewire('../../../js/check-sudoku/checkColumns');

describe('checkColumns', function(){

    it("should convert a column to a row, and call checkRow with it", function(){
        var callcount = 0;
        var testBoard = [
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9]
        ];
        var revert = checkColumn.__set__({
            checkRows: {
                isRowValid: function(row){
                    callcount++;
                    var expectedResult = [1,1,1,1,1,1,1,1,1].map(function(value){
                        return value * callcount;
                    });
                    expect(row).to.eql(expectedResult);

                    return true;
                }
            }
        });
        checkColumn.check(testBoard);
        expect(callcount).to.equal(9);
        revert();
    });

    it("should return true if all columns are valid", function(){
        var testBoard = [
            [1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,4,5,6,7,8,9,1],
            [5,6,7,8,9,1,2,3,4],
            [8,9,1,2,3,4,5,6,7],
            [3,4,5,6,7,8,9,1,2],
            [6,7,8,9,1,2,3,4,5],
            [9,1,2,3,4,5,6,7,8]
        ];
        var testResult = checkColumn.check(testBoard);
        expect(testResult).to.equal(true);
    });

    it("should return false if any of the columns is invalid", function(){
        var testBoard = [
            [1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,4,5,6,7,8,9,1],
            [5,6,7,8,9,1,2,3,4],
            [8,9,1,2,3,4,5,6,7],
            [3,4,5,6,7,8,9,1,2],
            [9,7,8,9,1,2,3,4,5],// Two
            [9,1,2,3,4,5,6,7,8] // 9s
        ];
        var testResult = checkColumn.check(testBoard);
        expect(testResult).to.equal(false);
    });
});