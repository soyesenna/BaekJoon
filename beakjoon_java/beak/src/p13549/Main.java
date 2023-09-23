package p13549;

import java.io.*;
import java.util.*;
public class Main {

    public static int start;
    public static int target;
    public static List<Integer> direction = List.of(-1, 1, 2);

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        start = Integer.parseInt(st.nextToken());
        target = Integer.parseInt(st.nextToken());

        System.out.println(bfs());
    }

    public static int bfs(){
        Deque<List<Integer>> queue = new ArrayDeque<>();
        Map<Integer, Integer> visit = new HashMap<>();
        //현재 점, 이동 횟수
        queue.add(new ArrayList<>(List.of(start, 0)));
        visit.put(start, 0);

        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            if (now.get(0) == target) return now.get(1);
            if (visit.containsKey(now.get(0)) && visit.get(now.get(0)) < now.get(1)) continue;
            visit.putIfAbsent(now.get(0), now.get(1));

            for (Integer dir : direction) {
                int next = now.get(0);
                int nextTime = now.get(1);
                if (dir == 2){
                    next *= 2;
                }else{
                    next += dir;
                    nextTime++;
                }

                if (!visit.containsKey(next)) {
                    visit.put(next, now.get(1) + 1);
                    queue.add(new ArrayList<>(List.of(next, nextTime)));
                }else if(visit.get(next) > now.get(1) + 1){
                    visit.replace(next, now.get(1) + 1);
                    queue.add(new ArrayList<>(List.of(next, nextTime)));
                }
            }

        }
        return 0;
    }
}
