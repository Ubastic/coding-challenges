int hasDig(int n,int d){
  int count = 0;
  
  if (n == d){
    return 1;
  }
  
  while(n){
    int ost = n % 10;
    
    if (ost == d){
      count += 1;
    }
    n = n / 10;
  }
  
  return count;
}

int nbDig(int n, int d) {
  int count = 0;
  int i;
  printf("%d\n",n);  
  for (i = 0;i <= n;i++){
    count += hasDig(i * i, d);
  }
  
  return count;
}