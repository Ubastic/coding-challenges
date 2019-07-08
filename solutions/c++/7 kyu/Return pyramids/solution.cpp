std::string pyramid(int n){
  std::string result = "";
  for (int i = 0; i < n; i++){
    result += std::string(n - i - 1, ' ') + "/" + std::string(i * 2 , (i + 1 == n ? '_' : ' ')) + "\\\n";
  }
  
  return result;
}