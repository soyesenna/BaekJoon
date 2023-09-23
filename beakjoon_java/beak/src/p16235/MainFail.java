package p16235;

import java.io.*;
import java.util.*;
public class MainFail {

    public static int N;
    public static int M;
    public static int K;
    public static List<List<Integer>> land = new ArrayList<>();
    public static List<List<Integer>> s2d2 = new ArrayList<>();
    public static List<List<Integer>> trees = new ArrayList<>();
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
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                tmp.add(5);
            }
            land.add(tmp);
        }

        userInput(N, s2d2, br);
        userInput(M, trees, br);

        Collections.sort(trees, (List<Integer> li1, List<Integer> li2) -> li2.get(2) - li1.get(2));
        while (K > 0){
            spring();
            summer();
            autumn();
            winter();
            K--;
        }

        System.out.println(trees.size());
    }

    public static void spring(){
        for (int i = trees.size() - 1; i >= 0; i--) {
            List<Integer> tree = trees.get(i);
            int nowR = tree.get(0) - 1;
            if (nowR < 0) continue;
            int nowC = tree.get(1) - 1;
            int age = tree.get(2);
            int landM = land.get(nowR).get(nowC);
            if (landM >= age){
                land.get(nowR).set(nowC, landM - age);
                tree.set(2, ++age);
            }else{
                deadTrees.add(new ArrayList<>(List.of(nowR + 1, nowC + 1, age)));
                tree.set(0, -1);
            }
        }
    }
    public static void summer(){
        for (List<Integer> deadTree : deadTrees) {
            int nowR = deadTree.get(0) - 1;
            int nowC = deadTree.get(1) - 1;
            int age = (int) (deadTree.get(2) / 2);
            land.get(nowR).set(nowC, land.get(nowR).get(nowC) + age);
        }
        deadTrees = new ArrayList<>();
    }
    public static void autumn(){
        List<List<Integer>> tmp = new ArrayList<>();
        List<List<Integer>> tmp2 = new ArrayList<>();
        for (List<Integer> tree : trees) {
            if (tree.get(0) > 0) {
                tmp.add(new ArrayList<>(List.of(tree.get(0), tree.get(1), tree.get(2))));
                if (tree.get(2) % 5 == 0) {
                    for (List<Integer> dir : direction) {
                        int nowR = tree.get(0) + dir.get(0);
                        int nowC = tree.get(1) + dir.get(1);

                        if (inRange(nowR, nowC)) tmp2.add(new ArrayList<>(List.of(nowR, nowC, 1)));
                    }
                }
            }
        }

        tmp.addAll(tmp2);
        trees = tmp;
    }
    public static void winter(){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int nowLand = land.get(i).get(j);
                land.get(i).set(j, nowLand + s2d2.get(i).get(j));
            }
        }
    }


    public static boolean inRange(int r, int c) {
        return r >= 1 && r <= N && c >= 1 && c <= N;
    }

    public static void userInput(int n, List<List<Integer>> dest, BufferedReader br) throws Exception{
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            List<Integer> tmpList = new ArrayList<>();
            for (String s : tmp) {
                tmpList.add(Integer.parseInt(s));
            }
            dest.add(tmpList);
        }
    }

}


