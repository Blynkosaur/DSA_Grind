/*class Solution {
    public int check(int x){
        int size = 0;
        int divider = 10;
        while(true){
            if(x%divider == x){
                break;
            }else{
                size++;
            }
        }
        return size;
    }
    public int reverse(int x) {
        int reverse = 0;
        int divider = 10;
        boolean flag = false;
        boolean negative = false;
        if (x<0){
            x = x*-1;
            negative = true;
        }
        while(!flag){
            
            if(x%divider == x){
                flag = true;
            }else{
                divider = divider *10;
                
            }
        }
        int digit = divider/10;
        for (int toDivide =10; toDivide<= divider; toDivide = toDivide *10){
            int toAdd = Integer.parseInt(String.valueOf(String.valueOf(x%toDivide).charAt(0)));
            reverse = reverse+ toAdd*digit;
            
            digit = digit/10;
        }
        if (negative == true){
            reverse = reverse * -1;
        }
        System.out.print(check(30));
        return reverse;    
            
            
            
            
            
        
        
    }     
    

    
}*/
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}