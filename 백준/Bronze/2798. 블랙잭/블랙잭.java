import java.io.*;
import java.util.*;

public class Main{
    
    private static int N, M;
    private static List<Integer> cards = new ArrayList<>();
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        
        while (st.hasMoreTokens()){
            cards.add(Integer.parseInt(st.nextToken()));
        }
        
        int result = -1;
        int diff = Integer.MAX_VALUE;
        
        for (int i = 0; i < N - 2; i++){
            for (int j = i + 1; j < N - 1; j++){
                for (int k = j + 1; k < N; k++){
                    int now = cards.get(i) + cards.get(j) + cards.get(k);
                    if (now <= M && M - now < diff){
                        diff = M - now;
                        result = now;
                    }
                }   
            }
        }
        
        System.out.println(result);
    }
}