package p2638;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static List<List<Node>> space = new ArrayList<>();
    public static Deque<Node> meltCheese = new ArrayDeque<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static int result = 0;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        Deque<Node> outAir = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            List<Node> tmp = new ArrayList<>();
            for (int j = 0; j < M; j++) {
                Node nodeTmp = new Node(i, j, 0, st.nextToken().equals("1"), false);
                if (i == 0 || i == N - 1 || j == 0 || j == M - 1) outAir.add(nodeTmp);
                tmp.add(nodeTmp);
            }
            space.add(tmp);
        }

        boolean[][] visit = new boolean[N][M];
        getInCheeseBFS(visit, outAir);

        for (List<Node> nodes : space) {
            for (Node node : nodes) {
                if (!node.isCheese && !visit[node.r][node.c]) {
                    node.inCheese = true;
                }
            }
        }


        for (List<Node> nodes : space) {
            for (Node node : nodes) {
                if (node.isCheese){
                    for (List<Integer> dir : direction) {
                        int nowR = node.r + dir.get(0);
                        int nowC = node.c + dir.get(1);
                        if (inRange(nowR, nowC) && !space.get(nowR).get(nowC).isCheese && !space.get(nowR).get(nowC).inCheese) {
                            node.airCnt += 1;
                            if (node.airCnt >= 2) meltCheese.add(node);
                        }
                    }
                }

            }
        }
        while (melting()) {
//            for (List<Node> nodes : space) {
//                for (Node node : nodes) {
//                    System.out.print("" + (node.isCheese ? 1 : 0) + " ");
//                }
//                System.out.println();
//            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(result);
        bw.write(sb.toString());
        bw.flush();

    }

    public static void getInCheeseBFS(boolean[][] visit, Deque<Node> queue) {
        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c] = true;
            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC] && !space.get(nowR).get(nowC).isCheese){
                    Node tmp = new Node(nowR, nowC, 0, false, false);
                    visit[nowR][nowC] = true;
                    queue.add(tmp);
                }
            }
        }
    }

    public static Set<Node> bfs(Node start, boolean[][] visit) {
        Deque<Node> queue = new ArrayDeque<>();
        Set<Node> toReturn = new HashSet<>();
        queue.add(start);
        visit[start.r][start.c] = true;
        start.inCheese = false;
        //toReturn.add(start);

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.r][now.c] = true;
            now.inCheese = false;

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC) && space.get(nowR).get(nowC).isCheese) {
                    Node tmp = space.get(nowR).get(nowC);
                    tmp.airCnt += 1;
                    if (tmp.airCnt >= 2) toReturn.add(tmp);
                } else if (inRange(nowR, nowC) && !space.get(nowR).get(nowC).isCheese && space.get(nowR).get(nowC).inCheese) {
                    queue.add(space.get(nowR).get(nowC));
                    visit[nowR][nowC] = true;
                }
            }
        }

        return toReturn;
    }

    public static boolean melting(){

        Set<Node> nextMelt = new HashSet<>();
        boolean flag = false;
        while (!meltCheese.isEmpty()) {
            Node now = meltCheese.pollFirst();
            now.isCheese = false;
            if (!flag){
                flag = true;
                result++;
            }
            boolean[][] visit = new boolean[N][M];
            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC) && space.get(nowR).get(nowC).isCheese) {
                    Node tmp = space.get(nowR).get(nowC);
                    System.out.println(tmp.isCheese);
                    tmp.airCnt += 1;
                    if (tmp.airCnt >= 2) nextMelt.add(tmp);
                } else if (inRange(nowR, nowC) && space.get(nowR).get(nowC).inCheese) {
                    nextMelt.addAll(bfs(now, visit));
                }
            }
        }

        meltCheese = new ArrayDeque<>(nextMelt);

        return !meltCheese.isEmpty();
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}

class Node {
    int r, c;
    int airCnt;
    boolean isCheese;
    boolean inCheese;

    public Node(int r, int c, int airCnt, boolean isCheese, boolean inCheese) {
        this.r = r;
        this.c = c;
        this.airCnt = airCnt;
        this.isCheese = isCheese;
        this.inCheese = inCheese;
    }
}
