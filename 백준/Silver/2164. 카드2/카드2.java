
import java.io.*;
import java.util.*;
public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            queue.add(i);
        }

        while (queue.size() > 1) {
            queue.pollFirst();
            int now = queue.pollFirst();
            queue.add(now);
        }

        System.out.println(queue.pollFirst());
    }
}
