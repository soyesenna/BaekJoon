package p10026;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static List<char[]> normal = new ArrayList<>();
    public static List<char[]> redGreen = new ArrayList<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            char[] str = br.readLine().toCharArray();
            char[] toNormal = new char[N];
            char[] toRed = new char[N];
            for (int j = 0; j < N; j++) {
                toRed[j] = str[j];
                if (str[j] == 'G') toRed[j] = 'R';
                toNormal[j] = str[j];
            }
            redGreen.add(toRed);
            normal.add(toNormal);
        }

        System.out.println(check(normal) + " " + check(redGreen));
    }

    public static int check(List<char[]> target) {
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (target.get(i)[j] != 'C'){
                    bfs(target, i, j);
                    cnt++;
                }
            }
        }
        return cnt;
    }

    public static void bfs(List<char[]> target, int r, int c) {
        char targetChar = target.get(r)[c];
        Deque<List<Integer>> queue = new ArrayDeque<>();
        boolean[][] visit = new boolean[N][N];
        queue.add(new ArrayList<>(List.of(r, c)));
        visit[r][c] = true;
        target.get(r)[c] = 'C';

        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            visit[now.get(0)][now.get(1)] = true;
            target.get(now.get(0))[now.get(1)] = 'C';

            for (List<Integer> dir : direction) {
                int nowR = now.get(0) + dir.get(0);
                int nowC = now.get(1) + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC] && target.get(nowR)[nowC] == targetChar){
                    queue.add(new ArrayList<>(List.of(nowR, nowC)));
                    visit[nowR][nowC] = true;
                }
            }

        }
    }

    public static boolean inRange(int r, int c) {
        return r >=0 && r < N && c >= 0 && c < N;
    }
}
