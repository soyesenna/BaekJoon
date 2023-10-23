
import java.io.*;
import java.util.*;
public class Main {

    public static int N, M, K;
    public static char[][] spcae;
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
        K = Integer.parseInt(st.nextToken());

        spcae = new char[N][M];

        for (int i = 0; i < N; i++) {
            spcae[i] = br.readLine().toCharArray();
        }

        System.out.println(bfs(new Node(0, 0, 0, 1)));

    }

    public static int bfs(Node start) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(start);
        boolean[][][] visit = new boolean[N][M][K + 1];
        visit[start.r][start.c][0] = true;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c][now.cnt] = true;
            if (now.r == N - 1 && now.c == M - 1) return now.distance;

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);

                if (inRange(nowR, nowC)) {
                    if (spcae[nowR][nowC] == '1' && now.cnt + 1 <= K && !visit[nowR][nowC][now.cnt + 1]) {
                        queue.add(new Node(nowR, nowC, now.cnt + 1, now.distance + 1));
                        visit[nowR][nowC][now.cnt + 1] = true;
                    }
                    if (spcae[nowR][nowC] == '0' && !visit[nowR][nowC][now.cnt]) {
                        queue.add(new Node(nowR, nowC, now.cnt, now.distance + 1));
                        visit[nowR][nowC][now.cnt] = true;
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

class Node {
    int r,c;
    int cnt;
    int distance;

    public Node(int r, int c, int cnt, int distance) {
        this.r = r;
        this.c = c;
        this.cnt = cnt;
        this.distance = distance;
    }
}