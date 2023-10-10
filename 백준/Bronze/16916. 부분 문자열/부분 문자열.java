
import java.io.*;
import java.util.*;
public class Main {

    public static String target;
    public static String pattern;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        target = br.readLine();
        pattern = br.readLine();

        int[] table = getTable();

        //System.out.println(Arrays.toString(table));
        System.out.println(kmp());
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

    public static int kmp() {
        int[] table = getTable();
        char[] parents = target.toCharArray();
        char[] patterns = pattern.toCharArray();
        int k = 0;
        for (int i = 0; i < parents.length; i++) {
            while (k > 0 && parents[i] != patterns[k]) {
                k = table[k - 1];
            }
            if (parents[i] == patterns[k]) {
                if (k == patterns.length - 1) {
                    k = table[k];
                    return 1;
                } else {
                    k++;
                }
            }
        }
        return 0;
    }

}
