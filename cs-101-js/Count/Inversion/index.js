var invCount = require('./inversion-count');

function run(arr) {
  console.log("Inversion for array");
  console.log(arr);
  console.log(invCount.slowCount(arr));
}

run([1,2,3]);
run([3,2,1]);
run([1,3,5,2,4,6]);
