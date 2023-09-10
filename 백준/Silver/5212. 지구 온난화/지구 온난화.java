import java.io.*;
import java.util.*;

public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static int countSea(int x, int y, char[][] grid) {
        int count = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= grid.length || ny < 0 || ny >= grid[0].length || grid[nx][ny] == '.') {
                count++;
            }
        }
        return count;
    }

    public static char[][] solve(char[][] grid) {
        char[][] newGrid = new char[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 'X') {
                    if (countSea(i, j, grid) >= 3) {
                        newGrid[i][j] = '.';
                    } else {
                        newGrid[i][j] = 'X';
                    }
                } else {
                    newGrid[i][j] = '.';
                }
            }
        }
        return newGrid;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        char[][] grid = new char[R][C];
        for (int i = 0; i < R; i++) {
            grid[i] = br.readLine().toCharArray();
        }

        grid = solve(grid);

        int min_x = Integer.MAX_VALUE, max_x = Integer.MIN_VALUE, min_y = Integer.MAX_VALUE, max_y = Integer.MIN_VALUE;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (grid[i][j] == 'X') {
                    min_x = Math.min(min_x, i);
                    max_x = Math.max(max_x, i);
                    min_y = Math.min(min_y, j);
                    max_y = Math.max(max_y, j);
                }
            }
        }

        for (int i = min_x; i <= max_x; i++) {
            for (int j = min_y; j <= max_y; j++) {
                System.out.print(grid[i][j]);
            }
            System.out.println();
        }
    }
}
