
import java.io.*;
import java.util.*;
public class Main {

    public static int N, M;
    public static List<List<Integer>> zeros = new ArrayList<>();
    public static List<List<Integer>> ones = new ArrayList<>();
    public static int[][] dp;
    public static int[][] space;
    public static final int[][] direction = {
                {-1, 0},
                {0, 1},
                {1, 0},
                {0, -1}
        };
    public static int groupNum = 1;
    public static boolean[][] visit;
    public static int nowSize = 0;
    public static int[] groupSizeMap;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        dp = new int[N][M];
        space = new int[N][M];
        visit = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int now = Integer.parseInt(st.nextToken());
                if (now == 0) zeros.add(List.of(i, j));
                else ones.add(List.of(i, j));
                space[i][j] = now;
            }
        }

        //여기까지 700만번

        groupSizeMap = new int[N * M];

        for (List<Integer> one : ones) {
            if (!visit[one.get(0)][one.get(1)]) {
                dfs(one.get(0), one.get(1));
                groupSizeMap[groupNum] = nowSize;
                nowSize = 0;
                groupNum++;
            }
        }




        int result = Integer.MIN_VALUE;
        for (List<Integer> one : zeros) {
            int nowResult = 1;
            Set<Integer> plusGroup = new HashSet<>();
            for (int[] dir : direction) {
                int nowR = one.get(0) + dir[0];
                int nowC = one.get(1) + dir[1];
                if (inRange(nowR, nowC) && dp[nowR][nowC] != 0) {
                    plusGroup.add(dp[nowR][nowC]);
                }
            }
            for (Integer integer : plusGroup) {
                nowResult += groupSizeMap[integer];
            }
            if (result < nowResult) result = nowResult;
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(result));

        bw.close();
        br.close();

    }

    public static void dfs(int r, int c) {
        nowSize++;
        dp[r][c] = groupNum;
        visit[r][c] = true;
        for (int[] dir : direction) {
            int nowR = r + dir[0];
            int nowC = c + dir[1];
            if (inRange(nowR, nowC) && !visit[nowR][nowC] && space[nowR][nowC] == 1) {
                dfs(nowR, nowC);
            }
        }
        return;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
