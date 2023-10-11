
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
	
	public static int N;
	public static int K;
	public static int S;
	public static int x;
	public static int y;
	public static int[][] space;
	public static Deque<Node> infection = new ArrayDeque<>();
	public static List<List<Integer>> direction = List.of(
			List.of(-1, 0),
			List.of(0, 1),
			List.of(1, 0),
			List.of(0, -1)
	);

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		space = new int[N][N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int now = Integer.parseInt(st.nextToken());
				if (now != 0) {
					infection.add(new Node(i, j, now));
				}
				space[i][j] = now;
			}
		}

		st = new StringTokenizer(br.readLine());
		S = Integer.parseInt(st.nextToken());
		x = Integer.parseInt(st.nextToken());
		y = Integer.parseInt(st.nextToken());

		infection = infection.stream()
							.sorted((Node n1, Node n2) -> n1.virusNum - n2.virusNum)
							.collect(Collectors.toCollection(ArrayDeque::new));

		while (S > 0){
			doInfect();
			S--;
		}

		System.out.println(space[x - 1][y - 1]);

	}

	public static void doInfect() {
		Deque<Node> queue = new ArrayDeque<>();

		while (!infection.isEmpty()) {
			Node now = infection.pollFirst();

			for (List<Integer> dir : direction) {
				int nowR = now.r + dir.get(0);
				int nowC = now.c + dir.get(1);
				if (inRange(nowR, nowC) && space[nowR][nowC] == 0) {
					queue.add(new Node(nowR, nowC, now.virusNum));
					space[nowR][nowC] = now.virusNum;;
				}
			}
		}
		infection = queue;
	}

	public static boolean inRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}
	


}

class Node {
	int r, c;
	int virusNum;

	public Node(int r, int c, int virusNum) {
		this.r = r;
		this.c = c;
		this.virusNum = virusNum;
	}
}