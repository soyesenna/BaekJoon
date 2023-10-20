package p9019;

import java.io.*;
import java.util.*;
import java.util.function.Function;

public class Main {

    public static int start;
    public static int target;
    public static List<Function<Integer, List<Object>>> order = new ArrayList<>(
            List.of(
                    (Integer num) -> {
                        List<Object> result = new ArrayList<>();
                        result.add((num * 2) % 10000);
                        result.add("D");
                        return result;
                    },
                    (Integer num) -> {
                        List<Object> result = new ArrayList<>();
                        result.add((num - 1) < 0 ? 9999 : num - 1);
                        result.add("S");
                        return result;
                    },
                    (Integer num) -> {
                        StringBuilder sb = new StringBuilder(Integer.toString(num, 10));
                        int len = sb.length();
                        for (int i = 0; i < 4 - len; i++) {
                            sb.insert(0, 0);
                        }
                        char c = sb.charAt(0);
                        sb.deleteCharAt(0);
                        sb.append(c);
                        List<Object> result = new ArrayList<>();
                        result.add(Integer.parseInt(sb.toString()));
                        result.add("L");
                        return result;
                    },
                    (Integer num) -> {
                        StringBuilder sb = new StringBuilder(Integer.toString(num, 10));
                        int len = sb.length();
                        for (int i = 0; i < 4 - len; i++) {
                            sb.insert(0, 0);
                        }
                        char c = sb.charAt(sb.length() - 1);
                        sb.deleteCharAt(sb.length() - 1);
                        sb.insert(0, c);
                        List<Object> result = new ArrayList<>();
                        result.add(Integer.parseInt(sb.toString()));
                        result.add("R");
                        return result;
                    }
            )
    );



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());

        StringTokenizer st;



        while (T > 0) {

            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            target = Integer.parseInt(st.nextToken());

            StringBuilder res = bfs(start);
            res.append("\n");

            bw.write(res.toString());
            bw.flush();
            T--;
        }
    }

    public static StringBuilder bfs(int start) {
        Deque<Node> queue = new ArrayDeque<>();
        boolean[] visit = new boolean[10001];
        queue.add(new Node(start));
        visit[start] = true;

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit[now.num] = true;
            if (now.num == target) {
                queue.clear();
                return now.sb;
            }

            for (Function<Integer, List<Object>> o : order) {
                List<Object> nowResult = o.apply(now.num);
                if (!visit[(int)nowResult.get(0)]) {
                    Node next = new Node((int)nowResult.get(0));
                    next.sb.append(now.sb);
                    next.sb.append(nowResult.get(1));
                    queue.add(next);
                    visit[next.num] = true;
                }
            }
        }

        return null;
    }
}

class Node {
    int num;
    StringBuilder sb = new StringBuilder();

    public Node(int num) {
        this.num = num;
    }


}