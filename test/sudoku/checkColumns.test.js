var expect = require('chai').expect;
var rewire = require("rewire");
var sinon = require('sinon');
var checkColumn = rewire('../../js/checkColumns');

describe('checkRow', function(){

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
        debugger;
        checkColumn.check(testBoard);
        expect(callcount).to.equal(9);
        revert();
    });

    it("should return true if all columns are valid", function(){
        var testBoard = [
            [1,2,3,4,5,6,7,8,9],
            [2,3,4,5,6,7,8,9,1],
            [3,4,5,6,7,8,9,1,2],
            [4,5,6,7,8,9,1,2,3],
            [5,6,7,8,9,1,2,3,4],
            [6,7,8,9,1,2,3,4,5],
            [7,8,9,1,2,3,4,5,6],
            [8,9,1,2,3,4,5,6,7],
            [9,1,2,3,4,5,6,7,8]
        ];
        var testResult = checkColumn.check(testBoard);
        expect(testResult).to.equal(true);
    });

    it("should return false if any of the columns is invalid", function(){

    });
});