package programmers.p169199;

import java.util.*;
public class MainFail {


    public static void main(String[] args) throws Exception {
        SolutionFail s = new SolutionFail();
        String[] board = {"...D..R", ".D.G...", "....D.D", "D....D.", "..D...."};
        System.out.println(s.solution(board));
    }
}

class SolutionFail {
    public List<Integer> nowIndex = new ArrayList<>();
    public List<Integer> goal = new ArrayList<>();
    public int lengthR;
    public int lengthC;
    public List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public boolean[][] visit;

    public int solution(String[] board) {
        lengthR = board.length;
        lengthC = board[0].length();
        visit = new boolean[lengthR][lengthC];
        boolean flag = true;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length(); j++) {
                if (board[i].charAt(j) == 'R') {
                    nowIndex.add(i);
                    nowIndex.add(j);
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
        }
        flag = true;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length(); j++) {
                if (board[i].charAt(j) == 'G') {
                    goal.add(i);
                    goal.add(j);
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
        }

        int result = dfs(nowIndex.get(0), nowIndex.get(1), 0, board);
        if (result == Integer.MAX_VALUE) return -1;
        else return result;
    }


    public int dfs(int r, int c, int cnt, String[] board){
        if (r == goal.get(0) && c == goal.get(1)) return cnt;

        visit[r][c] = true;
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
        int result = res.stream().min(Comparator.naturalOrder()).orElseGet(() -> Integer.MAX_VALUE);
        return result;
    }


    public boolean inRange(int r, int c){
        return r >= 0 && r < lengthR && c >= 0 && c < lengthC;
    }

}