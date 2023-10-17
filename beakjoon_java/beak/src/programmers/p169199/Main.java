package programmers.p169199;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        String[] board = {"...D..R", ".D.G...", "....D.D", "D....D.", "..D...."};
        System.out.println(s.solution(board));
    }
}

class Solution{

    public int[][] dp;
    public List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public int lengthR;
    public int lengthC;
    public int[] robot = new int[2];
    public boolean[][] visit;
    public int[] start = new int[2];

    public int solution(String[] board){
        lengthR = board.length;
        lengthC = board[0].length();

        dp = new int[lengthR][lengthC];
        visit = new boolean[lengthR][lengthC];

        start = new int[2];
        boolean flag = false;
        for (int i = 0; i < lengthR; i++) {
            for (int j = 0; j < lengthC; j++) {
                if (board[i].charAt(j) == 'G'){
                    start[0] = i;
                    start[1] = j;
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
        flag = false;
        for (int i = 0; i < lengthR; i++) {
            for (int j = 0; j < lengthC; j++) {
                if (board[i].charAt(j) == 'R'){
                    robot[0] = i;
                    robot[1] = j;
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }

        dfs(robot[0], robot[1], 0, board);

        for (int i = 0; i < lengthR; i++) {
            for (int j = 0; j < lengthC; j++) {
                System.out.print(dp[i][j] + " ");
            }
            System.out.println();
        }

        return dp[robot[0]][robot[1]];
    }

    public int dfs(int r, int c, int cnt, String[] board) {
        if (r == start[0] && c == start[1]) return cnt;

        //visit[r][c] = true;
        if (dp[r][c] != 0) return dp[r][c];

        List<Integer> res = new ArrayList<>();
        for (List<Integer> dir : direction){
            int nowR = r;
            int nowC = c;
            while (inRange(nowR, nowC)){
                if (board[nowR].charAt(nowC) == 'D'){
                    break;
                }
                nowR += dir.get(0);
                nowC += dir.get(1);
            }
            nowR -= dir.get(0);
            nowC -= dir.get(1);
            if (!visit[nowR][nowC] && !(nowR == r && nowC == c)){
                visit[nowR][nowC] = true;
                res.add(dfs(nowR, nowC, cnt + 1, board));
                visit[nowR][nowC] = false;
            }
        }
        dp[r][c] = res.stream().min(Comparator.naturalOrder()).orElseGet(() -> 20);
        return dp[r][c];
    }

    public boolean inRange(int r, int c) {
        return r >= 0 && r < lengthR && c >= 0 && c < lengthC;
    }

}
