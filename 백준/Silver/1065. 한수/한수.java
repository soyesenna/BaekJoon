import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        
        if (N < 100) {
            System.out.println(N);
            System.exit(0);
        }
        
        int result = 99;
        
        for (int i = 100; i <= N; i++){
            String strNum = String.valueOf(i);
            int diff = strNum.charAt(0) - strNum.charAt(1);
            
            result++;
            for (int j = 0; j < strNum.length() - 1; j++){
                if (strNum.charAt(j) - strNum.charAt(j + 1) != diff){
                    result--;
                    break;
                }
            }
        }
        
        System.out.println(result);
    }
}