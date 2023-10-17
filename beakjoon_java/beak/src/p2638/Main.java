package p2638;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static List<List<Node>> space = new ArrayList<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static Deque<Node> willMelt = new ArrayDeque<>();
    public static Deque<Node> cheeses = new ArrayDeque<>();
    public static int[][] spcaeToDebug;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        spcaeToDebug = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            List<Node> tmp = new ArrayList<>();
            for (int j = 0; j < M; j++) {
                int now = Integer.parseInt(st.nextToken());
                Node tmpNode = new Node(i, j, now == 1, false);
                tmp.add(tmpNode);
                if (now == 1) cheeses.add(tmpNode);
                spcaeToDebug[i][j] = now;
            }
            space.add(tmp);
        }

        findFirstOutAir();
        firstFindMeltCheese();

        int result = 0;

        while (!willMelt.isEmpty()) {
            meltAndFindMeltCheese();
            result++;
        }
        System.out.println(result);

    }

    public static void meltAndFindMeltCheese() {
        Set<Node> tmp = new HashSet<>();

        while (!willMelt.isEmpty()) {
            Node now = willMelt.pollFirst();
            now.cheese = false;
            spcaeToDebug[now.r][now.c] = 0;

            String flag = "none";
            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);

                if (inRange(nowR, nowC)){
                    Node next = space.get(nowR).get(nowC);
                    if (next.cheese) {
                        next.airCnt++;
                        if (next.airCnt > 1) {
                            tmp.add(next);
                        }
                    }else if(next.outAir) {
                        if (flag.equals("inAirContact")) tmp.addAll(findOutAir(next));
                        else flag = "outAirContact";
                    }else if (!next.outAir){
                        if (flag.equals("outAirContact")) tmp.addAll(findOutAir(next));
                        else flag = "inAirContact";
                    }
                }
            }
        }
        willMelt = new ArrayDeque<>(tmp);
    }

    public static Set<Node> findOutAir(Node first) {
        Deque<Node> queue = new ArrayDeque<>();
        Set<Node> toReturn = new HashSet<>();
        boolean[][] visit = new boolean[N][M];
        queue.add(first);
        visit[first.r][first.c] = true;
        first.cheese = false;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c] = true;
            now.cheese = false;

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);

                if (inRange(nowR, nowC) && !visit[nowR][nowC]) {
                    Node next = space.get(nowR).get(nowC);
                    if (next.cheese) {
                        next.airCnt++;
                        if (next.airCnt > 1) toReturn.add(next);
                    }else if(!next.outAir) {
                        next.outAir = true;
                        queue.add(next);
                        visit[nowR][nowC] = true;
                    }

                }
            }
        }
        first.cheese = true;
        return toReturn;
    }

    public static void firstFindMeltCheese() {
        while (!cheeses.isEmpty()){
            Node now = cheeses.pollFirst();
            int cnt = 0;
            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC)){
                    Node check = space.get(nowR).get(nowC);
                    if (!check.cheese && check.outAir) {
                        cnt++;
                    }
                }
            }
            if (cnt > 1) willMelt.add(now);
            now.airCnt = cnt;
        }

    }

    public static void findFirstOutAir() {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(space.get(0).get(0));
        boolean[][] visit = new boolean[N][M];
        visit[0][0] = true;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c] = true;
            now.outAir = true;

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);

                if (inRange(nowR, nowC) && !visit[nowR][nowC]) {
                    Node willNext = space.get(nowR).get(nowC);
                    if (!willNext.cheese){
                        queue.add(willNext);
                        visit[nowR][nowC] = true;
                        willNext.outAir = true;
                        //System.out.println(nowR + " " + nowC);
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
    int r, c;
    boolean cheese;
    boolean outAir;
    int airCnt = 0;

    public Node(int r, int c, boolean cheese, boolean outAir) {
        this.r = r;
        this.c = c;
        this.cheese = cheese;
        this.outAir = outAir;
    }
}