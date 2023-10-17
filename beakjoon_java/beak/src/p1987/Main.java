package p1987;

import java.io.*;
import java.util.*;

public class Main {

    public static int R;
    public static int C;

    public static List<char[]> space = new ArrayList<>();
    public static int result = Integer.MIN_VALUE;
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
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        visit = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            space.add(br.readLine().toCharArray());
        }
        if (R == 1 && C == 1) {
            System.out.println(1);
            System.exit(0);
        }

        dfs(0, 0, new ArrayDeque<>());

        System.out.println(result);
    }

    public static void dfs(int r, int c, Deque<Character> alpha) {
        char now = space.get(r)[c];
        if (alpha.contains(now)) {
            result = Math.max(result, alpha.size());
            return;
        }else{
            alpha.add(now);
            if (alpha.size() >= 26) {
                System.out.println(26);
                System.exit(0);
            }
        }

        for (List<Integer> dir : direction) {
            int nowR = r + dir.get(0);
            int nowC = c + dir.get(1);
            if (inRange(nowR, nowC) && !visit[nowR][nowC]){
                visit[nowR][nowC] = true;
                dfs(nowR, nowC, alpha);
                visit[nowR][nowC] = false;
            }
        }

        alpha.pollLast();
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < R && c >= 0 && c < C;
    }
}
