package p16235;

import java.io.*;
import java.util.*;

public class MainFail2 {

    public static int N;
    public static int M;
    public static int K;
    public static PriorityQueue<List<Integer>> trees = new PriorityQueue<>((List<Integer> a, List<Integer> b) -> a.get(2) - b.get(2));
    public static List<List<Integer>> neutrition = new ArrayList<>();
    public static List<List<Integer>> land = new ArrayList<>();
    public static List<List<Integer>> deadTrees = new ArrayList<>();
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


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            String[] tmp = br.readLine().split(" ");
            List<Integer> tmpList = new ArrayList<>();
            for (String s : tmp) {
                tmpList.add(Integer.parseInt(s));
            }
            neutrition.add(tmpList);
        }

        for (int i = 0; i < M; i++) {
            String[] tmp = br.readLine().split(" ");
            List<Integer> tmpList = new ArrayList<>();
            for (int j = 0; j < 3; j++) {
                int now = Integer.parseInt(tmp[j]);
                if (j < 2) now--;
                tmpList.add(now);
            }
            trees.add(tmpList);
        }

        for (int i = 0; i < N; i++) {
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                tmp.add(5);
            }
            land.add(tmp);
        }

        while (K > 0) {
            spring();
            summer();
            autumn();
            winter();
            K--;
        }
        System.out.println(trees.size());
    }
    public static void spring(){
        PriorityQueue<List<Integer>> tmp = new PriorityQueue<>((List<Integer> a, List<Integer> b) -> a.get(2) - b.get(2));
        while(!trees.isEmpty()) {
            List<Integer> now = trees.poll();
            int nowR = now.get(0);
            int nowC = now.get(1);
            int age = now.get(2);
            if (land.get(nowR).get(nowC)>= age) {
                land.get(nowR).set(nowC, land.get(nowR).get(nowC) - age);
                now.set(2, ++age);
                tmp.add(now);
            }else{
                deadTrees.add(now);
            }

        }
        trees = tmp;
    }
    public static void summer(){
        for (List<Integer> deadTree : deadTrees) {
            int nowR = deadTree.get(0);
            int nowC = deadTree.get(1);
            int age = deadTree.get(2);
            land.get(nowR).set(nowC, land.get(nowR).get(nowC) + (int)(age / 2));
        }
        deadTrees = new ArrayList<>();
    }
    public static void autumn(){
        PriorityQueue<List<Integer>> tmp = new PriorityQueue<>((List<Integer> a, List<Integer> b) -> a.get(2) - b.get(2));

        while(!trees.isEmpty()) {
            List<Integer> tree = trees.poll();
            tmp.add(tree);
            if (tree.get(2) % 5 == 0) {
                for (List<Integer> dir : direction) {
                    int nowR = tree.get(0) + dir.get(0);
                    int nowC = tree.get(1) + dir.get(1);
                    if (inRange(nowR, nowC)) tmp.add(new ArrayList<>(List.of(nowR, nowC, 1)));
                }
            }
        }
        trees = tmp;
    }

    public static void winter() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int nowLand = land.get(i).get(j);
                land.get(i).set(j, nowLand + neutrition.get(i).get(j));
            }
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < N;
    }
}
