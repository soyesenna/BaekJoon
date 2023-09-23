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
    public static boolean[][] visitIdx;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        visitIdx = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            space.add(br.readLine().toCharArray());
        }

        visitIdx[0][0] = true;

        dfs(0, 0, new ArrayList<>(List.of(space.get(0)[0])));
        System.out.println(result);

    }

    public static void dfs(int r, int c, List<Character> visitChar) {
        if (r != 0 && c != 0) {
            if (visitChar.contains(space.get(r)[c])) {
                result = Math.max(result, visitChar.size());
                return;
            }
            if (visitIdx[r][c]) return;
        }

        for (List<Integer> dir : direction) {
            int nowR = r + dir.get(0);
            int nowC = c + dir.get(1);
            if (inRange(nowR, nowC)) {
                visitIdx[nowR][nowC] = true;
                visitChar.add(space.get(nowR)[nowC]);
                dfs(nowR, nowC, visitChar);
                visitIdx[nowR][nowC] = false;
                visitChar.remove(visitChar.size() - 1);
            }
        }

    }
    public static boolean inRange(int r, int c) {
        return r >= 0 && r < R && c >= 0 && c < C;
    }
}
