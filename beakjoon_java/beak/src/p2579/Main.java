package p2579;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int[] table;
    public static int[] score;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        table = new int[N + 1];

        score = new int[N + 1];

        for (int i = 1; i < N + 1; i++) {
            score[i] = Integer.parseInt(br.readLine());
        }

        table[1] = score[1];
        if (N == 1){
            System.out.println(table[1]);
            System.exit(0);
        }
        table[2] = score[1] + score[2];
        if (N == 2){
            System.out.println(table[2]);
            System.exit(0);
        }
        table[3] = (Math.max(score[1] + score[3], score[2] + score[3]));

        for (int i = 4; i < N; i++) {
            table[i] = (Math.max(table[i - 3] + score[i - 1] + score[i], table[i - 2] + score[i]));
        }

        System.out.println(Math.max(table[N - 3] + score[N - 1] + score[N], table[N - 2] + score[N]));

    }


//10 17 17 22 52 67
}
