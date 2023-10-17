package p10711;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static Deque<Node> willRemove = new ArrayDeque<>();
    public static List<List<Node>> space = new ArrayList<>();
    //[dust cnt, str]

    //public static List<List<Integer>> dustCntAndStr = new ArrayList<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(-1, 1),
            List.of(0, 1),
            List.of(1, 1),
            List.of(1, 0),
            List.of(1, -1),
            List.of(0, -1),
            List.of(-1, -1)
    );
    public static int result = 0;


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            char[] tmp = br.readLine().toCharArray();
            List<Node> tmpList = new ArrayList<>();
            for (int j = 0; j < M; j++){
                if (tmp[j] == '.') tmpList.add(new Node(i, j, -1, 0, false));
                else tmpList.add(new Node(i, j, Character.digit(tmp[j], 10), 0, true));
            }
            space.add(tmpList);
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                Node now = space.get(i).get(j);
                if (now.isCastle) {
                    for (List<Integer> dir : direction) {
                        int nowR = now.r + dir.get(0);
                        int nowC = now.c + dir.get(1);
                        if (inRange(nowR, nowC) && !space.get(nowR).get(nowC).isCastle) now.dustCnt++;
                    }
                    if (now.dustCnt >= now.str) willRemove.add(now);
                }
            }
        }

        while (!willRemove.isEmpty()) {
            remove();
            result++;
        }

        System.out.println(result);

    }

    public static void remove(){
        Set<Node> tmp = new HashSet<>();
        while (!willRemove.isEmpty()) {
            Node now = willRemove.pollFirst();
            now.isCastle = false;
            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);
                if (inRange(nowR, nowC) && space.get(nowR).get(nowC).isCastle) {
                    Node next = space.get(nowR).get(nowC);
                    if (++next.dustCnt >= next.str) {
                        tmp.add(next);
                    }
                }
            }

        }

        for (Node node : tmp) {
            if (node.isCastle) willRemove.add(node);
        }

    }



    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}

class Node {
    int r, c;
    int str;
    int dustCnt;
    boolean isCastle;

    public Node(int r, int c, int str, int dustCnt, boolean isCastle) {
        this.r = r;
        this.c = c;
        this.str = str;
        this.dustCnt = dustCnt;
        this.isCastle = isCastle;
    }
}