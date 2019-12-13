function takeWhile (arr, pred) {
  let new_arr = [];
  for (let i of arr){
	  if (!pred(i))break;
	  new_arr.push(i);
  }
	return new_arr;
}