var expect = require('chai').expect;
var rewire = require("rewire");
var sinon = require('sinon');
var checkRows = rewire('../../js/checkRows');

describe('checkRows', function(){

    it("should return true if all rows are valid", function(){
        var testBoard = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ];
        var callCount = 0;
        var revert = checkRows.__set__({
            isRowValid: function(){
                callCount++;
                return true;
            }
        });
        var boardTest = checkRows.check(testBoard);
        expect(boardTest).to.equal(true);
        expect(callCount).to.equal(9);
        revert();
    });

    it("should return false if any of the rows is invalid", function(){
        var testBoard = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ];
        var callCount = 0;
        var revert = checkRows.__set__({
            isRowValid: function(){
                callCount++;
                return false;
            }
        });
        var boardTest = checkRows.check(testBoard);
        expect(boardTest).to.equal(false);
        expect(callCount).to.equal(1);
        revert();
    });

    describe('isRowValid', function(){
        var isRowValid = checkRows.__get__("isRowValid");
        it('Should return false if row has invalid number', function(){
            var testRow = [1,2,3,4,5,6,7,8,10];
            var rowTestResult;

            for(var i = 0; i < testRow.length; i ++) {
                rowTestResult = isRowValid(testRow);
                expect(rowTestResult).to.equal(false);

                testRow.push(testRow.shift()); //Rotate the array
            }
        });

        it('Should return false if row has invalid character', function(){
            var testRow = [1,2,3,4,5,6,7,8,"a"];
            var rowTestResult;
            for(var i = 0; i < testRow.length; i ++) {
                rowTestResult = isRowValid(testRow);
                expect(rowTestResult).to.equal(false);
                testRow.push(testRow.shift()); //Rotate the array
            }
        });

        it('Should treat 0 as a valid entery, representing empty space', function(){
            var testRow = [1,2,3,4,5,6,7,8,0];
            var rowTestResult;

            for(var i = 0; i < testRow.length; i ++) {
                rowTestResult = isRowValid(testRow);
                expect(rowTestResult).to.equal(true);

                testRow.push(testRow.shift()); //Rotate the array
            }
        });

        it('Should return true if row is invalid', function(){
            var testRow = [1,2,3,4,5,6,7,8,9];
            var rowTestResult;
            for(var i = 0; i < testRow.length; i ++) {
                rowTestResult = isRowValid(testRow);
                expect(rowTestResult).to.equal(true);
                testRow.push(testRow.shift()); //Rotate the array
            }
        });
    });
});