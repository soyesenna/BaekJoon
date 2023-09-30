package p1700;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int K;
    public static int[] multiTap;
    public static LinkedList<Integer> orders = new LinkedList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        multiTap = new int[N];

        StringTokenizer st1 = new StringTokenizer(br.readLine());

        while (st1.hasMoreTokens()) orders.add(Integer.parseInt(st1.nextToken()));

        int cnt = 0;
        while (!orders.isEmpty()) {
            int order = orders.poll();
            boolean isHasOrder = false;
            for (int i = 0; i < N; i++) {
                if (multiTap[i] == order) isHasOrder = true;
            }
            if (isHasOrder) continue;
            boolean flag = false;
            for (int i = 0; i < N; i++) {
                if (multiTap[i] == 0) {
                    multiTap[i] = order;
                    flag = true;
                    break;
                }
            }
            if (!flag){
                List<List<Integer>> fre = new ArrayList<>();
                for (int i = 0; i < N; i++) {
                    fre.add(new ArrayList<>(List.of(i, orders.indexOf(multiTap[i]))));
                }
                Collections.sort(fre, (List<Integer> l1, List<Integer> l2) -> {
                    if (l1.get(1) == -1) l1.set(1, Integer.MAX_VALUE);
                    if (l2.get(1) == -1) l2.set(1, Integer.MAX_VALUE);
                    return l2.get(1) - l1.get(1);
                });
                multiTap[fre.get(0).get(0)] = order;
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
