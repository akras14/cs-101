exports.slowCount = function(arr){
  var inversionCount =0;
  for(var i=0; i<arr.length; i++){
    for(var j=i+1; j<arr.length; j++){
      if(arr[i] > arr[j]){
        console.log("[%s,%s]", arr[i], arr[j]);
        inversionCount++;
      }
    }
  }
  return inversionCount;
};