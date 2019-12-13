int is_dd(const long n){
  int arr[9] = {0};
  int number = n;
  
  while(number){
    int ost = number % 10;
    
    arr[ost]++;
    number = number / 10;
  }
  
  int i;
  
  for (i = 1; i < 9;i++){
    if (i == arr[i]){
      return 1;
    }
  }
  
  return 0;
}