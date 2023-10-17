package p1463;

import java.io.*;
import java.util.*;
public class Main {

    public static int[] dpArray;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (n == 1){
            System.out.println(0);
            System.exit(0);
        } else if (n <= 3) {
            System.out.println(1);
            System.exit(0);
        }
        dpArray = new int[n + 1];
        for (int i = 0; i < n; i++) dpArray[i] = Integer.MAX_VALUE;

        dpArray[1] = 0;
        dpArray[2] = 1;
        dpArray[3] = 1;

        System.out.println(dp(n));
    }

    public static int dp(int n) {
        if (n == 1) return 0;
        if (n == 2) return 1;
        if (n == 3) return 1;

        if (n % 2 == 0 && n % 3 == 0){
            int res =  minThree(dpArray[(int)(n / 3)] == Integer.MAX_VALUE ? dp((int) (n / 3)) + 1 : dpArray[(int)(n / 3)] + 1,
                    dpArray[(int)(n / 2)] == Integer.MAX_VALUE ? dp((int) (n / 2)) + 1 : dpArray[(int)(n / 2)] + 1,
                    dpArray[n - 1] == Integer.MAX_VALUE ? dp(n - 1) + 1 : dpArray[n - 1] + 1);
            dpArray[n] = Math.min(res, dpArray[n]);
            return res;
        }else if (n % 2 == 0){
            int res = Math.min(dpArray[(int)(n / 2)] == Integer.MAX_VALUE ? dp((int) (n / 2)) + 1 : dpArray[(int)(n / 2)] + 1,
                    dpArray[n - 1] == Integer.MAX_VALUE ? dp(n - 1) + 1 : dpArray[n - 1] + 1);
            dpArray[n] = Math.min(res, dpArray[n]);
            return res;
        }else if (n % 3 == 0){
            int res = Math.min(dpArray[(int)(n / 3)] == Integer.MAX_VALUE ? dp((int) (n / 3)) + 1 : dpArray[(int)(n / 3)] + 1,
                    dpArray[n - 1] == Integer.MAX_VALUE ? dp(n - 1) + 1 : dpArray[n - 1] + 1);
            dpArray[n] = Math.min(res, dpArray[n]);
            return res;
        } else {
            int res = dpArray[n - 1] == Integer.MAX_VALUE ? dp(n - 1) + 1 : dpArray[n - 1] + 1;
            dpArray[n] = Math.min(res, dpArray[n]);
            return res;
        }

    }

    public static int minThree(int a, int b, int c) {
        return Math.min(Math.min(a, b), c);
    }
}
