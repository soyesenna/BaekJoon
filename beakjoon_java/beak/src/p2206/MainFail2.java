package p2206;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class MainFail2 {

    public static int N;
    public static int M;
    public static int[][] space;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        if (N == 1 && M == 1) {
            System.out.println(1);
            System.exit(0);
        }
        space = new int[N][M];

        for (int i = 0; i < N; i++) {
            char[] tmp = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                int n = tmp[j] - '0';
                space[i][j] = n;
            }
        }

        bfs();
        //if (result == Integer.MAX_VALUE) System.out.println(-1);
        System.out.println(result);
    }

    public static void bfs(){
        Deque<List<Integer>> queue = new ArrayDeque<>();
        boolean[][] visit = new boolean[N][M];
        //r, c, distance, break wall count
        queue.add(new ArrayList<>(List.of(0, 0, 1, 0)));
        visit[0][0] = true;
        Set<List<Integer>> visitResult = new HashSet<>();

        int nowResult = Integer.MAX_VALUE;
        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            visitResult.add(now);
            visit[now.get(0)][now.get(1)] = true;
            //if (now.get(2) == nowResult) continue;

            for (List<Integer> dir : direction) {
                int nowR = now.get(0) + dir.get(0);
                int nowC = now.get(1) + dir.get(1);

                if (inRange(nowR, nowC)) {
                    if (!visit[nowR][nowC]) {
                        if (space[nowR][nowC] == 1) {
                            if (now.get(3) < 1) {
                                queue.add(new ArrayList<>(List.of(nowR, nowC, now.get(2) + 1, now.get(3) + 1)));
                                visit[nowR][nowC] = true;
                            }
                        } else {
                            queue.add(new ArrayList<>(List.of(nowR, nowC, now.get(2) + 1, now.get(3))));
                            visit[nowR][nowC] = true;
                        }
                        //visit[nowR][nowC] = true;
                    }else if (now.get(3) == 0){
                        if (space[nowR][nowC] == 1) {
                            queue.add(new ArrayList<>(List.of(nowR, nowC, now.get(2) + 1, now.get(3) + 1)));
                        } else {
                            queue.add(new ArrayList<>(List.of(nowR, nowC, now.get(2) + 1, now.get(3))));
                        }
                }
                }
            }
        }
        //System.out.println(visitResult);
        List<List<Integer>> find  = visitResult.stream()
                                        .filter((List<Integer> li) -> li.get(0) == N - 1 && li.get(1) == M - 1 && li.get(3) < 2)
                                        .sorted((List<Integer> li1, List<Integer> li2) -> li1.get(2) - li2.get(2))
                                        .collect(Collectors.toList());
        //System.out.println(find);
        if (find.isEmpty()) result = -1;
        else result = find.get(0).get(2);
    }
    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
