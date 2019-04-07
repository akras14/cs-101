var MergeSort = (function(){
  "use strict";

  function sort(input){
    var arrayLength = input.length;
    var output;
    if(arrayLength <= 1) { //Nothing to sort, return the array
      return input;
    } else {
      //1. Divide the array in half
      var leftIndex = Math.floor(arrayLength/2);
      var rightIndex = arrayLength - leftIndex;
      var leftPart = input.splice(0, leftIndex);
      var rightPart = input; //Left of from splice operation

      leftPart = sort(leftPart);
      rightPart = sort(rightPart);
      return merge(leftPart, rightPart);
    }
  }

  function merge(left, right) {
    var leftTest, rightTest;
    var outputNeededLength = left.length + right.length;
    var output = [];
    while(output.length < outputNeededLength) {
      if(left[0]) {// If left still has items
        if(right[0]) { //There is a right left, do a comparison
          if( left[0] <  right[0]){
            output.push(left.shift());
          } else {
            output.push(right.shift());
          }
        } else { //No more right left, store the left value
          output.push(left.shift());
        }
      } else if (right[0]) { //No more left items left, store the right item
        output.push(right.shift());
      } else {
        throw new Error("Run out of items to merge, without exiting the function");
      }
    }
    return output;
  }

  function MergeSort(){
    this.input = null; 
  }

  MergeSort.prototype.sort = function(inputCSV){
    if(!inputCSV) {
      throw new Error("Input to sort is required");
    }
    var input = inputCSV.split(",");
    return sort(input);
  };

  return MergeSort;
})();

function sortAndTest(input){
  //1. Sort the string
  var sorter = new MergeSort();
  var sortedString = sorter.sort(input).join();

  //2. Check the result
  var testInput = input.split(',');

  /* TODO
    - Is just sort enough?
    - Is parseInt reliable?
  */
  testInput = testInput.sort(function(a,b){
    a = parseInt(a);
    b = parseInt(b);
    if (a < b) return -1;
    if (a > b) return 1;
    if (a == b) return 0;
  });
  if(testInput.sort().join() != sortedString) {
    throw new Error("Input is not sorted properly " + input);
  } else {
    console.log(sortedString);
  }
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

var test = (function(MergeSort){

  /* TODO
    - Check for need to push things on Stack, doens't seem to be a problem here
    - Check for negative numbers
    - Remove modularizatoin, to make it easier on the reader
  */
  var inputToSort = "3,5,2,1,4,2,5";
  sortAndTest(inputToSort);
  inputToSort = [];
  for(var i=0; i<100000; i++) {
    inputToSort.push(getRandomInt(0, 10000))
  }
  sortAndTest(inputToSort.join());
})(MergeSort);

