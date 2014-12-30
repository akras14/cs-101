var expect = require('chai').expect;
var rewire = require("rewire");
var sinon = require('sinon');
var Sudoku = rewire('../../js/sudoku');
var getRandomValue = Sudoku.__get__('getRandomValue');

describe('getRandomValue', function(){
    it('Should return a random integer from including first to excluding second parameter', function(){
        var testValues = [0,1,2,3,4,5,6,7,8,9];
        sinon.stub(Math, 'random', function(){ //0 - 0.9 range
            return testValues.pop()/10;
        });
        expect(getRandomValue(0,9)).to.equal(8); //0.9
        expect(getRandomValue(0,9)).to.equal(7); //0.8
        expect(getRandomValue(0,9)).to.equal(6); //0.7
        expect(getRandomValue(0,9)).to.equal(5); //0.6
        expect(getRandomValue(0,9)).to.equal(4); //0.5
        expect(getRandomValue(0,9)).to.equal(3); //0.4
        expect(getRandomValue(0,9)).to.equal(2); //0.3
        expect(getRandomValue(0,9)).to.equal(1); //0.2
        expect(getRandomValue(0,9)).to.equal(0); //0.1
        expect(getRandomValue(0,9)).to.equal(0); //0.0
        expect(getRandomValue(0,9)).to.not.equal(0); //undefined

        Math.random.restore();
    });
});
