package p17142;

import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static int M;
    public static List<Node> space = new ArrayList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int n = Integer.parseInt(st.nextToken());
                space.add(new Node(i, j, n == 1, n == 2));
            }
        }



    }
}

class Node {
    int r, c;
    boolean isWall;
    boolean isVirus;

    public Node(int r, int c, boolean isWall, boolean isVirus) {
        this.r = r;
        this.c = c;
        this.isWall = isWall;
        this.isVirus = isVirus;
    }
}