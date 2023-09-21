
import java.io.*;
import java.util.*;

public class Main {

    public static int N;
    public static int M;
    public static boolean[][] visit;
    public static boolean[][] brokeVisit;
    public static int[][] space;
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
        brokeVisit = new boolean[N][M];

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

        System.out.println(bfs(new Node(0, 0, 1, false)));
    }

    public static int bfs(Node node) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(node);

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            if (now.r == N - 1 && now.c == M - 1) return now.distance;
            boolean[][] nowVisitMap;
            if (now.isBroken) nowVisitMap = brokeVisit;
            else nowVisitMap = visit;

            nowVisitMap[now.r][now.c] = true;

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC)) {
                    if (now.isBroken){
                        if (space[nowR][nowC] != 1 && !nowVisitMap[nowR][nowC]) {
                            queue.add(new Node(nowR, nowC, now.distance + 1, now.isBroken));
                            brokeVisit[nowR][nowC] = true;
                        }
                    }else{
                        if (space[nowR][nowC] == 1 && !visit[nowR][nowC]){
                            queue.add(new Node(nowR, nowC, now.distance + 1, true));
                            brokeVisit[nowR][nowC] = true;
                            //visit[nowR][nowC] = true;
                        }else if (!visit[nowR][nowC]){
                            queue.add(new Node(nowR, nowC, now.distance + 1, now.isBroken));
                            //brokeVisit[nowR][nowC] = true;
                            visit[nowR][nowC] = true;
                        }
                    }
                }
            }
        }
        return -1;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}

class Node{
    int r, c;
    int distance;
    boolean isBroken = false;

    public Node(int r, int c, int distance, boolean isBroken) {
        this.r = r;
        this.c = c;
        this.distance = distance;
        this.isBroken = isBroken;
    }
}
