package p2668;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static List<Integer> first = new ArrayList<>();
    public static boolean[] visit;
    public static List<Integer> second = new ArrayList<>();
    public static Set<Integer> numResult = new HashSet<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        visit = new boolean[N];

        for (int i = 0; i < N; i++) {
            first.add(i);
            second.add(Integer.parseInt(br.readLine()) - 1);
        }

        for (int i = 0; i < N; i++) {
            visit = new boolean[N];
            if (first.get(i).equals(second.get(i))) {
                numResult.add(first.get(i));
            }
            else if (!visit[i]) dfs(i, 0, first.get(i));

        }



        System.out.println(numResult.size());
        List<Integer> resultList = new ArrayList<>(numResult);
        Collections.sort(resultList);
        for (Integer num : resultList) {
            System.out.println(num + 1);
        }



    }

    public static int dfs(int idx, int cnt, int start) {
        if (!visit[idx]){
            if (!visit[second.get(idx)]) {
                visit[idx] = true;
                int re = dfs(second.get(idx), cnt + 1, start);
                if (re != 0) {
                    numResult.add(first.get(idx));
                }
                return re;
            }
            else{
                if (second.get(idx) == start) return cnt;
            }
        }

        return 0;
    }
}
