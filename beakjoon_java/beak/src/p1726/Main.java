package p1726;

import java.io.*;
import java.util.*;
import java.util.function.BiFunction;
import java.util.function.Function;

public class Main {

    public static int N;
    public static int M;
    public static int[][] space;
    public static boolean[][] visit;
    public static int[][][] dirVisit;
    public static List<Integer> goal = new ArrayList<>();
    public static List<Integer> resultCnt = new ArrayList<>();
    public static List<BiFunction<List<Integer>, Integer, List<Integer>>> order = new ArrayList<>(
            List.of(
                    //move order
                    (List<Integer> list, Integer moveCnt) -> {
                        switch (list.get(2)) {
                            case 0:
                                list.set(1, list.get(1) + moveCnt);
                                break;
                            case 1:
                                list.set(0, list.get(0) + moveCnt);
                                break;
                            case 2:
                                list.set(1, list.get(1) - moveCnt);
                                break;
                            case 3:
                                list.set(0, list.get(0) - moveCnt);
                                break;
                        }
                        return new ArrayList<>(list);
                    },
                    //turn right order
                    (List<Integer> list, Integer moveCnt) -> {
                        list.set(2, list.get(2) + 1);
                        if (list.get(2) > 3) list.set(2, list.get(2) - 4);
                        return new ArrayList<>(list);
                    },
                    //turn left order
                    (List<Integer> list, Integer moveCnt) -> {
                        list.set(2, list.get(2) - 1);
                        if (list.get(2) < 0) list.set(2, list.get(2) + 4);
                        return new ArrayList<>(list);
                    }
            )
    );

    /*
    0 : 동
    1 : 남
    2 : 서
    3 : 북
     */

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        space = new int[N][M];
        visit = new boolean[N][M];
        dirVisit = new int[N][M][4];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                space[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        List<Integer> robot = new ArrayList<>();
        while (st.hasMoreTokens()) {
            robot.add(Integer.parseInt(st.nextToken()) - 1);
        }
        if (robot.get(2) == 1) robot.set(2, 2);
        else if(robot.get(2) == 2) robot.set(2, 1);
        robot.add(0);

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            goal.add(Integer.parseInt(st.nextToken()) - 1);
        }
        if (goal.get(2) == 1) goal.set(2, 2);
        else if(goal.get(2) == 2) goal.set(2, 1);

        bfs(robot);

        System.out.println(resultCnt);

    }

    public static void bfs(List<Integer> start) {
        Deque<List<Integer>> queue = new ArrayDeque<>();
        queue.add(new ArrayList<>(start));
        visit[start.get(0)][start.get(1)] = true;
        dirVisit[start.get(0)][start.get(1)][start.get(2)] = 1;


        //List -> r, c, d, cnt
        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            visit[now.get(0)][now.get(1)] = true;
            if (now.get(0).equals(goal.get(0)) && now.get(1).equals(goal.get(1)) && now.get(2).equals(goal.get(2))) {
                resultCnt.add(now.get(3));
            }

            boolean moveOrder = true;
            List<List<Integer>> moveResult = new ArrayList<>();
            for (BiFunction<List<Integer>, Integer, List<Integer>> function : order) {
                if (moveOrder){
                    for (int i = 1; i <= 3; i++) {
                        moveResult.add(function.apply(new ArrayList<>(now), i));
                    }
                    moveOrder = false;
                    continue;
                }
                moveResult.add(function.apply(new ArrayList<>(now), 0));
            }

            for (List<Integer> list : moveResult) {
                if (list.get(0).equals(now.get(0)) && list.get(1).equals(now.get(1))) {
                    if (dirVisit[list.get(0)][list.get(1)][list.get(2)] == 0) {
                        list.set(3, list.get(3) + 1);
                        queue.add(new ArrayList<>(list));
                        dirVisit[list.get(0)][list.get(1)][list.get(2)] = 1;
                    }
                }else{
                    if (inRange(list.get(0), list.get(1)) 
                            && space[list.get(0)][list.get(1)] != 1 && dirVisit[list.get(0)][list.get(1)][list.get(2)] == 0) {
                        list.set(3, list.get(3) + 1);
                        queue.add(new ArrayList<>(list));
                        visit[list.get(0)][list.get(1)] = true;
                        dirVisit[list.get(0)][list.get(1)][list.get(2)] = 1;
                    }
                }
            }

        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
