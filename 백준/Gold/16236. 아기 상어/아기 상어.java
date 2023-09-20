
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static int N;
    public static List<List<Integer>> space = new ArrayList<>();
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static int time = 0;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        Shark shark = new Shark();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            List<Integer> tmpList = new ArrayList<>();
            int j = 0;
            while (st.hasMoreTokens()) {
                int a = Integer.parseInt(st.nextToken());
                if (a == 9) {
                    shark.setR(i);
                    shark.setC(j);
                    a = 0;
                }
                tmpList.add(a);
                j++;
            }
            space.add(tmpList);
        }

        while (bfs(shark)){
           // System.out.println(shark.getR());
            //System.out.println(shark.getC());
        }
        System.out.println(time);
    }

    public static boolean bfs(Shark shark){
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(shark.getR(), shark.getC(), 0, 0));
        Set<Node> visit = new HashSet<>();

        boolean isFind = false;
        List<Node> find = new ArrayList<>();

        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();
            visit.add(now);

            for (List<Integer> dir : direction) {
                int nowR = now.getR() + dir.get(0);
                int nowC = now.getC() + dir.get(1);

                if (inRange(nowR, nowC)){
                    Node next = new Node(nowR, nowC, space.get(nowR).get(nowC), now.getDistance() + 1);
                    boolean isVisit = false;
                    for (Node node : visit) {
                        if (node.getR() == next.getR() && node.getC() == next.getC()) {
                            isVisit = true;
                            break;
                        }
                    }
                    if (isVisit) continue;
                    if (next.getSize() != 0 && next.getSize() < shark.getSize()) {
                        find.add(next);
                        isFind = true;
                    }else if (next.getSize() == shark.getSize() || next.getSize() == 0) {
                        queue.add(next);
                        visit.add(next);
                    }
                }
            }
        }
        if (isFind) {
            Collections.sort(find, (Node n1, Node n2) -> {
                if (n1.getDistance() == n2.getDistance()) {
                    if (n1.getR() == n2.getR()) {
                        return n1.getC() - n2.getC();
                    } else {
                        return n1.getR() - n2.getR();
                    }
                } else {
                    return n1.getDistance() - n2.getDistance();
                }
            });
            space.get(find.get(0).getR()).set(find.get(0).getC(), 0);
            shark.setR(find.get(0).getR());
            shark.setC(find.get(0).getC());
            if (shark.getToGrow() == 1) {
                shark.setSize(shark.getSize() + 1);
                shark.setToGrow(shark.getSize());
            }else{
                shark.setToGrow(shark.getToGrow() - 1);
            }
            time += find.get(0).getDistance();
        }
        return isFind;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < N;
    }
}

class Node{
    int r;
    int c;
    int size;
    int distance;

    public Node(int r, int c, int size, int distance) {
        this.r = r;
        this.c = c;
        this.size = size;
        this.distance = distance;
    }

    public int getR() {
        return r;
    }

    public void setR(int r) {
        this.r = r;
    }

    public int getC() {
        return c;
    }

    public void setC(int c) {
        this.c = c;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }
}
 class Shark{

    int r;
    int c;
    int size = 2;
    int toGrow;

     public Shark() {
         toGrow = size;
     }

     Shark(int r, int c) {
         this.r = r;
         this.c = c;
         toGrow = size;
     }

     public int getR() {
         return r;
     }

     public void setR(int r) {
         this.r = r;
     }

     public int getC() {
         return c;
     }

     public void setC(int c) {
         this.c = c;
     }

     public int getSize() {
         return size;
     }

     public void setSize(int size) {
         this.size = size;
     }

     public int getToGrow() {
         return toGrow;
     }

     public void setToGrow(int grow) {
         this.toGrow = grow;
     }
 }