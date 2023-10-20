
import java.io.*;
import java.util.*;
public class Main {

    public static int K;
    public static int N, M;

    public static int[][] space;

    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static List<List<Integer>> horseDirection = List.of(
            List.of(-2, 1),
            List.of(-1, 2),
            List.of(2, 1),
            List.of(1, 2),
            List.of(2, -1),
            List.of(1, -2),
            List.of(-2, -1),
            List.of(-1, -2)
    );

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        K = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        space = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                space[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(bfs(0, 0));

    }

    public static int bfs(int r, int c) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(r, c, 0, 0));
        boolean[][][] visit = new boolean[N][M][K + 1];
        visit[r][c][0] = true;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c][now.horseCnt] = true;
            if (now.r == N - 1 && now.c == M - 1) return now.cnt;

            if (now.horseCnt < K){
                for (List<Integer> dir : horseDirection) {
                    int nowR = now.r + dir.get(0);
                    int nowC = now.c + dir.get(1);

                    if (inRange(nowR, nowC) && !visit[nowR][nowC][now.horseCnt + 1] && space[nowR][nowC] == 0) {
                        queue.add(new Node(nowR, nowC, now.cnt + 1, now.horseCnt + 1));
                        visit[nowR][nowC][now.horseCnt + 1] = true;
                    }
                }
            }


            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);

                if (inRange(nowR, nowC) && !visit[nowR][nowC][now.horseCnt] && space[nowR][nowC] == 0) {
                    queue.add(new Node(nowR, nowC, now.cnt + 1, now.horseCnt));
                    visit[nowR][nowC][now.horseCnt] = true;
                }
            }
        }

        return -1;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }


}

class Node {
    int r,c;
    int cnt;
    int horseCnt;

    public Node(int r, int c, int cnt, int horseCnt) {
        this.r = r;
        this.c = c;
        this.cnt = cnt;
        this.horseCnt = horseCnt;
    }
}