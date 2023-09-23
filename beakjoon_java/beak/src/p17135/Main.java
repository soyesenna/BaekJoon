package p17135;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static int D;
    public static List<List<Integer>> game = new ArrayList<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static int kill = 0;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            List<Integer> tmpList = new ArrayList<>();
            while (st1.hasMoreTokens()) {
                tmpList.add(Integer.parseInt(st1.nextToken()));
            }
            game.add(tmpList);
        }
        List<Integer> tmpList = new ArrayList<>();
        for (int i = 0; i < M; i++) tmpList.add(0);
        game.add(tmpList);

        for (int i = 0; i < M - 2; i++) {
            for (int j = i + 1; j < M - 1; j++) {
                for (int k = j + 1; k < M; k++) {
                    List<List<Integer>> nowGame = newGame();
                    int nowKill = 0;
                    while (checkGame(nowGame)) {
                        Set<Node> now = new HashSet<>();
                        now.add(bfs(i, new ArrayList<>(nowGame)));
                        now.add(bfs(j,new ArrayList<>(nowGame)));
                        now.add(bfs(k, new ArrayList<>(nowGame)));
                        for (Node node : now) {
                            if (node == null) continue;
                            if (nowGame.get(node.getR()).get(node.getC()) != 1) continue;
                            nowGame.get(node.getR()).set(node.getC(), 0);
                            nowKill++;
                        }
                        Deque<List<Integer>> nowGame1 = new ArrayDeque<>(nowGame);
                        List<Integer> tmp = nowGame1.pollLast();
                        nowGame1.pollLast();
                        List<Integer> toInsert = new ArrayList<>();
                        for (int p = 0; p < M; p++) toInsert.add(0);
                        nowGame1.addFirst(toInsert);
                        nowGame1.addLast(tmp);
                        nowGame = new ArrayList<>(nowGame1);
                    }
                    kill = Math.max(kill, nowKill);
                }
            }
        }
        System.out.println(kill);
    }

    public static boolean checkGame(List<List<Integer>> check) {

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (check.get(i).get(j) == 1) return true;
            }
        }
        return false;
    }

    public static List<List<Integer>> newGame() {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < M; j++) {
                tmp.add(game.get(i).get(j));
            }
            result.add(tmp);
        }
        return result;
    }

    public static Node bfs(int nowAch, List<List<Integer>> game) {
        Deque<Node> queue = new ArrayDeque<>();
        Set<Node> visit = new HashSet<>();
        queue.add(new Node(N, nowAch, 0));

        List<Node> find = new ArrayList<>();
        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit.add(now);
            if (now.getDistance() == D) continue;

            for (List<Integer> dir : direction) {
                int nowR = now.getR() + dir.get(0);
                if (nowR == N) continue;
                int nowC = now.getC() + dir.get(1);
                Node next = new Node(nowR, nowC, now.getDistance() + 1);
                if (inRange(nowR, nowC) && !visit.contains(next)) {
                    queue.add(next);
                    visit.add(next);
                    if (game.get(nowR).get(nowC) == 1) find.add(next);
                }
            }

        }
         if (find.isEmpty()) return null;

        Collections.sort(find, (Node n1, Node n2) -> {
            if (n1.getDistance() == n2.getDistance()){
                return n1.getC() - n2.getC();
            }else return n1.getDistance() - n2.getDistance();
        });

        return find.get(0);

    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }

}

class Node{
    int r;
    int c;
    int distance;

    public Node() {
    }

    public Node(int r, int c, int distance) {
        this.r = r;
        this.c = c;
        this.distance = distance;
    }

    public int getR() {
        return r;
    }

    public void setR(int r) {
        this.r = r;
    }

    public int getC() {
        return c;
    }

    public void setC(int c) {
        this.c = c;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }


    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Node) {
            return ((Node) obj).getR() == this.getR() && ((Node)obj).getC() == this.getC();
        }
        return false;
    }
}