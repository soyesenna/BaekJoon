package p2839;

import java.io.*;
import java.util.*;
public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int threeCnt = 0;
        while (true) {
            int now = n;
            now -= threeCnt * 3;
            if (now == 0){
                System.out.println(threeCnt);
                break;
            }
            int fiveCnt = now / 5;
            if (fiveCnt == 0 && now != 3) {
                System.out.println(-1);
                break;
            }
            int fiveElse = now % 5;
            if (fiveElse == 0) {
                System.out.println(threeCnt + fiveCnt);
                break;
            }
            else threeCnt++;
        }
    }
}
