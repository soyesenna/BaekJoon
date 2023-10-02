package p16946;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static List<char[]> space = new ArrayList<>();
    public static List<char[]> result = new ArrayList<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static boolean[][] visit;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            space.add(br.readLine().toCharArray());
        }

        for (int i = 0; i < N; i++) {
            char[] tmp = new char[M];
            for (int j = 0; j < M; j++) {
                if (space.get(i)[j] == '1'){
                    space.get(i)[j] = '0';
                    visit = new boolean[N][M];
                    tmp[j] =Character.forDigit(dfs(i, j) + 1, 10);
                    space.get(i)[j] = '1';
                }else{
                    tmp[j] = '0';
                }
            }
            result.add(tmp);
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (char[] chars : result) {
            StringBuilder sb = new StringBuilder();
            sb.append(chars);
            sb.append("\n");
            bw.write(sb.toString());

            bw.flush();
        }
        bw.close();
        br.close();

    }

    public static int dfs(int r, int c) {

        visit[r][c] = true;

        int result = 0;
        for (List<Integer> dir : direction) {
            int nowR = r + dir.get(0);
            int nowC = c + dir.get(1);
            if (inRange(nowR, nowC) && !visit[nowR][nowC] && space.get(nowR)[nowC] != '1') {
                visit[nowR][nowC] = true;
                result += 1 + dfs(nowR, nowC);
            }
        }
        return result;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
