package p12851;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int K;
    public static List<Integer> direction = List.of(1, -1, 2);
    public static List<List<Integer>> result = new ArrayList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        bfs();

        Optional<Integer> min = result.stream()
                                        .sorted((List<Integer> li1, List<Integer> li2) -> li1.get(1) - li2.get(1))
                                        .map((List<Integer> li) -> li.get(0))
                                        .findFirst();
        long resCnt = result.stream()
                            .filter((List<Integer> li) -> li.get(1) == min.get())
                            .count();
        System.out.println(min.get());
        System.out.println(resCnt);
    }

    public static void bfs() {
        Deque<List<Integer>> queue = new ArrayDeque<>();
        queue.add(new ArrayList<>(List.of(N, 0)));
        Set<List<Integer>> visit = new HashSet<>();
        visit.add(List.of(N, 0));

        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            if (now.get(0) == K){
                result.add(now);
                continue;
            }
            visit.add(now);

            for (Integer dir : direction) {
                int nowIdx = now.get(0);
                if (dir == 2) nowIdx *= 2;
                else nowIdx += dir;
                if (inRange(nowIdx) && !visit.contains(List.of(nowIdx, now.get(1) + 1))){
                    queue.add(new ArrayList<>(List.of(nowIdx, now.get(1) + 1)));
                    visit.add(List.of(nowIdx, now.get(1) + 1));
                }
            }
        }
    }

    public static boolean inRange(int n) {
        return n >= 0 && n <= K * 2;
    }
}
