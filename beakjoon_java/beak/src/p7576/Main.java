package p7576;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static List<List<Integer>> box = new ArrayList<>();
    public static List<List<Integer>> roots = new ArrayList<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            List<Integer> tmpList = new ArrayList<>();
            for (int j = 0; j < M; j++) {
                int n = Integer.parseInt(st1.nextToken());
                if (n == 1) roots.add(new ArrayList<>(List.of(i, j)));
                tmpList.add(n);
            }
            box.add(tmpList);
        }

        System.out.println(bfs());
    }

    public static int bfs(){
        boolean[][] visit = new boolean[N][M];
        int[][] distance = new int[N][M];

        Deque<List<Integer>> queue = new ArrayDeque<>();

        for (List<Integer> root : roots) {
            distance[root.get(0)][root.get(1)] = 1;
            queue.add(root);
            visit[root.get(0)][root.get(1)] = true;
        }

        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            visit[now.get(0)][now.get(1)] = true;

            for (List<Integer> dir : direction) {
                int nowR = now.get(0) + dir.get(0);
                int nowC = now.get(1) + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC]) {
                    if (box.get(nowR).get(nowC) == -1) distance[nowR][nowC] = -1;
                    else {
                        queue.add(new ArrayList<>(List.of(nowR, nowC)));
                        visit[nowR][nowC] = true;
                        distance[nowR][nowC] = distance[now.get(0)][now.get(1)] + 1;
                    }
                }
            }
        }


        int max = Integer.MIN_VALUE;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (box.get(i).get(j) == -1) continue;
                if (distance[i][j] == 0) return -1;
                max = Math.max(max, distance[i][j]);
            }
        }
        return max == Integer.MIN_VALUE ? 0 : max - 1;

    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
