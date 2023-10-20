
import java.io.*;
import java.util.*;
import java.util.function.Function;

public class Main {

    public static int start;
    public static int target;
    



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

            int res = orderD(now.num);
            if (!visit[res]){
                Node next = new Node(res);
                next.sb.append(now.sb);
                next.sb.append('D');
                queue.add(next);
                visit[next.num] = true;
            }

            res = orderS(now.num);
            if (!visit[res]){
                Node next = new Node(res);
                next.sb.append(now.sb);
                next.sb.append('S');
                queue.add(next);
                visit[next.num] = true;
            }

            res = orderL(now.num);
            if (!visit[res]){
                Node next = new Node(res);
                next.sb.append(now.sb);
                next.sb.append('L');
                queue.add(next);
                visit[next.num] = true;
            }

            res = orderR(now.num);
            if (!visit[res]){
                Node next = new Node(res);
                next.sb.append(now.sb);
                next.sb.append('R');
                queue.add(next);
                visit[next.num] = true;
            }


        }

        return null;
    }

    public static int orderD(int n) {
        return (n * 2) % 10000;
    }

    public static int orderS(int n) {
        return (n - 1) < 0 ? 9999 : n - 1;
    }

    public static int orderL(int num) {
        StringBuilder sb = new StringBuilder(Integer.toString(num, 10));
        int len = sb.length();
        for (int i = 0; i < 4 - len; i++) {
            sb.insert(0, 0);
        }
        char c = sb.charAt(0);
        sb.deleteCharAt(0);
        sb.append(c);
        return Integer.parseInt(sb.toString());
    }

    public static int orderR(int num) {
        StringBuilder sb = new StringBuilder(Integer.toString(num, 10));
        int len = sb.length();
        for (int i = 0; i < 4 - len; i++) {
            sb.insert(0, 0);
        }
        char c = sb.charAt(sb.length() - 1);
        sb.deleteCharAt(sb.length() - 1);
        sb.insert(0, c);
        return Integer.parseInt(sb.toString());
    }
}

class Node {
    int num;
    StringBuilder sb = new StringBuilder();

    public Node(int num) {
        this.num = num;
    }


}