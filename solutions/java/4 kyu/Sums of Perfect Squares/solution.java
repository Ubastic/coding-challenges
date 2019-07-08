public class SumOfSquares {
    
    private static boolean is_square(int n){  
      int sqrt_n = (int)(Math.sqrt(n));  
      return (sqrt_n*sqrt_n == n);  
    }
    
    public static int nSquaresFor(int n) {
      if(is_square(n)) {
          return 1;  
      }
  
      while ((n & 3) == 0){
          n >>= 2;  
      }
      if ((n & 7) == 7){
          return 4;
      }
  
      int sqrt_n = (int)(Math.sqrt(n)); 
      for(int i = 1; i <= sqrt_n; i++){  
          if (is_square(n - i*i)) {
              return 2;
          }
      }  
  
      return 3;  
    }
}