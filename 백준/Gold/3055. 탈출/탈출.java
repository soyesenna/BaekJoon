import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int R, C;
    static char[][] forest;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");
        R = Integer.parseInt(line[0]);
        C = Integer.parseInt(line[1]);

        forest = new char[R][C];
        visited = new boolean[R][C];

        Queue<int[]> waterQueue = new LinkedList<>();
        Queue<int[]> hedgehogQueue = new LinkedList<>();

        for (int i = 0; i < R; i++) {
            forest[i] = br.readLine().toCharArray();
            for (int j = 0; j < C; j++) {
                if (forest[i][j] == '*') {
                    waterQueue.add(new int[]{i, j});
                } else if (forest[i][j] == 'S') {
                    hedgehogQueue.add(new int[]{i, j});
                    visited[i][j] = true;
                }
            }
        }

        int result = bfs(waterQueue, hedgehogQueue);
        System.out.println(result == -1 ? "KAKTUS" : result);
    }

    private static int bfs(Queue<int[]> waterQueue, Queue<int[]> hedgehogQueue) {
        int time = 0;

        while (!hedgehogQueue.isEmpty()) {
            time++;
            int waterSize = waterQueue.size();
            for (int i = 0; i < waterSize; i++) {
                int[] water = waterQueue.poll();
                for (int j = 0; j < 4; j++) {
                    int nx = water[0] + dx[j];
                    int ny = water[1] + dy[j];

                    if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
                        if (forest[nx][ny] == '.' || forest[nx][ny] == 'S') {
                            forest[nx][ny] = '*';
                            waterQueue.add(new int[]{nx, ny});
                        }
                    }
                }
            }

            int hedgehogSize = hedgehogQueue.size();
            for (int i = 0; i < hedgehogSize; i++) {
                int[] hedgehog = hedgehogQueue.poll();
                for (int j = 0; j < 4; j++) {
                    int nx = hedgehog[0] + dx[j];
                    int ny = hedgehog[1] + dy[j];

                    if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
                        if (!visited[nx][ny]) {
                            if (forest[nx][ny] == 'D') {
                                return time;
                            } else if (forest[nx][ny] == '.') {
                                forest[nx][ny] = 'S';
                                visited[nx][ny] = true;
                                hedgehogQueue.add(new int[]{nx, ny});
                            }
                        }
                    }
                }
            }
        }

        return -1; // 비버의 굴로 갈 수 없는 경우
    }
}
