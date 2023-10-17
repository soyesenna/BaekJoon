
import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static char[][] space;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static int[][] move;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        move = new int[N][M];
        space = new char[N][M];

        List<Integer> startJ = new ArrayList<>();
        List<List<Integer>> fire = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            char[] tmp = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                if (tmp[j] == 'J') {
                    startJ.add(i);
                    startJ.add(j);
                }else if(tmp[j] == 'F'){
                    fire.add(new ArrayList<>(List.of(i, j)));
                }
                space[i][j] = tmp[j];
            }
        }

        bfsJ(startJ.get(0), startJ.get(1));

        for (List<Integer> list : fire) {
            bfsF(list.get(0), list.get(1));
        }

//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < M; j++) {
//                System.out.print(move[i][j]);
//            }
//            System.out.println();
//        }

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            if (move[i][0] != 0) {
                result.add(move[i][0]);
            }
            else if(move[i][M - 1] != 0){
                result.add(move[i][M - 1]);
            }
        }

        for (int i = 0; i < M; i++) {
            if (move[0][i] != 0){
                result.add(move[0][i]);
            } else if (move[N - 1][i] != 0) {
                result.add(move[N - 1][i]);
            }
        }

        if (result.isEmpty()) System.out.println("IMPOSSIBLE");
        else {
            Collections.sort(result);
            System.out.println(result.get(0));
        }

    }

    public static void bfsF(int r, int c) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(r, c, 1));
        boolean[][] visit = new boolean[N][M];
        visit[r][c] = true;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c] = true;

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC] && space[nowR][nowC] != '#') {
                    if (move[nowR][nowC] >= now.days + 1) {
                        move[nowR][nowC] = 0;
                    }
                    queue.add(new Node(nowR, nowC, now.days + 1));
                    visit[nowR][nowC] = true;
                }
            }
        }
    }

    public static void bfsJ(int r, int c) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(r, c, 1));
        boolean[][] visit = new boolean[N][M];
        visit[r][c] = true;
        move[r][c] = 1;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c] = true;

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC]) {
                    if (space[nowR][nowC] == '.' || space[nowR][nowC] == 'J') {
                        move[nowR][nowC] = now.days + 1;
                        queue.add(new Node(nowR, nowC, now.days + 1));
                        visit[nowR][nowC] = true;
                    }
                }
            }
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}

class Node {
    int r,c;
    int days;

    public Node(int r, int c, int days) {
        this.r = r;
        this.c = c;
        this.days = days;
    }
}