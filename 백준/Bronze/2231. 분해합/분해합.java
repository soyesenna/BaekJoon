import java.io.*;
import java.util.*;

public class Main{
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        
        for (int i = 1; i < N; i++){
            String strNum = String.valueOf(i);
            int tmp = i;
            for (char c : strNum.toCharArray()){
                tmp += Character.digit(c, 10);
            }
            if (tmp == N) {
                System.out.println(i);
                System.exit(0);
            }
        }
        System.out.println(0);
    }
}