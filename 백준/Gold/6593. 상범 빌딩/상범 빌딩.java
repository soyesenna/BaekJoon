
import java.io.*;
import java.util.*;
public class Main {

    public static int L, R, C;
    public static char[][][] space;
    public static int[][] direction = {
            {-1, 0, 0},
            {0, 1, 0},
            {1, 0, 0},
            {0, -1, 0},
            {0, 0, -1},
            {0, 0, 1}
    };

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            if (L == 0 && R == 0 && L == 0) break;

            space = new char[R][C][L];

            int[] start = new int[4];
            int[] end = new int[4];

            for (int i = 0; i < L; i++) {
                for (int j = 0; j < R; j++) {
                    String input = br.readLine();
                    for (int k = 0; k < C; k++) {
                        char c = input.charAt(k);
                        space[j][k][i] = c;
                        if (c == 'S') {
                            start[0] = j;
                            start[1] = k;
                            start[2] = i;
                        } else if (c == 'E') {
                            end[0] = j;
                            end[1] = k;
                            end[2] = i;
                        }
                    }
                }
                br.readLine();
            }

            int result = bfs(start, end);
            if (result == -1) System.out.println("Trapped!");
            else System.out.println("Escaped in " + result + " minute(s).");
        }

    }

    public static int bfs(int[] start, int[] end) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(start);
        boolean[][][] visit = new boolean[R][C][L];
        visit[start[0]][start[1]][start[2]] = true;

        int result = -1;
        while (!queue.isEmpty()) {
            int[] now = queue.pollFirst();
            visit[now[0]][now[1]][now[2]] = true;
            if (now[0] == end[0] && now[1] == end[1] && now[2] == end[2]) {
                result = now[3];
                break;
            }

            for (int[] dir : direction) {
                int nowR = now[0] + dir[0];
                int nowC = now[1] + dir[1];
                int nowL = now[2] + dir[2];

                if (inRange(nowR, nowC, nowL) && !visit[nowR][nowC][nowL] && space[nowR][nowC][nowL] != '#') {
                    int[] next = {nowR, nowC, nowL, now[3] + 1};
                    queue.add(next);
                    visit[nowR][nowC][nowL] = true;
                }
            }
        }

        return result;
    }

    public static boolean inRange(int r, int c, int l) {
        return r >= 0 && r < R && c >= 0 && c < C && l >= 0 && l < L;
    }
}
