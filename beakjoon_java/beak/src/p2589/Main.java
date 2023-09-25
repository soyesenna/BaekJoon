package p2589;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static List<String> space = new ArrayList<>();
    public static boolean[][] visit;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visit = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            space.add(br.readLine());
        }

        int result = Integer.MIN_VALUE;

        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++) {
                if (space.get(i).charAt(j) == 'L') {
                    result = Math.max(result, bfs(i, j));
                }
            }
        }
       System.out.println(result);
//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < M; j++){
//                System.out.print(visit[i][j] + " ");
//            }
//            System.out.println();
//        }
    }

    public static int bfs(int r, int c) {
        Deque<Node> queue = new ArrayDeque<>();
        visit = new boolean[N][M];
        visit[r][c] = true;
        queue.add(new Node(r, c, 0));
        int result = Integer.MIN_VALUE;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c] = true;
            result = Math.max(result, now.cnt);

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC] && space.get(nowR).charAt(nowC) == 'L') {
                    queue.add(new Node(nowR, nowC, now.cnt + 1));
                    visit[nowR][nowC] = true;
                }
            }
        }
        return result;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}

class Node {
    int r, c, cnt;

    public Node(int r, int c, int cnt) {
        this.r = r;
        this.c = c;
        this.cnt = cnt;
    }
}