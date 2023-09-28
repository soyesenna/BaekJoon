
import java.io.*;
import java.util.*;

public class Main {

    public static int N;
    public static int M;
    public static char[][] space;
    public static boolean[][] visit;
    public static int result = 0;
    public static Deque<List<Integer>> birds = new ArrayDeque<>();
    public static Deque<List<Integer>> meltIce = new ArrayDeque<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        space = new char[N][M];
        visit = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                if (str.charAt(j) == 'L') birds.add(List.of(i, j));
                space[i][j] = str.charAt(j);
            }
        }
        birds.pollFirst();

        //천만번 썻음
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (space[i][j] == 'X'){
                    for (List<Integer> dir : direction) {
                        int nowR = i + dir.get(0);
                        int nowC = j + dir.get(1);
                        if (inRange(nowR, nowC) && (space[nowR][nowC] == '.' || space[nowR][nowC] == 'L'))
                            meltIce.add(List.of(i, j));
                    }
                }
            }
        }

        while (!bfsBird()) {
            if (meltIce.size() != 0) bfsIce();
            result++;
        }

        System.out.println(result);
    }

    public static void bfsIce(){
        Deque<List<Integer>> queue = new ArrayDeque<>(meltIce);
        meltIce = new ArrayDeque<>();
        boolean[][] visit = new boolean[N][M];
        List<Integer> ice = queue.peekFirst();
        visit[ice.get(0)][ice.get(1)] = true;

        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            visit[now.get(0)][now.get(1)] = true;
            space[now.get(0)][now.get(1)] = '.';

            for (List<Integer> dir : direction) {
                int nowR = now.get(0) + dir.get(0);
                int nowC = now.get(1) + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC] && space[nowR][nowC] == 'X') {
                    meltIce.add(List.of(nowR, nowC));
                    visit[nowR][nowC] = true;
                }
            }
        }

    }

    public static boolean bfsBird() {
        Deque<List<Integer>> queue = new ArrayDeque<>(birds);
        birds = new ArrayDeque<>();
        List<Integer> bird = queue.peekFirst();
        visit[bird.get(0)][bird.get(1)] = true;

        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            visit[now.get(0)][now.get(1)] = true;
            boolean flag = false;
            for (List<Integer> dir : direction) {
                int nowR = now.get(0) + dir.get(0);
                int nowC = now.get(1) + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC]) {
                    if (space[nowR][nowC] == 'L'){
                        return true;
                    }else if (space[nowR][nowC] == '.'){
                        queue.add(List.of(nowR, nowC));
                        visit[nowR][nowC] = true;
                        flag = true;
                    }
                }
            }
            if (!flag) birds.add(now);
        }
        return false;
    }

    public static boolean inRange(int r, int c) {
        return 0 <= r && r < N && c >= 0 && c < M;
    }
}
