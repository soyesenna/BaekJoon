package p1520;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static int[][] space;
    public static int result = 0;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static boolean[][] visit;
    public static int[][] canLast;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        space = new int[N][M];
        visit = new boolean[N][M];
        canLast = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                space[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(List.of(0, 0));
        System.out.println(result);
    }

    public static int dfs(List<Integer> now) {
        if (now.get(0) == N - 1 && now.get(1) == M - 1) {
            result++;
            return 1;
        }
        //visit[now.get(0)][now.get(1)] = true;

        int flag = 0;
        for (List<Integer> dir : direction) {
            int nowR = now.get(0) + dir.get(0);
            int nowC = now.get(1) + dir.get(1);
            if (inRange(nowR, nowC)) {
                if (canLast[nowR][nowC] > 0) {
                    result += canLast[nowR][nowC];
                    return canLast[nowR][nowC] + 1;
                }
                if (!visit[nowR][nowC] && space[nowR][nowC] < space[now.get(0)][now.get(1)]) {
                    //visit[nowR][nowC] = true;
                    flag += dfs(List.of(nowR, nowC));
                    //visit[nowR][nowC] = false;
                }
            }

        }
        visit[now.get(0)][now.get(1)] = true;
        canLast[now.get(0)][now.get(1)] = flag;
        return flag;
    }

    public static boolean inRange(int r, int c) {
        return 0 <= r && r < N && c >= 0 && c < M;
    }
}
