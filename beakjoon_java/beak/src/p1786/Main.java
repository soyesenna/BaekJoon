package p1786;

import java.io.*;
import java.util.*;

public class Main {

    public static String target;
    public static String pattern;
    public static int cnt = 0;
    public static List<Integer> result = new ArrayList<>();


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        target = br.readLine();
        pattern = br.readLine();

        kmp();

        //System.out.println(target.length());

    }

    public static int[] getTable() {
        int[] pi = new int[pattern.length()];
        int j = 0;
        for (int i = 1; i < pattern.length(); i++) {
            // 맞는 위치가 나올 때까지 j - 1칸의 공통 부분 위치로 이동
            while(j > 0 && pattern.charAt(i) != pattern.charAt(j)){
                j = pi[j - 1];
            }
            // 맞는 경우
            if(pattern.charAt(i) == pattern.charAt(j)) {
                //i길이 문자열의 공통 길이는 j의 위치 + 1
                pi[i] = ++j;
            }
        }
        return pi;
    }

    public static void kmp() {
        int[] table = getTable();
        StringBuilder sb = new StringBuilder();

        int j = 0;
        int before = 0;

            for (int i = 0; i < target.length(); i++) {
                while (j > 0 && target.charAt(i) != pattern.charAt(j)) {
                    j = table[j - 1];
                }
                if (pattern.charAt(j) == target.charAt(i)) {
                    if (j == pattern.length() - 1) {
                        cnt++;
                        sb.append((i - pattern.length() + 2) + " ");
                        if (i == target.length() - 1) break;
                        i = ++before;
                        j = table[j];
                    } else {
                        j++;
                    }
                }
            }
        System.out.println(cnt);
        System.out.println(sb.toString());
        
    }
}
