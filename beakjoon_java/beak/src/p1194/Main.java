package p1194;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static List<String> space = new ArrayList<>();
    public static int r;
    public static int c;
    public static List<Node> visit = new ArrayList<>();
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


        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            int me = str.indexOf('0');
            if (me != -1) {
                r = i;
                c = me;
            }
            space.add(str);
        }

        System.out.println(bfs(r, c));

    }

    public static int bfs(int r, int c) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(r, c, 0));
        visit.add(queue.peekFirst());

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit.add(now);

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);

                //System.out.println(visit.contains(new Node(nowR, nowC, now.cnt, now.newkeys())));

                if (inRange(nowR, nowC) && !visit.contains(new Node(nowR, nowC, now.cnt, now.newkeys()))) {
                    Node next = new Node(nowR, nowC, now.cnt + 1, now.newkeys());
                    char nowCharacter =  space.get(nowR).charAt(nowC);
                    if (nowCharacter == '.' || nowCharacter == '0') {
                        queue.add(next);
                        visit.add(next);
                    } else if (nowCharacter >= 'A' && nowCharacter <= 'Z') {
                        if (now.keys.contains((char)((int)nowCharacter + 32))) {
                            queue.add(next);
                            visit.add(next);
                        }
                    } else if (nowCharacter >= 'a' && nowCharacter <= 'z') {
                        next.keys.add(nowCharacter);
                        queue.add(next);
                        visit.add(next);
                    } else if (nowCharacter == '1') {
                        return now.cnt + 1;
                    }
                }
            }
        }

        return -1;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}

class Node{
    int r, c;
    int cnt = 0;
    List<Character> keys = new ArrayList<>();

    public Node() {
    }

    public Node(int r, int c, int cnt) {
        this.r = r;
        this.c = c;
        this.cnt = cnt;
    }

    public Node(int r, int c, int cnt, List<Character> keys) {
        this.r = r;
        this.c = c;
        this.cnt = cnt;
        this.keys = keys;
    }

    public List<Character> newkeys() {
        List<Character> tmp = new ArrayList<>();
        for (Character key : keys) {
            tmp.add(key);
        }
        return tmp;
    }

    public boolean keyEquals(List<Character> target) {
        target = new ArrayList<>(new HashSet<>(target));
        List<Character> thisKeys = new ArrayList<>(new HashSet<>(this.keys));
        if (target.size() != thisKeys.size()) return false;
        if (target.size() == 0) return true;

        return target.containsAll(thisKeys);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Node){
            return ((Node) obj).r == this.r && ((Node) obj).c == this.c && ((Node) obj).keyEquals(this.keys);
        }
        return false;
    }
}

