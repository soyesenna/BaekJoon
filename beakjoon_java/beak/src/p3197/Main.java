package p3197;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static int R;
    public static int C;
    public static List<Node> lake = new ArrayList<>();
    public static List<Node> birds = new ArrayList<>();
    public static int day = 0;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        for (int i = 0; i < R; i++) {
            char[] tmp = br.readLine().toCharArray();
            for (int j = 0; j < C; j++){
                if (tmp[j] == '.') lake.add(new Node(i, j, false));
                else if(tmp[j] == 'X') lake.add(new Node(i, j, true));
                else {
                    Node bird = new Node(i, j, false);
                    bird.setBird(true);
                    lake.add(bird);
                    birds.add(bird);
                }
            }
        }

        while (!bfs()) {
            meltIce();
            day++;
        }
        System.out.println(day);

    }

    public static boolean bfs() {
        Deque<Node> queue = new ArrayDeque<>();
        List<Node> visit = new ArrayList<>();
        Node start = birds.get(0);
        queue.add(start);

        lake.stream()
                .forEach((Node node) -> node.setVisit(false));

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            if (now.isBird() && !now.equals(birds.get(0))) return true;
            now.setVisit(true);
            for (List<Integer> dir : direction) {
                int nowR = now.getR() + dir.get(0);
                int nowC = now.getC() + dir.get(1);
                if (inRange(nowR, nowC)) {
                    Node next = Node.findNode(nowR, nowC, lake);
                    if (!next.isIce() && !next.isVisit()) {
                        queue.add(next);
                        visit.add(next);
                    }
                }
            }
        }
        return false;
    }

    public static void meltIce(){
        List<Node> tmp = new ArrayList<>();
        for (Node node : lake) {
            tmp.add(node.nodeCopy());
        }

        lake.stream()
            .filter((Node n) -> {
                if (n.isIce) {
                    for (List<Integer> dir : direction) {
                        int nowR = n.getR() + dir.get(0);
                        int nowC = n.getC() + dir.get(1);
                        if (inRange(nowR, nowC) && !Node.findNode(nowR, nowC, tmp).isIce()) return true;
                    }
                }
                return false;
            } )
            .forEach((Node n) -> n.setIce(false));

    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < R && c >= 0 && c < C;
    }
}

class Node{
    int R;
    int C;
    boolean isIce;
    boolean isBird = false;
    boolean visit = false;

    public boolean isVisit() {
        return visit;
    }

    public void setVisit(boolean visit) {
        this.visit = visit;
    }

    public Node() {
    }

    public Node(int r, int c, boolean isIce, boolean isBird, boolean visit) {
        R = r;
        C = c;
        this.isIce = isIce;
        this.isBird = isBird;
        this.visit = visit;
    }

    public Node nodeCopy(){
        return new Node(this.R, this.C, this.isIce, this.isBird, this.visit);
    }

    public static boolean collectionHasNode(Collection<Node> li, Node node) {
        for (Node check : li) {
            if (check.equals(node)) return true;
        }
        return false;
    }

    public static Node findNode(int r, int c, Collection<Node> target) {
        for (Node node : target) {
            if (node.getR() == r && node.getC() == c) return node;
        }
        return null;
    }

    public Node(int r, int c, boolean isIce) {
        R = r;
        C = c;
        this.isIce = isIce;
    }

    public int getR() {
        return R;
    }

    public void setR(int r) {
        R = r;
    }

    public int getC() {
        return C;
    }

    public void setC(int c) {
        C = c;
    }

    public boolean isIce() {
        return isIce;
    }

    public void setIce(boolean ice) {
        isIce = ice;
    }

    public boolean isBird() {
        return isBird;
    }

    public void setBird(boolean bird) {
        isBird = bird;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Node) {
            return ((Node)obj).getR() == this.getR() && ((Node)obj).getC() == this.getC();
        }
        return false;
    }
}