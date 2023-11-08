
import java.io.*;
import java.util.*;
public class Main {

    public static int N, M, H;
    public static int[][][] space;
    public static List<int[]> tomato = new ArrayList<>();
    public static int[][] direction = {
            {-1, 0, 0},
            {0, 1, 0},
            {1, 0, 0},
            {0, -1, 0},
            {0, 0, 1},
            {0, 0, -1}
    };

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        space = new int[N][M][H];

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < M; k++) {
                    int now = Integer.parseInt(st.nextToken());
                    if (now == 1) {
                        int[] nowTomato = {j, k, i, 0};
                        tomato.add(nowTomato);
                    }
                    space[j][k][i] = now;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(bfs());
        bw.write(sb.toString());

        bw.close();
        br.close();

    }

    public static int bfs() {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addAll(tomato);
        boolean[][][] visit = new boolean[N][M][H];

        int result = Integer.MIN_VALUE;
        while (!queue.isEmpty()) {
            int[] now = queue.pollFirst();
            space[now[0]][now[1]][now[2]] = 1;
            visit[now[0]][now[1]][now[2]] = true;
            if (now[3] > result) result = now[3];

            for (int[] dir : direction) {
                int nowR = now[0] + dir[0];
                int nowC = now[1] + dir[1];
                int nowH = now[2] + dir[2];

                if (inRange(nowR, nowC, nowH) && !visit[nowR][nowC][nowH] && space[nowR][nowC][nowH] == 0) {
                    int[] next = {nowR, nowC, nowH, now[3] + 1};
                    queue.add(next);
                    visit[nowR][nowC][nowH] = true;
                }
            }
        }

        for (int[][] ints : space) {
            for (int[] anInt : ints) {
                for (int i : anInt) {
                    if (i == 0) return -1;
                }
            }
        }

        return result;
    }

    public static boolean inRange(int r, int c, int h) {
        return r >= 0 && r < N && c >= 0 && c < M && h >= 0 && h < H;
    }
}
