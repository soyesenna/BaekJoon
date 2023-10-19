package p9328;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static char[][] spcae;
    public static List<List<Integer>> canStart = new ArrayList<>();

    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );

    public static Set<Integer> result = new HashSet<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        while (T > 0) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            spcae = new char[N][M];
            canStart = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                spcae[i] = br.readLine().toCharArray();
                for (int j = 0; j < M; j++) {
                    if ((i == 0 || j == 0 || i == N - 1 || j == M - 1) && spcae[i][j] == '.') {
                        canStart.add(new ArrayList<>(List.of(i, j)));
                    }
                }
            }

            String firstKeys = br.readLine();

            List<Character> keys = new ArrayList<>();
            for (int i = 0; i < firstKeys.length(); i++) {
                keys.add(firstKeys.charAt(i));
            }

            for (List<Integer> start : canStart) {
                bfs(start.get(0), start.get(1), keys);
            }

            List<Integer> resultList = new ArrayList<>(result);
            Collections.sort(resultList);
            System.out.println(resultList.get(resultList.size() - 1));

            T--;
        }
    }

    public static void bfs(int r, int c, List<Character> keys) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(r, c, new ArrayList<>(keys), 0));
        List<List<Set<String>>> visit = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            List<Set<String>> tmp = new ArrayList<>();
            for (int j = 0; j < M; j++) {
                tmp.add(new HashSet<>());
            }
            visit.add(tmp);
        }

        visit.get(r).get(c).add(keys.toString());

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit.get(now.r).get(now.c).add(now.keys.toString());
            result.add(now.cnt);

            for (List<Integer> dir : direction) {
                int nowR = now.r + dir.get(0);
                int nowC = now.c + dir.get(1);

                if (inRange(nowR, nowC) && !visit.get(nowR).get(nowC).contains(now.keys.toString())) {
                    if (spcae[nowR][nowC] == '.' || spcae[nowR][nowC] == '$') {
                        Node next = new Node(nowR, nowC, new ArrayList<>(now.keys), now.cnt);
                        if (spcae[nowR][nowC] == '$') next.cnt++;
                        queue.add(next);
                        visit.get(nowR).get(nowC).add(next.keys.toString());
                    }else if(spcae[nowR][nowC] >= 'A' && spcae[nowR][nowC] <= 'Z' ){
                        if (now.keys.contains((char)(spcae[nowR][nowC] + 32))) {
                            queue.add(new Node(nowR, nowC, new ArrayList<>(now.keys), now.cnt));
                            visit.get(nowR).get(nowC).add(now.keys.toString());
                        }
                    } else if (spcae[nowR][nowC] >= 'a' && spcae[nowR][nowC] <= 'z') {
                        Node next = new Node(nowR, nowC, new ArrayList<>(now.keys), now.cnt);
                        next.keys.add(spcae[nowR][nowC]);
                        queue.add(next);
                        visit.get(nowR).get(nowC).add(next.keys.toString());
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
    List<Character> keys;
    int cnt = 0;

    public Node(int r, int c, List<Character> keys, int cnt) {
        this.r = r;
        this.c = c;
        this.keys = keys;
        this.cnt = cnt;
    }
}
