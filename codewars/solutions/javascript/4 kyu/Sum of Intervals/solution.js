let sumIntervals = intervals => {
  let values = new Set();
  for (let [start, end] of intervals){
    for (let i = start; i < end; i++){
      values.add(i);
    }
  }
  return values.size;
}