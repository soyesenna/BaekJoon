
import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {

    public static BigInteger start;
    public static BigInteger target;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        start = BigInteger.valueOf(Long.parseLong(st.nextToken()));
        target = BigInteger.valueOf(Long.parseLong(st.nextToken()));

        System.out.println(bfs());

    }

    public static String bfs() {
        Deque<Node> queue = new ArrayDeque<>();
        boolean[] visit = new boolean[1000000000 + 1];
        visit[start.intValue()] = true;
        queue.add(new Node(start, ""));

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            if (now.val.intValue() == target.intValue()) {
                if (now.sb.toString().equals("")) return"0";
                return now.sb.toString();
            }

            visit[now.val.intValue()] = true;

            List<Node> nowResult = Order.doOrder(now);
            for (Node node : nowResult) {
                if (node != null && !visit[node.val.intValue()]) {
                    queue.add(node);
                    visit[node.val.intValue()] = true;
                }
            }

        }
        return "-1";
    }


}

class Order {
    public static List<Node> doOrder(Node now) {
        List<Node> result = new ArrayList<>();
        result.add(multiply(new Node(now)));
        result.add(plus(new Node(now)));
        result.add(minus(new Node(now)));
        result.add(divide(new Node(now)));
        return result;
    }

    private static Node plus(Node node) {
        Node result = new Node(node.val.add(node.val), node.sb);
        if (result.val.compareTo(BigInteger.valueOf(1000000001)) >= 0) return null;

        result.sb.append("+");
        return result;
    }

    private static Node minus(Node node) {
        Node result = new Node(node.val.subtract(node.val), node.sb);
        if (result.val.compareTo(BigInteger.ZERO) <= 0) return null;
        result.sb.append("-");
        return result;
    }

    private static Node multiply(Node node) {
        Node result = new Node(node.val.multiply(node.val), node.sb);
        if (result.val.compareTo(BigInteger.valueOf(1000000001)) >= 0) return null;
        result.sb.append("*");
        return result;
    }

    private static Node divide(Node node) {
        if (node.val.intValue() == 0) return null;
        Node result = new Node(node.val.divide(node.val), node.sb);
        result.sb.append("/");
        return result;
    }
}

class Node {
    BigInteger val;
    StringBuilder sb = new StringBuilder();

    public Node(BigInteger now, StringBuilder sb) {
        this.val = now;
        this.sb.append(sb);
    }

    public Node(BigInteger now, String s) {
        this.val = now;
        this.sb.append(s);
    }

    public Node(Node node) {
        this.val = BigInteger.valueOf(node.val.intValue());
        this.sb.append(node.sb);
    }
}
