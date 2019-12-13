bool valid_braces(std::string braces) 
{
  std::string all_braces = "(){}[]";
  std::string stack = "";
  
  for (auto c : braces){  
  {    
      std::cout << c << std::endl;
      if (all_braces.find(c) != std::string::npos)
      {
        if (all_braces.find(c) % 2 == 0){
          stack += c;
        }else{
          if (all_braces.find(c) - all_braces.find(stack.back()) != 1){
            return false;
          }
          stack.pop_back();
        }
      }
    }
   }
 return stack.empty();
}